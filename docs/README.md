this is a web service that show you how Penter405 solve problem by charpter and time or name and so on(can adjust what you want)

# 📊 Git 提交變更分析工具

## 🎯 功能介紹

這是一個 **Web 服務**，用於分析和展示 Git 提交歷史中的代碼變更。它可以幫助開發者：

- 📈 **追蹤代碼變更** - 按章節、時間、作者等維度分析代碼修改
- 🔍 **統計代碼量** - 計算每個文件的新增、刪除、修改行數
- 💾 **持久化存儲** - 將分析結果保存到 SQLite 數據庫
- 🌐 **REST API 服務** - 提供 HTTP 接口供前端查詢
- 📱 **交互式 Web UI** - 美觀的網頁界面展示分析結果
- 🔎 **智能搜尋** - 支持按文件名、倉庫名等搜尋分析記錄

## 🏗️ 系統架構

```
┌─────────────────────────────────────────────────────────┐
│                      Web 前端                            │
│            (HTML5 + CSS3 + Vanilla JS)                   │
│                   index.html                             │
└────────────┬────────────────────────────────────────────┘
             │ HTTP 請求/響應
┌────────────▼────────────────────────────────────────────┐
│                 Flask REST API                           │
│                   api.py                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │ GET  /api/analyses                               │   │
│  │ GET  /api/analysis/<id>                          │   │
│  │ GET  /api/analysis/<id>/files                    │   │
│  │ GET  /api/analysis/<id>/commits                  │   │
│  │ GET  /api/analysis/<id>/statistics               │   │
│  │ GET  /api/database/info                          │   │
│  │ GET  /api/search                                 │   │
│  └──────────────────────────────────────────────────┘   │
└────────────┬────────────────────────────────────────────┘
             │ 數據查詢
┌────────────▼────────────────────────────────────────────┐
│              SQLite 數據庫層                             │
│                database.py                              │
│  ┌──────────────────────────────────────────────────┐   │
│  │ analysis_records  - 分析會話記錄                 │   │
│  │ file_changes      - 文件變更詳情                 │   │
│  │ commits           - 提交信息                     │   │
│  └──────────────────────────────────────────────────┘   │
│                analysis.db                              │
└────────────┬────────────────────────────────────────────┘
             │
┌────────────▼────────────────────────────────────────────┐
│              Git 數據源                                  │
│         (repository metadata)                            │
└─────────────────────────────────────────────────────────┘
```

## 📚 核心組件說明

### 1️⃣ **run.sh** - 自動化執行器
- 檢查系統環境 (Python, Git)
- 安裝 Python 依賴
- 初始化 SQLite 數據庫
- 執行主分析程序
- 打開 Web UI

### 2️⃣ **main.py** - 主分析程序
```python
# 工作流程:
1. 連接到 Git 倉庫
2. 獲取所有提交記錄
3. 詢問用戶選擇提交範圍
4. 獲取範圍內變更的文件列表
5. 分析每個文件的差異 (新增/刪除行數)
6. 詢問用戶設定文件位置
7. 保存分析結果到數據庫
8. 導出 JSON 數據給前端使用
```

### 3️⃣ **database.py** - 數據庫管理
提供 SQLite 數據庫操作：
- `create_analysis_record()` - 創建分析記錄
- `insert_file_change()` - 保存文件變更
- `insert_commit()` - 保存提交信息
- `get_*()` - 各種查詢方法
- `export_to_json()` - 導出為 JSON

### 4️⃣ **api.py** - REST API 服務
Flask 框架搭建的 HTTP 服務，提供 API 端點供前端調用：

| 方法 | 端點 | 說明 |
|------|------|------|
| GET | `/api/health` | 健康檢查 |
| GET | `/api/analyses` | 獲取所有分析記錄 |
| GET | `/api/analysis/<id>` | 獲取特定分析詳情 |
| GET | `/api/analysis/<id>/files` | 獲取文件變更列表 |
| GET | `/api/analysis/<id>/commits` | 獲取提交信息 |
| GET | `/api/analysis/<id>/statistics` | 獲取統計數據 |
| GET | `/api/database/info` | 獲取數據庫信息 |
| GET | `/api/search` | 搜尋分析記錄 |

### 5️⃣ **index.html** - Web 前端
美觀的單頁應用 (SPA)：
- 📊 分析卡片列表視圖
- 🔍 搜尋和篩選功能
- 📈 統計信息展示
- 💾 詳細信息查看
- 📱 響應式設計

### 6️⃣ **analysis.db** - SQLite 數據庫
持久化存儲分析結果：
```sql
analysis_records   - 分析會話 (id, analysis_id, repo, branch, commits...)
file_changes       - 文件變更 (file_name, added_lines, removed_lines...)
commits            - 提交信息 (hash, author, date, message...)
```

## 🚀 快速開始

### 方式 1: 完整自動化 (推薦)
```bash
cd /workspaces/code/docs
bash run.sh
```

自動執行以下步驟：
1. ✅ 檢查環境
2. ✅ 安裝依賴
3. ✅ 初始化數據庫
4. ✅ 運行分析程序 (交互式)
5. ✅ 打開 Web UI

### 方式 2: 手動步驟

```bash
cd /workspaces/code/docs

# 1. 安裝依賴
pip install -r requirements.txt

# 2. 初始化數據庫
python3 database.py

# 3. 運行分析程序
python3 main.py /workspaces/code

# 4. (可選) 啟動 API 服務
python3 api.py

# 5. 打開 Web UI
# 訪問: file:///workspaces/code/docs/index.html
```

## 🔧 API 使用示例

### 1. 健康檢查
```bash
curl http://localhost:5000/api/health
```

**響應:**
```json
{
  "status": "ok",
  "message": "API 服務正常"
}
```

### 2. 獲取所有分析記錄
```bash
curl http://localhost:5000/api/analyses
```

**響應:**
```json
{
  "success": true,
  "data": [
    {
      "analysis_id": "code_abc1234_def5678_20240901_120000",
      "repo_name": "code",
      "repo_owner": "Penter405",
      "branch": "main",
      "total_files": 5,
      "mode": "new_only",
      "created_at": "2024-09-01 12:00:00"
    }
  ],
  "count": 1
}
```

### 3. 獲取特定分析詳情
```bash
curl http://localhost:5000/api/analysis/code_abc1234_def5678_20240901_120000
```

**響應:**
```json
{
  "success": true,
  "data": {
    "analysis": { ... },
    "files": [
      {
        "file_name": "main.py",
        "file_location": "docs/main.py",
        "added_lines": 150,
        "removed_lines": 20,
        "total_changes": 170,
        "file_type": "Python"
      }
    ],
    "commits": [ ... ],
    "statistics": {
      "total_files": 5,
      "total_added": 500,
      "total_removed": 100,
      "total_changes": 600,
      "total_commits": 10
    }
  }
}
```

### 4. 搜尋分析記錄
```bash
# 搜尋分析 ID
curl "http://localhost:5000/api/search?q=abc1234"

# 搜尋倉庫名
curl "http://localhost:5000/api/search?repo=code"
```

## 💡 使用場景

### 場景 1: 按章節查看代碼進度
```
Chapter 1: 基礎架構搭建
├─ main.py      +250 lines (章節1開始時提交)
├─ database.py  +180 lines
└─ api.py       +120 lines

Chapter 2: 功能完善
├─ main.py      +150 lines (章節2新增)
├─ index.html   +500 lines
└─ ...
```

### 場景 2: 按時間追蹤代碼演進
```
Week 1 (2024-09-01 to 2024-09-07)
├─ 5 個提交
├─ 3 個文件變更
└─ 總計 +800 lines, -50 lines

Week 2 (2024-09-08 to 2024-09-14)
├─ 8 個提交
├─ 6 個文件變更
└─ 總計 +1200 lines, -300 lines
```

### 場景 3: 按開發者查看貢獻
```
Alice (alice@example.com)
├─ 10 次提交
├─ 修改 5 個文件
└─ 貢獻 +500 lines

Bob (bob@example.com)
├─ 8 次提交
├─ 修改 3 個文件
└─ 貢獻 +300 lines
```

## 📋 數據庫架構

### analysis_records 表
記錄每次分析會話的元信息：

| 字段 | 類型 | 說明 |
|------|------|------|
| id | INTEGER | 主鍵 |
| analysis_id | TEXT | 唯一分析 ID |
| repo_name | TEXT | 倉庫名稱 |
| repo_owner | TEXT | 倉庫所有者 |
| branch | TEXT | 分析的分支 |
| start_commit | TEXT | 起始提交 hash |
| end_commit | TEXT | 結束提交 hash |
| mode | TEXT | 分析模式 (new_only/all_changes) |
| total_files | INTEGER | 變更文件數 |
| created_at | TIMESTAMP | 創建時間 |
| updated_at | TIMESTAMP | 更新時間 |

### file_changes 表
記錄每個文件的變更詳情：

| 字段 | 類型 | 說明 |
|------|------|------|
| id | INTEGER | 主鍵 |
| analysis_id | TEXT | 關聯的分析 ID |
| file_name | TEXT | 文件名 |
| file_location | TEXT | 文件位置 |
| added_lines | INTEGER | 新增行數 |
| removed_lines | INTEGER | 刪除行數 |
| total_changes | INTEGER | 總變更行數 |
| file_type | TEXT | 文件類型 (Python/JS/...) |
| created_at | TIMESTAMP | 記錄時間 |

### commits 表
記錄分析範圍內的提交信息：

| 字段 | 類型 | 說明 |
|------|------|------|
| id | INTEGER | 主鍵 |
| analysis_id | TEXT | 關聯的分析 ID |
| commit_hash | TEXT | 提交 hash |
| author | TEXT | 提交作者 |
| email | TEXT | 作者郵箱 |
| commit_date | TIMESTAMP | 提交時間 |
| message | TEXT | 提交信息 |

## 🔍 文件類型支持

系統自動識別以下文件類型：

| 擴展名 | 語言 |
|--------|------|
| .py | Python |
| .js | JavaScript |
| .ts | TypeScript |
| .jsx | React |
| .tsx | React |
| .java | Java |
| .cpp | C++ |
| .go | Go |
| .rb | Ruby |
| .php | PHP |
| .html | HTML |
| .css | CSS |
| .sql | SQL |
| .json | JSON |
| .md | Markdown |
| .sh | Shell |

## ⚙️ 配置和自定義

### 更改分析模式
在 `main.py` 中：
```python
# 模式 1: 只顯示新代碼
mode = "new_only"

# 模式 2: 顯示所有更改
mode = "all_changes"
```

### 更改數據庫位置
在 `database.py` 中：
```python
db = Database("/custom/path/analysis.db")
```

### 更改 API 端口
在 `api.py` 中：
```python
app.run(debug=True, port=8000, host='0.0.0.0')
```

## 🐛 故障排除

### 問題 1: 找不到 Flask 包
**解決方案:**
```bash
pip install -r requirements.txt
# 或
sudo apt-get install python3-flask python3-flask-cors
```

### 問題 2: 數據庫已鎖定
**解決方案:**
```bash
# 確認沒有其他進程在使用數據庫
lsof /workspaces/code/docs/analysis.db

# 重新初始化數據庫
rm /workspaces/code/docs/analysis.db
python3 database.py
```

### 問題 3: API 服務無法啟動
**解決方案:**
```bash
# 檢查端口是否被占用
netstat -tuln | grep 5000

# 終止占用進程
pkill -f "python3 api.py"

# 重新啟動
python3 api.py
```

### 問題 4: 分析程序無法連接 Git
**解決方案:**
```bash
# 確認在 Git 倉庫目錄
cd /workspaces/code

# 檢查 Git 配置
git config --list

# 獲取提交歷史
git log --oneline -5
```

## 📊 性能和限制

| 指標 | 限制 |
|------|------|
| 最大分析記錄 | 無限 (取決於磁盤空間) |
| 單次查詢超時 | 30 秒 |
| 最大文件變更數 | 無限 |
| 數據庫大小 | 無限 (SQLite 最大 140 TB) |
| API 並發連接 | 支持多線程 |

## 🤝 貢獻和反饋

歡迎提出 Issue 和 Pull Request！

## 📝 許可證

此項目採用 MIT 許可證。

## 📞 聯絡方式

- 作者: Penter405
- 倉庫: https://github.com/Penter405/code

---

**最後更新**: 2024-09-01
**版本**: 1.0.0