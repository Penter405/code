#!/bin/bash

echo "Fetching remote branches..."
git fetch --all

CUR_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $CUR_BRANCH"

############################################
# 1. 檢查未儲存變更
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
    echo "1) Discard local / 2) Normal Push / 3) BACKUP & AUTO-RESOLVE / 4) Cancel"
    read -p "Choose (1-4): " merge_choice

    case $merge_choice in
        1) git reset --hard origin/$CUR_BRANCH ;;
        2) git push origin $CUR_BRANCH ;;
        3)
            echo "📦 Backing up unique files to 'all_local_backups'..."
            # 建立一個統一的備份資料夾，避免找不到檔案
            BACKUP_ROOT="all_local_backups/$(date +%Y%m%d_%H%M%S)"
            mkdir -p "$BACKUP_ROOT"

            # 找出所有與遠端不同的檔案並備份
            git diff --name-only HEAD origin/$CUR_BRANCH | while read -r file; do
                if [ -f "$file" ]; then
                    dest="$BACKUP_ROOT/$file"
                    mkdir -p "$(dirname "$dest")"
                    cp -f "$file" "$dest"
                    echo " -> Backed up: $file"
                fi
            done
            
            git add .
            git commit -m "Add local backup before rebase"
            
            echo "🔄 Rebase-pulling (Auto-resolving with -X theirs)..."
            # 關鍵：使用 -X theirs 自動選擇 GitHub 版本解決衝突
            if git pull --rebase -X theirs origin $CUR_BRANCH; then
                echo "⬆️ Uploading to GitHub..."
                git push origin $CUR_BRANCH
                echo "✅ Success! Backups are in $BACKUP_ROOT and uploaded."
            else
                echo "❌ Rebase failed. Please run 'git rebase --abort'."
                exit 1
            fi
            ;;
        *) exit 1 ;;
    esac

elif [ "$BEHIND_COUNT" -gt 0 ]; then
    git pull --rebase origin $CUR_BRANCH
elif [ "$AHEAD_COUNT" -gt 0 ]; then
    git push origin $CUR_BRANCH
fi

############################################
# 3. 分支切換 (main 優先排序)
############################################
RAW_LIST=$(git branch -r | sed 's/origin\///' | grep -v 'HEAD')
MAIN_EXISTS=$(echo "$RAW_LIST" | grep -w "main")
OTHER_BRANCHES=$(echo "$RAW_LIST" | grep -v -w "main" | sort)

FINAL_LIST=()
[ -n "$MAIN_EXISTS" ] && FINAL_LIST+=("main")
while read -r line; do [ -n "$line" ] && FINAL_LIST+=("$line"); done <<< "$OTHER_BRANCHES"

echo -e "\nRemote branches:"
for i in "${!FINAL_LIST[@]}"; do echo "$i) ${FINAL_LIST[$i]}"; done

read -p "Enter index to switch: " NEW_IDX
if [[ -n "$NEW_IDX" && "$NEW_IDX" =~ ^[0-9]+$ ]] && [ "$NEW_IDX" -lt "${#FINAL_LIST[@]}" ]; then
    TARGET_BRANCH=${FINAL_LIST[$NEW_IDX]}
    git checkout $TARGET_BRANCH
    git pull --rebase origin $TARGET_BRANCH 2>/dev/null
fi