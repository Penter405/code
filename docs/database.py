#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import json
import os
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path

class Database:
    """SQLite 數據庫管理類"""
    
    def __init__(self, db_path: str = None):
        if db_path is None:
            db_path = os.path.join(os.path.dirname(__file__), "analysis.db")
        
        self.db_path = db_path
        self.conn = None
        self.init_database()
    
    def connect(self):
        """連接到數據庫"""
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
        return self.conn
    
    def close(self):
        """關閉連接"""
        if self.conn:
            self.conn.close()
            self.conn = None
    
    def init_database(self):
        """初始化數據庫架構"""
        conn = self.connect()
        cursor = conn.cursor()
        
        # 創建分析記錄表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analysis_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                analysis_id TEXT UNIQUE NOT NULL,
                repo_name TEXT NOT NULL,
                repo_owner TEXT NOT NULL,
                branch TEXT NOT NULL,
                start_commit TEXT NOT NULL,
                end_commit TEXT NOT NULL,
                mode TEXT NOT NULL,
                total_files INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # 創建文件變更表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS file_changes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                analysis_id TEXT NOT NULL,
                file_name TEXT NOT NULL,
                file_location TEXT NOT NULL,
                added_lines INTEGER NOT NULL,
                removed_lines INTEGER NOT NULL,
                total_changes INTEGER NOT NULL,
                file_type TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (analysis_id) REFERENCES analysis_records(analysis_id),
                UNIQUE(analysis_id, file_name)
            )
        ''')
        
        # 創建提交信息表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS commits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                analysis_id TEXT NOT NULL,
                commit_hash TEXT NOT NULL,
                author TEXT NOT NULL,
                email TEXT NOT NULL,
                commit_date TIMESTAMP NOT NULL,
                message TEXT NOT NULL,
                FOREIGN KEY (analysis_id) REFERENCES analysis_records(analysis_id),
                UNIQUE(analysis_id, commit_hash)
            )
        ''')
        
        # 創建索引以提高查詢性能
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_analysis_id ON file_changes(analysis_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_repo_name ON analysis_records(repo_name)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_created_at ON analysis_records(created_at)')
        
        conn.commit()
    
    def create_analysis_record(self, repo_name: str, repo_owner: str, branch: str,
                              start_commit: str, end_commit: str, mode: str, 
                              total_files: int) -> str:
        """創建分析記錄"""
        analysis_id = f"{repo_name}_{start_commit[:7]}_{end_commit[:7]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        conn = self.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO analysis_records 
                (analysis_id, repo_name, repo_owner, branch, start_commit, end_commit, mode, total_files)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (analysis_id, repo_name, repo_owner, branch, start_commit, end_commit, mode, total_files))
            
            conn.commit()
            return analysis_id
        except sqlite3.IntegrityError:
            return analysis_id
    
    def insert_file_change(self, analysis_id: str, file_name: str, file_location: str,
                          added_lines: int, removed_lines: int, total_changes: int):
        """插入文件變更記錄"""
        conn = self.connect()
        cursor = conn.cursor()
        
        # 獲取文件類型
        file_type = self.get_file_type(file_name)
        
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO file_changes
                (analysis_id, file_name, file_location, added_lines, removed_lines, total_changes, file_type)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (analysis_id, file_name, file_location, added_lines, removed_lines, total_changes, file_type))
            
            conn.commit()
        except sqlite3.Error as e:
            print(f"數據庫錯誤: {e}")
    
    def insert_commit(self, analysis_id: str, commit_hash: str, author: str,
                     email: str, commit_date: str, message: str):
        """插入提交信息"""
        conn = self.connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO commits
                (analysis_id, commit_hash, author, email, commit_date, message)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (analysis_id, commit_hash, author, email, commit_date, message))
            
            conn.commit()
        except sqlite3.Error as e:
            print(f"數據庫錯誤: {e}")
    
    def get_analysis_record(self, analysis_id: str) -> Optional[Dict]:
        """獲取單個分析記錄"""
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM analysis_records WHERE analysis_id = ?', (analysis_id,))
        row = cursor.fetchone()
        
        if row:
            return dict(row)
        return None
    
    def get_all_analysis_records(self) -> List[Dict]:
        """獲取所有分析記錄"""
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM analysis_records 
            ORDER BY created_at DESC 
            LIMIT 100
        ''')
        
        return [dict(row) for row in cursor.fetchall()]
    
    def get_file_changes(self, analysis_id: str) -> List[Dict]:
        """獲取特定分析的文件變更"""
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM file_changes 
            WHERE analysis_id = ? 
            ORDER BY total_changes DESC
        ''', (analysis_id,))
        
        return [dict(row) for row in cursor.fetchall()]
    
    def get_commits(self, analysis_id: str) -> List[Dict]:
        """獲取特定分析的提交信息"""
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM commits 
            WHERE analysis_id = ? 
            ORDER BY commit_date DESC
        ''', (analysis_id,))
        
        return [dict(row) for row in cursor.fetchall()]
    
    def get_statistics(self, analysis_id: str) -> Dict:
        """獲取分析統計信息"""
        conn = self.connect()
        cursor = conn.cursor()
        
        # 文件統計
        cursor.execute('''
            SELECT 
                COUNT(*) as total_files,
                SUM(added_lines) as total_added,
                SUM(removed_lines) as total_removed,
                SUM(total_changes) as total_changes
            FROM file_changes
            WHERE analysis_id = ?
        ''', (analysis_id,))
        
        file_stats = dict(cursor.fetchone())
        
        # 提交統計
        cursor.execute('''
            SELECT COUNT(*) as total_commits
            FROM commits
            WHERE analysis_id = ?
        ''', (analysis_id,))
        
        commit_stats = dict(cursor.fetchone())
        
        return {
            **file_stats,
            **commit_stats
        }
    
    def export_to_json(self, analysis_id: str, output_path: str = None) -> str:
        """導出分析數據為 JSON"""
        if output_path is None:
            output_path = os.path.join(
                os.path.dirname(__file__),
                f"analysis_{analysis_id}.json"
            )
        
        data = {
            'analysis': self.get_analysis_record(analysis_id),
            'files': self.get_file_changes(analysis_id),
            'commits': self.get_commits(analysis_id),
            'statistics': self.get_statistics(analysis_id)
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        
        return output_path
    
    @staticmethod
    def get_file_type(file_name: str) -> str:
        """獲取文件類型"""
        ext = os.path.splitext(file_name)[1].lower()
        
        type_map = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.jsx': 'React',
            '.tsx': 'React',
            '.java': 'Java',
            '.cpp': 'C++',
            '.c': 'C',
            '.go': 'Go',
            '.rs': 'Rust',
            '.rb': 'Ruby',
            '.php': 'PHP',
            '.html': 'HTML',
            '.css': 'CSS',
            '.scss': 'SCSS',
            '.sql': 'SQL',
            '.json': 'JSON',
            '.yaml': 'YAML',
            '.yml': 'YAML',
            '.md': 'Markdown',
            '.txt': 'Text',
            '.sh': 'Shell',
            '.bash': 'Bash'
        }
        
        return type_map.get(ext, 'Other')
    
    def get_db_info(self) -> Dict:
        """獲取數據庫信息"""
        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM analysis_records')
        total_analyses = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM file_changes')
        total_files = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM commits')
        total_commits = cursor.fetchone()[0]
        
        return {
            'db_path': self.db_path,
            'db_size': os.path.getsize(self.db_path) if os.path.exists(self.db_path) else 0,
            'total_analyses': total_analyses,
            'total_files': total_files,
            'total_commits': total_commits
        }

if __name__ == "__main__":
    db = Database()
    print("✅ 數據庫已初始化")
    print(json.dumps(db.get_db_info(), indent=2, ensure_ascii=False, default=str))