#!/bin/bash

set -e

echo "🚀 開始自動化工作流程..."
echo "=================================="

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}[1/7] 檢查 Python 環境...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 未安裝${NC}"
    exit 1
fi
python3 --version
echo -e "${GREEN}✅ Python 環境就緒${NC}\n"

echo -e "${BLUE}[2/7] 檢查 Git 環境...${NC}"
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git 未安裝${NC}"
    exit 1
fi
git --version
cd /workspaces/code
git status
echo -e "${GREEN}✅ Git 環境就緒${NC}\n"

echo -e "${BLUE}[3/7] 檢查必要文件...${NC}"
# 獲取腳本所在目錄
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

echo -e "${YELLOW}腳本位置: $SCRIPT_DIR${NC}"
echo -e "${YELLOW}倉庫位置: $REPO_ROOT${NC}"

# 檢查必要文件
REQUIRED_FILES=(
    "$SCRIPT_DIR/main.py"
    "$SCRIPT_DIR/database.py"
    "$SCRIPT_DIR/api.py"
    "$SCRIPT_DIR/index.html"
    "$SCRIPT_DIR/requirements.txt"
)

MISSING_FILES=()
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}  ✓ $(basename "$file")${NC}"
    else
        echo -e "${RED}  ✗ $(basename "$file") 缺失${NC}"
        MISSING_FILES+=("$file")
    fi
done

if [ ${#MISSING_FILES[@]} -gt 0 ]; then
    echo -e "${RED}❌ 缺少必要文件:${NC}"
    for file in "${MISSING_FILES[@]}"; do
        echo -e "${RED}   - $file${NC}"
    done
    exit 1
fi

echo -e "${GREEN}✅ 文件檢查完成${NC}"
echo -e "   • 腳本位置: $SCRIPT_DIR"
echo -e "   • 倉庫位置: $REPO_ROOT\n"

echo -e "${BLUE}[4/7] 安裝 Python 依賴...${NC}"
if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
    echo -e "${YELLOW}安裝中...${NC}"
    python3 -m pip install -q -r "$SCRIPT_DIR/requirements.txt" 2>/dev/null || {
        echo -e "${YELLOW}⚠️  pip 安裝失敗，嘗試 apt 安裝...${NC}"
        sudo apt-get update -qq 2>/dev/null || true
        sudo apt-get install -y python3-flask python3-flask-cors 2>/dev/null || true
    }
    echo -e "${GREEN}✅ 依賴安裝完成${NC}\n"
else
    echo -e "${YELLOW}⚠️  requirements.txt 不存在${NC}\n"
fi

echo -e "${BLUE}[5/7] 初始化數據庫...${NC}"
cd "$SCRIPT_DIR"
python3 database.py
echo -e "${GREEN}✅ 數據庫初始化完成${NC}\n"

echo -e "${BLUE}[6/7] 執行提交分析程序...${NC}"
python3 main.py "$REPO_ROOT"

# 檢查是否生成了數據庫
if [ -f "$SCRIPT_DIR/analysis.db" ]; then
    echo -e "${GREEN}✅ 數據庫已生成${NC}"
else
    echo -e "${YELLOW}⚠️  analysis.db 可能未正確創建${NC}"
fi
echo -e "${GREEN}✅ 分析完成${NC}\n"

echo -e "${BLUE}[7/7] 打開結果網頁...${NC}"
HTML_PATH="file://$SCRIPT_DIR/index.html"
echo -e "${YELLOW}💡 結果位置: $HTML_PATH${NC}"

# 嘗試用瀏覽器打開
if [ -n "$BROWSER" ]; then
    echo -e "${GREEN}正在打開瀏覽器...${NC}"
    "$BROWSER" "$HTML_PATH" 2>/dev/null &
else
    echo -e "${YELLOW}⚠️  未檢測到 BROWSER 環境變數${NC}"
    echo -e "${YELLOW}   請手動打開: $HTML_PATH${NC}"
fi

echo ""
echo "=================================="
echo -e "${GREEN}✨ 工作流程完成！${NC}"
echo "=================================="
echo -e "${BLUE}📊 結果位置:${NC}"
echo "  • 數據庫: $SCRIPT_DIR/analysis.db"
echo "  • 元數據: $SCRIPT_DIR/file_metadata.json"
echo "  • 網頁: $HTML_PATH"
echo ""
echo -e "${BLUE}🌐 API 服務 (可選):${NC}"
echo "  • 啟動: cd $SCRIPT_DIR && python3 api.py"
echo "  • 訪問: http://localhost:5000/api/health"
echo "  • 所有端點: http://localhost:5000/api/analyses"
echo ""
echo -e "${BLUE}📋 快速命令:${NC}"
echo "  • 查看數據庫信息: sqlite3 $SCRIPT_DIR/analysis.db '.tables'"
echo "  • 查看元數據: cat $SCRIPT_DIR/file_metadata.json | python3 -m json.tool"
echo ""