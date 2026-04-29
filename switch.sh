#!/bin/bash

echo "Fetching remote branches..."
git fetch --all

CUR_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $CUR_BRANCH"

############################################
# 1. 檢查未儲存變更 (排除備份資料夾)
############################################
if [[ -n "$(git status --porcelain | grep -v "all_local_backups/")" ]]; then
    echo "⚠️ You have uncommitted changes."
    read -p "Save and commit them? (Y/n): " save_choice
    if [[ "$save_choice" == [Yy]* ]]; then
        git add .
        git commit -m "Auto-save: $(date +'%Y-%m-%d %H:%M:%S')"
    fi
fi

############################################
# 2. 精確檢查 Commit 狀態
############################################
BEHIND_COUNT=$(git rev-list --count HEAD..origin/$CUR_BRANCH)
AHEAD_COUNT=$(git rev-list --count origin/$CUR_BRANCH..HEAD)

if [ "$BEHIND_COUNT" -gt 0 ] && [ "$AHEAD_COUNT" -gt 0 ]; then
    echo "------------------------------------------------"
    echo "🚨 CONFLICT: Diverged from GitHub."
    echo "------------------------------------------------"
    echo "1) Discard local / 2) Normal Push / 3) BACKUP & AUTO-RESOLVE (Safe Align)"
    echo "4) Cancel"
    read -p "Choose (1-4): " merge_choice

    case $merge_choice in
        1) git reset --hard origin/$CUR_BRANCH ;;
        2) git push origin $CUR_BRANCH ;;
        3)
            echo "📦 Backing up local versions to 'all_local_backups'..."
            BACKUP_TIMESTAMP=$(date +%Y%m%d_%H%M%S)
            BACKUP_ROOT="all_local_backups/$BACKUP_TIMESTAMP"
            mkdir -p "$BACKUP_ROOT"

            # 備份 Local 內容並標註路徑
            git diff --name-only HEAD origin/$CUR_BRANCH | grep -v "all_local_backups/" | while read -r file; do
                if [ -f "$file" ]; then
                    dest="$BACKUP_ROOT/$file"
                    mkdir -p "$(dirname "$dest")"
                    cp -f "$file" "$dest"
                    
                    extension="${file##*.}"
                    case "$extension" in
                        py|sh|yml|yaml|txt|conf) comment="#" ;;
                        c|cpp|h|hpp|java|js|ts|cs|go|rs) comment="//" ;;
                        html|xml) comment="" ;;
                        css) comment="/* Original Path: ${file} */" ;;
                        *) comment="--" ;;
                    esac
                    
                    if [[ "$extension" == "html" || "$extension" == "xml" || "$extension" == "css" ]]; then
                        sed -i "1i ${comment}" "$dest"
                    else
                        sed -i "1i ${comment} Original Path: ${file}" "$dest"
                    fi
                    echo " -> Backed up: $file"
                fi
            done
            
            git add .
            git commit -m "Add local backup: $BACKUP_TIMESTAMP"
            
            echo "🔄 Synchronizing history with GitHub..."
            # 使用 -X theirs 進行初步 Rebase
            git pull --rebase -X theirs origin $CUR_BRANCH
            
            # 【核心修正】強制將主檔案內容同步為遠端版本
            echo "🎯 Aligning workspace with GitHub content (Keeping local in backups)..."
            git checkout origin/$CUR_BRANCH -- .
            
            # 提交這個對齊動作並推送
            git add .
            git commit --amend --no-edit
            git push origin $CUR_BRANCH
            
            echo "------------------------------------------------"
            echo "✅ DONE!"
            echo "Project files: Updated to GitHub version."
            echo "Local backup: Saved in $BACKUP_ROOT"
            echo "------------------------------------------------"
            ;;
        *) exit 1 ;;
    esac

elif [ "$BEHIND_COUNT" -gt 0 ]; then
    echo "☁️ GitHub is ahead. Pulling..."
    git pull --rebase origin $CUR_BRANCH

elif [ "$AHEAD_COUNT" -gt 0 ]; then
    echo "🚀 Your local is ahead. Pushing..."
    git push origin $CUR_BRANCH
fi

############################################
# 3. 分支切換 (main 優先)
############################################
RAW_LIST=$(git branch -r | sed 's/origin\///' | grep -v 'HEAD')
MAIN_EXISTS=$(echo "$RAW_LIST" | grep -w "main")
OTHER_BRANCHES=$(echo "$RAW_LIST" | grep -v -w "main" | sort)

FINAL_LIST=()
[ -n "$MAIN_EXISTS" ] && FINAL_LIST+=("main")
while read -r line; do [ -n "$line" ] && FINAL_LIST+=("$line"); done <<< "$OTHER_BRANCHES"

echo -e "\nRemote branches on GitHub:"
for i in "${!FINAL_LIST[@]}"; do echo "$i) ${FINAL_LIST[$i]}"; done

read -p "Enter index to switch: " NEW_IDX
if [[ -n "$NEW_IDX" && "$NEW_IDX" =~ ^[0-9]+$ ]] && [ "$NEW_IDX" -lt "${#FINAL_LIST[@]}" ]; then
    TARGET_BRANCH=${FINAL_LIST[$NEW_IDX]}
    echo "Switching to '$TARGET_BRANCH'..."
    git checkout $TARGET_BRANCH
    git pull --rebase origin $TARGET_BRANCH 2>/dev/null
    echo "Successfully synced to $TARGET_BRANCH."
fi