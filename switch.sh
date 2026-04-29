#!/bin/bash

echo "Fetching remote branches..."
git fetch --all

# 取得當前 branch
CUR_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $CUR_BRANCH"

############################################
# 1. 檢查是否有未儲存變更 (包含備份夾)
############################################
if [[ -n "$(git status --porcelain)" ]]; then
    echo "⚠️ You have uncommitted changes."
    read -p "Save and commit them now? (Y/n): " save_choice
    if [[ "$save_choice" == "Y" || "$save_choice" == "y" ]]; then
        git add .
        git commit -m "Auto-save: $(date +'%Y-%m-%d %H:%M:%S')"
    else
        echo "Proceeding without committing..."
    fi
fi

############################################
# 2. 精確檢查 Commit 狀態 (The Merger)
############################################
BEHIND_COUNT=$(git rev-list --count HEAD..origin/$CUR_BRANCH)
AHEAD_COUNT=$(git rev-list --count origin/$CUR_BRANCH..HEAD)

if [ "$BEHIND_COUNT" -gt 0 ] && [ "$AHEAD_COUNT" -gt 0 ]; then
    echo "------------------------------------------------"
    echo "🚨 REAL CONFLICT: Both you and GitHub have new work!"
    echo "------------------------------------------------"
    echo "1) Discard local commits (Use GitHub version)"
    echo "2) Normal Push (Might fail if behind)"
    echo "3) BACKUP, SYNC & UPLOAD (Safe Merge)"
    echo "4) Cancel"
    read -p "Choose (1-4): " merge_choice

    case $merge_choice in
        1)
            git reset --hard origin/$CUR_BRANCH
            ;;
        2)
            git push origin $CUR_BRANCH || echo "Push rejected. Use Option 3."
            ;;
        3)
            echo "📦 Backing up unique files..."
            # 備份差異檔案，但不備份備份資料夾本身
            git diff --name-only HEAD origin/$CUR_BRANCH | grep -v "local_backup/" | while IFS= read -r file; do
                if [ -f "$file" ]; then
                    dir=$(dirname "$file")
                    mkdir -p "$dir/local_backup"
                    cp "$file" "$dir/local_backup/$(basename "$file")"
                    echo " -> Backed up: $file"
                fi
            done
            
            echo "💾 Committing backups..."
            git add .
            git commit -m "Add local backup of conflicted files"
            
            echo "🔄 Rebase-pulling from GitHub..."
            if git pull --rebase origin $CUR_BRANCH; then
                echo "⬆️ Uploading to GitHub..."
                git push origin $CUR_BRANCH
                echo "✅ Success! Backups are now on GitHub."
            else
                echo "❌ Severe conflict. Please resolve manually."
                exit 1
            fi
            ;;
        *)
            exit 1
            ;;
    esac

elif [ "$BEHIND_COUNT" -gt 0 ]; then
    echo "☁️ GitHub is ahead. Auto-syncing..."
    git pull --rebase origin $CUR_BRANCH

elif [ "$AHEAD_COUNT" -gt 0 ]; then
    echo "🚀 Your local is ahead. Pushing..."
    git push origin $CUR_BRANCH
fi

############################################
# 3. 取得遠端分支 (Fixed Sort: main is index 0)
############################################
# 1. 取得原始清單並過濾掉 HEAD
RAW_LIST=$(git branch -r | sed 's/origin\///' | grep -v 'HEAD')

# 2. 分離 main 與其他分支
MAIN_EXISTS=$(echo "$RAW_LIST" | grep -w "main")
OTHER_BRANCHES=$(echo "$RAW_LIST" | grep -v -w "main" | sort)

# 3. 組合清單
FINAL_LIST=()
if [ -n "$MAIN_EXISTS" ]; then
    FINAL_LIST+=("main")
fi

while read -r line; do
    if [ -n "$line" ]; then
        FINAL_LIST+=("$line")
    fi
done <<< "$OTHER_BRANCHES"

echo -e "\nRemote branches on GitHub:"
for i in "${!FINAL_LIST[@]}"; do
    echo "$i) ${FINAL_LIST[$i]}"
done

############################################
# 4. 互動式切換
############################################
read -p "Enter index to switch: " NEW_IDX

if [[ -n "$NEW_IDX" && "$NEW_IDX" =~ ^[0-9]+$ ]] && [ "$NEW_IDX" -lt "${#FINAL_LIST[@]}" ]; then
    TARGET_BRANCH=${FINAL_LIST[$NEW_IDX]}
    echo "Switching to '$TARGET_BRANCH'..."
    
    if git show-ref --verify --quiet refs/heads/$TARGET_BRANCH; then
        git checkout $TARGET_BRANCH
    else
        git checkout -b $TARGET_BRANCH origin/$TARGET_BRANCH
    fi
    
    # 切換後確保是最新的
    git pull --rebase origin $TARGET_BRANCH 2>/dev/null
    echo "Successfully switched to $TARGET_BRANCH."
else
    echo "Staying on $CUR_BRANCH."
fi