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
git fetch origin
git reset --hard origin/main
```
## 切換branch on code space
```
#!/bin/bash

echo "Fetching remote branches..."
git fetch --all

# 取得當前 branch
CUR_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $CUR_BRANCH"

# 檢查本地是否有未 commit / untracked 改動
if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git ls-files --others --exclude-standard)" ]; then
    echo "You have local changes that are not committed (including untracked files)."
    read -p "You have not saved your changes on local. Continue and lose your updates on local? (Y/n) " bot
    if [[ "$bot" != "Y" && "$bot" != "y" ]]; then
        echo "Canceling."
        exit 1
    else
        echo "Discarding local changes..."
        git reset --hard
        git clean -fd
    fi
fi

# 檢查本地 commit 與遠端 commit
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/$CUR_BRANCH)

if [ "$LOCAL" != "$REMOTE" ]; then
    echo "Commit not same with remote!"
    read -p "Save local commits to GitHub and then switch? (Y/n) " bot
    if [[ "$bot" == "Y" || "$bot" == "y" ]]; then
        git push origin $CUR_BRANCH
        echo "Local commits pushed to GitHub."
    else
        read -p "Don't save, and switch branch anyway? (Y/n) " bot2
        if [[ "$bot2" != "Y" && "$bot2" != "y" ]]; then
            echo "Canceling."
            exit 1
        fi
    fi
fi

# 列出遠端 branch（main 第一，其餘排序）
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

# 列出遠端 branch
echo "Remote branches on GitHub:"
for i in "${!REMOTE_BRANCHES[@]}"; do
    echo "$i) ${REMOTE_BRANCHES[$i]}"
done

# 互動式選擇要切換的 branch
echo -n "Enter the index of the branch you want to switch to: "
read NEW_IDX
if ! [[ "$NEW_IDX" =~ ^[0-9]+$ ]] || [ "$NEW_IDX" -ge "${#REMOTE_BRANCHES[@]}" ]; then
    echo "Invalid index."
    exit 1
fi
NEW_BRANCH=${REMOTE_BRANCHES[$NEW_IDX]}

# 切換分支，如果本地沒有就建立 tracking branch
if git show-ref --verify --quiet refs/heads/$NEW_BRANCH; then
    git checkout $NEW_BRANCH
else
    git checkout -b $NEW_BRANCH origin/$NEW_BRANCH
fi

# 強制同步雲端版本
git reset --hard origin/$NEW_BRANCH
echo "Switched to branch '$NEW_BRANCH' and synced with GitHub."
```