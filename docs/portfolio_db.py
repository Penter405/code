#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Portfolio 數據庫模組
管理資料夾和文件的數據庫操作，支持靜態代碼存儲和 JSON 導出
"""

import sqlite3
import json
import os
import shutil
import subprocess
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from pathlib import Path


class PortfolioDB:
    """Portfolio 數據庫管理類"""

    def __init__(self, db_path: str = None):
        if db_path is None:
            db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "portfolio.db")

        self.db_path = db_path
        self.docs_dir = os.path.dirname(os.path.abspath(db_path))
        self.codes_dir = os.path.join(self.docs_dir, "codes")
        self.conn = None
        self._init_database()

    def _connect(self) -> sqlite3.Connection:
        """連接到數據庫"""
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
            self.conn.execute("PRAGMA foreign_keys = ON")
        return self.conn

    def close(self):
        """關閉連接"""
        if self.conn:
            self.conn.close()
            self.conn = None

    def _init_database(self):
        """初始化數據庫架構"""
        conn = self._connect()
        cursor = conn.cursor()

        # 資料夾表 (Web 分類，不等同於 GitHub 路徑)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS folders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                parent_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (parent_id) REFERENCES folders(id) ON DELETE CASCADE
            )
        ''')

        # Existing databases did not have nested folders.
        cursor.execute('PRAGMA table_info(folders)')
        if 'parent_id' not in [column[1] for column in cursor.fetchall()]:
            cursor.execute('ALTER TABLE folders ADD COLUMN parent_id INTEGER')

        # 文件表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT NOT NULL,
                display_name TEXT,
                folder_id INTEGER NOT NULL,
                commit_time TEXT NOT NULL,
                commit_name TEXT NOT NULL,
                github_url TEXT NOT NULL,
                raw_github_url TEXT NOT NULL,
                branch TEXT NOT NULL,
                repo TEXT NOT NULL DEFAULT 'Penter405/code',
                file_path TEXT NOT NULL,
                language TEXT,
                static_path TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (folder_id) REFERENCES folders(id) ON DELETE CASCADE,
                UNIQUE(file_name, folder_id, branch)
            )
        ''')

        self._migrate_file_branch_uniqueness(cursor)

        # 索引
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_folder ON files(folder_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_name ON files(file_name)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_folders_name ON folders(name)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_folders_parent ON folders(parent_id)')

        conn.commit()

    def _migrate_file_branch_uniqueness(self, cursor):
        """Upgrade databases created before branch was part of file identity."""
        cursor.execute('PRAGMA index_list(files)')
        has_old_unique_index = False
        for index in cursor.fetchall():
            # PRAGMA index_list: seq, name, unique, origin, partial
            if not index[2]:
                continue
            cursor.execute(f'PRAGMA index_info("{index[1]}")')
            columns = [item[2] for item in cursor.fetchall()]
            if columns == ['file_name', 'folder_id']:
                has_old_unique_index = True
                break
        if not has_old_unique_index:
            return

        # SQLite cannot alter a UNIQUE constraint in place.  Copy every column
        # so existing saved files and their static paths remain intact.
        cursor.execute('ALTER TABLE files RENAME TO files_old_branch_unique')
        # These index names remain reserved by the renamed table until it is
        # dropped; release them so _init_database can recreate them below.
        cursor.execute('DROP INDEX IF EXISTS idx_files_folder')
        cursor.execute('DROP INDEX IF EXISTS idx_files_name')
        cursor.execute('''
            CREATE TABLE files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT NOT NULL, display_name TEXT, folder_id INTEGER NOT NULL,
                commit_time TEXT NOT NULL, commit_name TEXT NOT NULL,
                github_url TEXT NOT NULL, raw_github_url TEXT NOT NULL,
                branch TEXT NOT NULL, repo TEXT NOT NULL DEFAULT 'Penter405/code',
                file_path TEXT NOT NULL, language TEXT, static_path TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (folder_id) REFERENCES folders(id) ON DELETE CASCADE,
                UNIQUE(file_name, folder_id, branch)
            )
        ''')
        cursor.execute('''
            INSERT INTO files
            (id, file_name, display_name, folder_id, commit_time, commit_name,
             github_url, raw_github_url, branch, repo, file_path, language,
             static_path, created_at, updated_at)
            SELECT id, file_name, display_name, folder_id, commit_time, commit_name,
                   github_url, raw_github_url, branch, repo, file_path, language,
                   static_path, created_at, updated_at
            FROM files_old_branch_unique
        ''')
        cursor.execute('DROP TABLE files_old_branch_unique')

    # =========================================================================
    # 資料夾操作
    # =========================================================================

    def create_folder(self, name: str, parent_id: int = None) -> int:
        """創建資料夾，返回 ID"""
        conn = self._connect()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO folders (name, parent_id) VALUES (?, ?)',
                (name, parent_id)
            )
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            # 已存在，返回現有 ID
            cursor.execute('SELECT id FROM folders WHERE name = ?', (name,))
            row = cursor.fetchone()
            return row['id'] if row else -1

    def rename_folder(self, folder_id: int, new_name: str) -> bool:
        """重命名資料夾"""
        conn = self._connect()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'UPDATE folders SET name = ?, updated_at = ? WHERE id = ?',
                (new_name, datetime.now().isoformat(), folder_id)
            )
            conn.commit()
            return cursor.rowcount > 0
        except sqlite3.IntegrityError:
            return False  # 名稱已存在

    def delete_folder(self, folder_id: int, delete_files: bool = True) -> bool:
        """
        刪除資料夾
        delete_files=True: 同時刪除文件記錄和靜態代碼
        delete_files=False: 僅在資料夾為空時刪除
        """
        conn = self._connect()
        cursor = conn.cursor()

        if not delete_files:
            cursor.execute('SELECT COUNT(*) as cnt FROM files WHERE folder_id = ?', (folder_id,))
            if cursor.fetchone()['cnt'] > 0:
                return False  # 資料夾非空

        # Delete descendants first; old databases may not have the FK cascade.
        for child in self.get_child_folders(folder_id):
            self.delete_folder(child['id'], delete_files=True)

        # 刪除相關靜態代碼文件
        files = self.get_files_in_folder(folder_id)
        for f in files:
            if f.get('static_path'):
                full_path = os.path.join(self.docs_dir, f['static_path'])
                if os.path.exists(full_path):
                    os.remove(full_path)

        # 因為有 ON DELETE CASCADE，刪除資料夾會自動刪除文件記錄
        cursor.execute('DELETE FROM folders WHERE id = ?', (folder_id,))
        conn.commit()
        return cursor.rowcount > 0

    def get_all_folders(self) -> List[Dict]:
        """獲取所有資料夾"""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT f.*, 
                   COUNT(fi.id) as file_count,
                   MAX(fi.updated_at) as last_file_update
            FROM folders f
            LEFT JOIN files fi ON f.id = fi.folder_id
            GROUP BY f.id
            ORDER BY f.created_at DESC
        ''')
        return [dict(row) for row in cursor.fetchall()]

    def get_folder_by_id(self, folder_id: int) -> Optional[Dict]:
        """獲取單個資料夾"""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM folders WHERE id = ?', (folder_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def get_folder_by_name(self, name: str) -> Optional[Dict]:
        """通過名稱獲取資料夾"""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM folders WHERE name = ?', (name,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def get_child_folders(self, parent_id: Optional[int]) -> List[Dict]:
        """Return direct child folders, ordered by name."""
        cursor = self._connect().cursor()
        if parent_id is None:
            cursor.execute('SELECT * FROM folders WHERE parent_id IS NULL ORDER BY name COLLATE NOCASE')
        else:
            cursor.execute('SELECT * FROM folders WHERE parent_id = ? ORDER BY name COLLATE NOCASE', (parent_id,))
        return [dict(row) for row in cursor.fetchall()]

    # =========================================================================
    # 文件操作
    # =========================================================================

    def add_file(self, file_name: str, folder_id: int, commit_time: str,
                 commit_name: str, github_url: str, raw_github_url: str,
                 branch: str, file_path: str, language: str = None,
                 display_name: str = None, repo: str = 'Penter405/code') -> Tuple[int, bool]:
        """
        添加文件記錄
        返回: (file_id, is_new) — is_new=False 表示已存在同名文件
        """
        conn = self._connect()
        cursor = conn.cursor()

        # 檢查重複
        cursor.execute(
            'SELECT id FROM files WHERE file_name = ? AND folder_id = ? AND branch = ?',
            (file_name, folder_id, branch)
        )
        existing = cursor.fetchone()

        if existing:
            return (existing['id'], False)  # 已存在

        # 自動偵測語言
        if language is None:
            language = self._detect_language(file_name)

        # 生成靜態路徑
        static_path = self._generate_static_path(branch, file_path)

        cursor.execute('''
            INSERT INTO files 
            (file_name, display_name, folder_id, commit_time, commit_name,
             github_url, raw_github_url, branch, repo, file_path, language, static_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (file_name, display_name, folder_id, commit_time, commit_name,
              github_url, raw_github_url, branch, repo, file_path, language, static_path))

        # 更新資料夾的 updated_at
        cursor.execute(
            'UPDATE folders SET updated_at = ? WHERE id = ?',
            (datetime.now().isoformat(), folder_id)
        )

        conn.commit()
        return (cursor.lastrowid, True)

    def update_file(self, file_id: int, commit_time: str, commit_name: str,
                    github_url: str, raw_github_url: str, branch: str,
                    file_path: str) -> bool:
        """更新已有文件 (替換舊數據)"""
        conn = self._connect()
        cursor = conn.cursor()

        # 刪除舊靜態文件
        cursor.execute('SELECT static_path, folder_id FROM files WHERE id = ?', (file_id,))
        old = cursor.fetchone()
        if old and old['static_path']:
            full_path = os.path.join(self.docs_dir, old['static_path'])
            if os.path.exists(full_path):
                os.remove(full_path)

        language = self._detect_language(file_path)
        static_path = self._generate_static_path(branch, file_path)

        cursor.execute('''
            UPDATE files SET
                commit_time = ?, commit_name = ?, github_url = ?,
                raw_github_url = ?, branch = ?, file_path = ?,
                language = ?, static_path = ?, updated_at = ?
            WHERE id = ?
        ''', (commit_time, commit_name, github_url, raw_github_url,
              branch, file_path, language, static_path,
              datetime.now().isoformat(), file_id))

        # 更新資料夾的 updated_at
        if old:
            cursor.execute(
                'UPDATE folders SET updated_at = ? WHERE id = ?',
                (datetime.now().isoformat(), old['folder_id'])
            )

        conn.commit()
        return cursor.rowcount > 0

    def delete_file(self, file_id: int) -> bool:
        """刪除文件記錄和靜態代碼"""
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute('SELECT static_path, folder_id FROM files WHERE id = ?', (file_id,))
        row = cursor.fetchone()
        if row and row['static_path']:
            full_path = os.path.join(self.docs_dir, row['static_path'])
            if os.path.exists(full_path):
                os.remove(full_path)

        cursor.execute('DELETE FROM files WHERE id = ?', (file_id,))

        # 更新資料夾的 updated_at
        if row:
            cursor.execute(
                'UPDATE folders SET updated_at = ? WHERE id = ?',
                (datetime.now().isoformat(), row['folder_id'])
            )

        conn.commit()
        return cursor.rowcount > 0

    def move_file(self, file_id: int, new_folder_id: int) -> bool:
        """移動文件到另一個資料夾"""
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute('SELECT folder_id, file_name FROM files WHERE id = ?', (file_id,))
        row = cursor.fetchone()
        if not row:
            return False

        # 檢查目標資料夾是否已有同名文件
        cursor.execute(
            'SELECT id FROM files WHERE file_name = ? AND folder_id = ?',
            (row['file_name'], new_folder_id)
        )
        if cursor.fetchone():
            return False  # 目標資料夾已有同名文件

        now = datetime.now().isoformat()
        old_folder_id = row['folder_id']

        cursor.execute(
            'UPDATE files SET folder_id = ?, updated_at = ? WHERE id = ?',
            (new_folder_id, now, file_id)
        )

        # 更新兩個資料夾的 updated_at
        cursor.execute('UPDATE folders SET updated_at = ? WHERE id = ?', (now, old_folder_id))
        cursor.execute('UPDATE folders SET updated_at = ? WHERE id = ?', (now, new_folder_id))

        conn.commit()
        return cursor.rowcount > 0

    def get_files_in_folder(self, folder_id: int) -> List[Dict]:
        """獲取資料夾中的所有文件"""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM files WHERE folder_id = ?
            ORDER BY updated_at DESC
        ''', (folder_id,))
        return [dict(row) for row in cursor.fetchall()]

    def get_all_files(self) -> List[Dict]:
        """獲取所有文件"""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT f.*, fo.name as folder_name 
            FROM files f
            JOIN folders fo ON f.folder_id = fo.id
            ORDER BY f.updated_at DESC
        ''')
        return [dict(row) for row in cursor.fetchall()]

    def search_files(self, query: str) -> List[Dict]:
        """搜索文件"""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT f.*, fo.name as folder_name
            FROM files f
            JOIN folders fo ON f.folder_id = fo.id
            WHERE f.file_name LIKE ? OR f.display_name LIKE ? OR f.file_path LIKE ?
            ORDER BY f.updated_at DESC
        ''', (f'%{query}%', f'%{query}%', f'%{query}%'))
        return [dict(row) for row in cursor.fetchall()]

    def check_duplicate(self, file_name: str, folder_id: int,
                        branch: str = None) -> Optional[Dict]:
        """Check duplicates within a folder; branch is part of file identity."""
        conn = self._connect()
        cursor = conn.cursor()
        if branch is None:
            cursor.execute('SELECT * FROM files WHERE file_name = ? AND folder_id = ?',
                           (file_name, folder_id))
        else:
            cursor.execute('SELECT * FROM files WHERE file_name = ? AND folder_id = ? AND branch = ?',
                           (file_name, folder_id, branch))
        row = cursor.fetchone()
        return dict(row) if row else None

    # =========================================================================
    # 靜態代碼管理
    # =========================================================================

    def save_static_code(self, file_id: int, code_content: str) -> str:
        """將代碼內容保存為靜態文件"""
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute('SELECT static_path FROM files WHERE id = ?', (file_id,))
        row = cursor.fetchone()
        if not row or not row['static_path']:
            return ""

        static_path = row['static_path']
        full_path = os.path.join(self.docs_dir, static_path)

        # 確保目錄存在
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(code_content)

        return static_path

    def fetch_code_from_branch(self, branch: str, file_path: str,
                               repo_path: str = None) -> Optional[str]:
        """
        使用 git show 從其他分支獲取代碼內容
        repo_path: Git 倉庫根目錄
        """
        if repo_path is None:
            repo_path = os.path.dirname(self.docs_dir)

        try:
            result = subprocess.run(
                f'git show origin/{branch}:{file_path}',
                shell=True, cwd=repo_path,
                capture_output=True, text=True, check=True
            )
            return result.stdout
        except subprocess.CalledProcessError:
            # 嘗試不帶 origin/ 前綴
            try:
                result = subprocess.run(
                    f'git show {branch}:{file_path}',
                    shell=True, cwd=repo_path,
                    capture_output=True, text=True, check=True
                )
                return result.stdout
            except subprocess.CalledProcessError:
                return None

    # =========================================================================
    # JSON 導出
    # =========================================================================

    def export_portfolio_json(self, output_path: str = None) -> str:
        """導出完整的 portfolio 數據為 JSON (給 index.html 用)"""
        if output_path is None:
            output_path = os.path.join(self.docs_dir, "portfolio_data.json")

        folders = self.get_all_folders()

        portfolio = {
            "meta": {
                "repo": "Penter405/code",
                "last_updated": datetime.now().isoformat(),
                "total_folders": len(folders),
                "total_files": 0
            },
            "folders": []
        }

        total_files = 0
        for folder in folders:
            files = self.get_files_in_folder(folder['id'])
            total_files += len(files)

            folder_data = {
                "id": folder['id'],
                "name": folder['name'],
                "parent_id": folder.get('parent_id'),
                "created_at": folder['created_at'],
                "updated_at": folder['updated_at'],
                "file_count": len(files),
                "files": []
            }

            for f in files:
                folder_data["files"].append({
                    "id": f['id'],
                    "file_name": f['file_name'],
                    "display_name": f.get('display_name'),
                    "commit_time": f['commit_time'],
                    "commit_name": f['commit_name'],
                    "github_url": f['github_url'],
                    "raw_github_url": f['raw_github_url'],
                    "branch": f['branch'],
                    "file_path": f['file_path'],
                    "language": f.get('language', ''),
                    "static_path": f.get('static_path', ''),
                    "created_at": f['created_at'],
                    "updated_at": f['updated_at']
                })

            portfolio["folders"].append(folder_data)

        portfolio["meta"]["total_files"] = total_files

        with open(output_path, 'w', encoding='utf-8') as fp:
            json.dump(portfolio, fp, indent=2, ensure_ascii=False, default=str)

        # A normal script tag can load this file even when index.html is opened
        # directly with file://, unlike fetch() which browsers often block for
        # local files.  Include saved branch code for the frontend-only viewer.
        frontend_data = json.loads(json.dumps(portfolio, default=str))
        for folder in frontend_data['folders']:
            for file_data in folder['files']:
                static_path = file_data.get('static_path')
                code_path = os.path.join(self.docs_dir, static_path) if static_path else ''
                try:
                    with open(code_path, encoding='utf-8', errors='replace') as code_file:
                        file_data['static_code'] = code_file.read()
                except OSError:
                    file_data['static_code'] = ''
        script_path = os.path.join(self.docs_dir, 'portfolio_data.js')
        with open(script_path, 'w', encoding='utf-8') as fp:
            fp.write('window.PORTFOLIO_DATA = ')
            json.dump(frontend_data, fp, ensure_ascii=False, default=str)
            fp.write(';\n')

        return output_path

    # =========================================================================
    # 工具方法
    # =========================================================================

    def _detect_language(self, file_name: str) -> str:
        """從文件名偵測語言"""
        ext = os.path.splitext(file_name)[1].lower()
        lang_map = {
            '.py': 'python', '.js': 'javascript', '.ts': 'typescript',
            '.java': 'java', '.cpp': 'cpp', '.c': 'c', '.cs': 'csharp',
            '.go': 'go', '.rs': 'rust', '.rb': 'ruby', '.php': 'php',
            '.swift': 'swift', '.kt': 'kotlin', '.scala': 'scala',
            '.html': 'html', '.css': 'css', '.scss': 'scss',
            '.sql': 'sql', '.sh': 'shell', '.bash': 'bash',
            '.json': 'json', '.yaml': 'yaml', '.yml': 'yaml',
            '.xml': 'xml', '.md': 'markdown', '.txt': 'text',
            '.asm': 'assembly', '.s': 'assembly',
        }
        return lang_map.get(ext, 'other')

    def _generate_static_path(self, branch: str, file_path: str) -> str:
        """Generate an explicit branch-specific copy path relative to ``docs/``.

        A file is copied only when the user confirms an import.  Keeping the
        branch in the path prevents ``feature-x/foo.py`` from replacing the
        saved copy of ``main/foo.py``.
        """
        safe_branch = branch.replace('\\', '/').strip('/').replace('/', '__')
        safe_branch = safe_branch or 'unknown-branch'
        clean_path = file_path.replace('\\', '/').lstrip('/')
        return f"branch/{safe_branch}/{clean_path}"

    @staticmethod
    def generate_github_url(file_path: str, branch: str = "main",
                            repo_owner: str = "Penter405",
                            repo_name: str = "code") -> str:
        """生成 GitHub URL"""
        return f"https://github.com/{repo_owner}/{repo_name}/blob/{branch}/{file_path}"

    @staticmethod
    def generate_raw_github_url(file_path: str, branch: str = "main",
                                repo_owner: str = "Penter405",
                                repo_name: str = "code") -> str:
        """生成 GitHub Raw URL"""
        return f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{file_path}"

    def get_db_info(self) -> Dict:
        """獲取數據庫概覽"""
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(*) FROM folders')
        folder_count = cursor.fetchone()[0]

        cursor.execute('SELECT COUNT(*) FROM files')
        file_count = cursor.fetchone()[0]

        return {
            'db_path': self.db_path,
            'db_size': os.path.getsize(self.db_path) if os.path.exists(self.db_path) else 0,
            'total_folders': folder_count,
            'total_files': file_count,
        }


if __name__ == "__main__":
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    db = PortfolioDB()
    print("Portfolio DB initialized OK")
    print(json.dumps(db.get_db_info(), indent=2, ensure_ascii=False, default=str))
