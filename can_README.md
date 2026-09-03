# code
## a place i set up IDE for programming
## use a code space always
## chatgpt
https://chatgpt.com/share/6928f630-f644-8013-88d1-686021a51411
## 檔案處理
```
touch 新檔案
mkdir 新資料夾
rm 刪檔案或資料夾
rm -r 超危險的刪除方法
```

## 本地完全吃到雲端
```
#!/bin/bash

echo "Fetching remote branches..."
git fetch --all

# 取得當前 branch
CUR_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $CUR_BRANCH"


############################################
# 檢查是否有未儲存變更（最穩定）
############################################
if [[ -n "$(git status --porcelain)" ]]; then
    echo "You have local changes (modified/staged/untracked)."
    read -p "You have not saved your changes on local. Continue and lose your updates on local? (Y/n) " bot

    if [[ "$bot" == "Y" ]]; then
        echo "Discarding local changes..."
        git reset --hard
        git clean -fd

    else
        # 第二問：是否要幫你儲存？
        read -p "We can help you save your file and continue. Save and continue? (Y/n) " bot2

        if [[ "$bot2" == "Y" ]]; then

            # 第三問：選擇 add . 或 add -A
            echo "Choose how to save your changes:"
            echo "1) git add .    (stage new & modified files; DO NOT stage deletions)"
            echo "2) git add -A   (stage ALL changes including deletions)"
            read -p "Enter 1 or 2: " add_choice

            if [[ "$add_choice" == "1" ]]; then
                echo "Running: git add ."
                git add .
            elif [[ "$add_choice" == "2" ]]; then
                echo "Running: git add -A"
                git add -A
            else
                echo "Invalid choice. Canceling."
                exit 1
            fi

            git commit -m "Auto-save by switch script"
            echo "Saved."

        else
            echo "Canceling."
            exit 1
        fi
    fi
fi


############################################
# 檢查本地 commit 與遠端 commit
############################################
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/$CUR_BRANCH)

if [ "$LOCAL" != "$REMOTE" ]; then
    read -p "Commit not same with remote! Switch and lose your commits? (Y/n) " bot

    if [[ "$bot" == "Y" ]]; then
        git reset --hard origin/$CUR_BRANCH
        echo "Local commits discarded, switched to remote version."

    else
        read -p "Save local commits to GitHub and then switch? (Y/n) " bot2

        if [[ "$bot2" == "Y" ]]; then
            git push origin $CUR_BRANCH
            echo "Local commits pushed to GitHub."
            git reset --hard origin/$CUR_BRANCH
            echo "Switched to remote version."
        else
            echo "Canceling."
            exit 1
        fi
    fi
fi


############################################
# 取得遠端 branches（main 排第一）
############################################
REMOTE_BRANCHES=($(git branch -r | sed 's/origin\///' | grep -v 'HEAD'))

MAIN_BRANCH=""
OTHER_BRANCHES=()
for br in "${REMOTE_BRANCHES[@]}"; do
    if [ "$br" = "main" ]; then
        MAIN_BRANCH="main"
    else
        OTHER_BRANCHES+=("$br")
    fi
done

IFS=$'\n' OTHER_BRANCHES=($(sort <<<"${OTHER_BRANCHES[*]}"))
unset IFS

if [ -n "$MAIN_BRANCH" ]; then
    REMOTE_BRANCHES=("$MAIN_BRANCH" "${OTHER_BRANCHES[@]}")
else
    REMOTE_BRANCHES=("${OTHER_BRANCHES[@]}")
fi


############################################
# 列出遠端 branches
############################################
echo "Remote branches on GitHub:"
for i in "${!REMOTE_BRANCHES[@]}"; do
    echo "$i) ${REMOTE_BRANCHES[$i]}"
done


############################################
# 互動式切換 branch
############################################
echo -n "Enter the index of the branch you want to switch to: "
read NEW_IDX

if ! [[ "$NEW_IDX" =~ ^[0-9]+$ ]] || [ "$NEW_IDX" -ge "${#REMOTE_BRANCHES[@]}" ]; then
    echo "Invalid index."
    exit 1
fi

NEW_BRANCH=${REMOTE_BRANCHES[$NEW_IDX]}

# 已存在本地就 checkout，否则建立 tracking branch
if git show-ref --verify --quiet refs/heads/$NEW_BRANCH; then
    git checkout $NEW_BRANCH
else
    git checkout -b $NEW_BRANCH origin/$NEW_BRANCH
fi

# 強制同步雲端版本
git reset --hard origin/$NEW_BRANCH
echo "Switched to branch '$NEW_BRANCH' and synced with GitHub."
```
