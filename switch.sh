#!/bin/bash

echo "Fetching remote branches..."
git fetch --all

# 取得當前 branch
CUR_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $CUR_BRANCH"

############################################
# 1. 檢查是否有未儲存變更 (Unstaged/Untracked)
############################################
if [[ -n "$(git status --porcelain)" ]]; then
    echo "⚠️ You have local changes that are not committed."
    read -p "Discard these changes and lose updates? (Y/n) " bot

    if [[ "$bot" == "Y" ]]; then
        echo "Discarding local changes..."
        git reset --hard
        git clean -fd
    else
        read -p "Save and commit these changes first? (Y/n) " bot2
        if [[ "$bot2" == "Y" ]]; then
            echo "1) git add . (exclude deletions)"
            echo "2) git add -A (include deletions)"
            read -p "Choice: " add_choice
            [[ "$add_choice" == "2" ]] && git add -A || git add .
            git commit -m "Auto-save by switch script"
        else
            echo "Canceling script to protect your work."
            exit 1
        fi
    fi
fi

############################################
# 2. 檢查 Commit 不一致 (The Merger)
############################################
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/$CUR_BRANCH)

if [ "$LOCAL" != "$REMOTE" ]; then
    echo "------------------------------------------------"
    echo "🚨 Local and GitHub commits have diverged!"
    echo "------------------------------------------------"
    echo "1) Discard local commits (Use GitHub version)"
    echo "2) Push local commits (Try updating GitHub)"
    echo "3) BACKUP local files & Sync with GitHub (Recommended)"
    echo "4) Cancel"
    read -p "Choose (1-4): " merge_choice

    case $merge_choice in
        1)
            git reset --hard origin/$CUR_BRANCH
            ;;
        2)
            git push origin $CUR_BRANCH
            git reset --hard origin/$CUR_BRANCH
            ;;
        3)
            echo "📦 Isolating local differences..."
            # 找出與遠端不同的檔案清單
            git diff --name-only HEAD origin/$CUR_BRANCH | while IFS= read -r file; do
                if [ -f "$file" ]; then
                    dir=$(dirname "$file")
                    base=$(basename "$file")
                    backup_dir="$dir/local_backup"
                    
                    mkdir -p "$backup_dir"
                    cp "$file" "$backup_dir/$base"
                    echo " -> Backed up: $file"
                fi
            done
            echo "🔄 Syncing workspace with GitHub..."
            git reset --hard origin/$CUR_BRANCH
            echo "✅ Done. Differences are in 'local_backup' folders."
            ;;
        *)
            echo "Exiting."
            exit 1
            ;;
    esac
fi

############################################
# 3. 取得並切換 Branch
############################################
REMOTE_BRANCHES=($(git branch -r | sed 's/origin\///' | grep -v 'HEAD'))
# (Sorting logic to put 'main' first)
MAIN_BRANCH=""
OTHER_BRANCHES=()
for br in "${REMOTE_BRANCHES[@]}"; do
    [[ "$br" == "main" ]] && MAIN_BRANCH="main" || OTHER_BRANCHES+=("$br")
done
IFS=$'\n' OTHER_BRANCHES=($(sort <<<"${OTHER_BRANCHES[*]}")); unset IFS
REMOTE_BRANCHES=($MAIN_BRANCH "${OTHER_BRANCHES[@]}")

echo -e "\nRemote branches:"
for i in "${!REMOTE_BRANCHES[@]}"; do echo "$i) ${REMOTE_BRANCHES[$i]}"; done

read -p "Enter index to switch: " NEW_IDX
NEW_BRANCH=${REMOTE_BRANCHES[$NEW_IDX]}

if git show-ref --verify --quiet refs/heads/$NEW_BRANCH; then
    git checkout $NEW_BRANCH
else
    git checkout -b $NEW_BRANCH origin/$NEW_BRANCH
fi

git reset --hard origin/$NEW_BRANCH
echo "Successfully switched and synced to $NEW_BRANCH."