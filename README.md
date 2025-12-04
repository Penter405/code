# code
## a place i set up IDE for programming
## use a code space always
## chatgpt
https://chatgpt.com/share/6928f630-f644-8013-88d1-686021a51411
## 本地完全吃到雲端
```
git fetch origin
git reset --hard origin/main
```
## 切換branch on code space(saved then switch)
```
bash <<'EOF'
echo "Fetching remote branches..."
git fetch --all

# 檢查本地修改
if ! git diff-index --quiet HEAD --; then
    echo "You have unsaved changes!"
    echo -n "Do you want to continue switching and discard them? (Y/n) "
    read CONFIRM
    if [[ "$CONFIRM" != "Y" && "$CONFIRM" != "y" && "$CONFIRM" != "" ]]; then
        echo "Switch cancelled."
        exit 0
    else
        echo "Discarding local changes..."
        git reset --hard
    fi
fi

# 列出所有本地 + 遠端分支
BRANCHES=($(git branch -a | sed 's/remotes\/origin\///' | sed 's/\* //' | sort -u))
echo "Available branches:"
for i in "${!BRANCHES[@]}"; do
    echo "$i) ${BRANCHES[$i]}"
done

# 讀取選擇
echo -n "Enter the index of the branch you want to switch to: "
read IDX

if ! [[ "$IDX" =~ ^[0-9]+$ ]] || [ "$IDX" -ge "${#BRANCHES[@]}" ]; then
    echo "Invalid index."
    exit 1
fi

BR=${BRANCHES[$IDX]}
echo "Switching to branch '$BR'..."

# 檢查分支是否存在於本地，沒有就建立 tracking
if git show-ref --verify --quiet refs/heads/$BR; then
    git checkout $BR
else
    git checkout -b $BR origin/$BR
fi

# 強制同步雲端
git reset --hard origin/$BR
echo "Switched to branch '$BR' and synced with GitHub."
EOF
```
