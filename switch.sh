#!/bin/bash

echo "Fetching remote branches..."
git fetch --all

CUR_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $CUR_BRANCH"

############################################
# 1. 檢查未儲存變更 (包含備份檔)
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
# 2. 精確檢查 Commit 狀態
############################################
BEHIND_COUNT=$(git rev-list --count HEAD..origin/$CUR_BRANCH)
AHEAD_COUNT=$(git rev-list --count origin/$CUR_BRANCH..HEAD)

if [ "$BEHIND_COUNT" -gt 0 ] && [ "$AHEAD_COUNT" -gt 0 ]; then
    echo "------------------------------------------------"
    echo "🚨 REAL CONFLICT: Both you and GitHub have new work!"
    echo "------------------------------------------------"
    echo "1) Discard local / 2) Normal Push / 3) BACKUP, SYNC & UPLOAD (Recommended)"
    echo "4) Cancel"
    read -p "Choose (1-4): " merge_choice

    case $merge_choice in
        1)
            git reset --hard origin/$CUR_BRANCH
            ;;
        2)
            # 嘗試普通 Push，若遠端較新會失敗，這是安全的
            git push origin $CUR_BRANCH || echo "Push rejected. Please use Option 3 to sync."
            ;;
        3)
            echo "📦 Backing up unique files..."
            git diff --name-only HEAD origin/$CUR_BRANCH | while IFS= read -r file; do
                if [ -f "$file" ]; then
                    dir=$(dirname "$file")
                    mkdir -p "$dir/local_backup"
                    cp "$file" "$dir/local_backup/$(basename "$file")"
                    echo " -> Backed up: $file"
                fi
            done
            
            echo "💾 Committing backups to local history..."
            git add .
            git commit -m "Add local backup of conflicted files"
            
            echo "🔄 Rebase-pulling from GitHub (Safely merging history)..."
            # 使用 rebase 把你的備份 commit 接在雲端更新之後
            if git pull --rebase origin $CUR_BRANCH; then
                echo "⬆️ Uploading synchronized version to GitHub..."
                git push origin $CUR_BRANCH
                echo "✅ Success! GitHub now has your code and the backups."
            else
                echo "❌ Rebase failed due to severe conflict. Manual merge required."
                # 若 rebase 失敗，通常需要手動處理
            fi
            ;;
        *)
            exit 1
            ;;
    esac

elif [ "$BEHIND_COUNT" -gt 0 ]; then
    echo "☁️ GitHub is ahead. Pulling updates..."
    git pull --rebase origin $CUR_BRANCH

elif [ "$AHEAD_COUNT" -gt 0 ]; then
    echo "🚀 Your local is ahead. Pushing to GitHub..."
    git push origin $CUR_BRANCH
fi

############################################
# 3. 互動式分支切換
############################################
REMOTE_BRANCHES=($(git branch -r | sed 's/origin\///' | grep -v 'HEAD' | sort))
echo -e "\nRemote branches:"
for i in "${!REMOTE_BRANCHES[@]}"; do echo "$i) ${REMOTE_BRANCHES[$i]}"; done

read -p "Enter index to switch: " NEW_IDX
if [[ -n "$NEW_IDX" ]]; then
    NEW_BRANCH=${REMOTE_BRANCHES[$NEW_IDX]}
    git checkout $NEW_BRANCH
    git pull --rebase origin $NEW_BRANCH 2>/dev/null
fi