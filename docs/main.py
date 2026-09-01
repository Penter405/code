#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Tuple
from pathlib import Path
from database import Database

class Colors:
    """終端顏色定義"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[90m'

class CommitAnalyzer:
    def __init__(self, repo_path: str = None):
        if repo_path is None:
            repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        self.repo_path = repo_path
        self.docs_path = os.path.join(repo_path, "docs")
        self.metadata_file = os.path.join(self.docs_path, "file_metadata.json")
        
        # 初始化數據庫
        self.db = Database(os.path.join(self.docs_path, "analysis.db"))
        
        print(f"\n{Colors.CYAN}[DEBUG] 倉庫路徑: {self.repo_path}{Colors.ENDC}")
        print(f"{Colors.CYAN}[DEBUG] Docs 路徑: {self.docs_path}{Colors.ENDC}")
        print(f"{Colors.CYAN}[DEBUG] 數據庫: {self.db.db_path}{Colors.ENDC}\n")
        
        self.load_metadata()
        self.print_header()
    
    def print_header(self):
        """打印標題"""
        print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.BLUE}  📊 Git 提交變更分析工具{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.ENDC}\n")
    
    def log(self, level: str, message: str):
        """統一日誌輸出"""
        levels = {
            'info': f"{Colors.BLUE}ℹ️  {message}{Colors.ENDC}",
            'success': f"{Colors.GREEN}✅ {message}{Colors.ENDC}",
            'warning': f"{Colors.YELLOW}⚠️  {message}{Colors.ENDC}",
            'error': f"{Colors.RED}❌ {message}{Colors.ENDC}",
            'section': f"{Colors.BOLD}{Colors.CYAN}{'='*60}\n{Colors.CYAN}{message}{Colors.ENDC}",
        }
        print(levels.get(level, message))
    
    def run_git_command(self, command: str) -> str:
        """執行 Git 命令"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            self.log('error', f"Git 命令失敗: {e.stderr}")
            return ""
    
    def get_all_commits(self) -> List[Dict]:
        """獲取所有提交信息"""
        self.log('info', "正在獲取提交記錄...")
        output = self.run_git_command(
            "git log --pretty=format:'%H|%an|%ae|%ai|%s'"
        )
        commits = []
        for line in output.split('\n'):
            if line:
                parts = line.split('|')
                if len(parts) == 5:
                    commits.append({
                        'hash': parts[0],
                        'author': parts[1],
                        'email': parts[2],
                        'date': parts[3],
                        'message': parts[4]
                    })
        return commits
    
    def get_commit_range(self, commits: List[Dict]) -> Tuple[str, str]:
        """詢問提交範圍 - 帶灰色默認值"""
        self.log('section', '📋 第一步: 選擇提交範圍')
        
        if not commits:
            self.log('error', "找不到任何提交")
            sys.exit(1)
        
        print(f"\n{Colors.YELLOW}當前分支提交統計:{Colors.ENDC}")
        print(f"  • 總提交數: {len(commits)}")
        print(f"  • 最早提交: {commits[-1]['hash'][:7]} - {commits[-1]['message']}")
        print(f"  • 最新提交: {commits[0]['hash'][:7]} - {commits[0]['message']}")
        
        # 灰色顯示默認值
        default_start = commits[-1]['hash']
        default_end = "HEAD"
        
        print(f"\n{Colors.GRAY}(按 Enter 使用默認值){Colors.ENDC}")
        start_input = input(f"{Colors.CYAN}起始提交雜湊值 {Colors.GRAY}[預設: {default_start[:7]}]{Colors.CYAN}: {Colors.ENDC}").strip()
        end_input = input(f"{Colors.CYAN}結束提交雜湊值 {Colors.GRAY}[預設: {default_end}]{Colors.CYAN}: {Colors.ENDC}").strip()
        
        start = start_input if start_input else default_start
        end = end_input if end_input else default_end
        
        self.log('success', f"已選擇範圍: {start[:7]}...{end}")
        return (start, end)
    
    def get_changed_files(self, start_commit: str, end_commit: str) -> List[str]:
        """
        獲取在指定提交範圍內變更的文件列表
        只返回在這個範圍內 有實際變更 的文件
        """
        self.log('info', f"正在獲取 {start_commit[:7]}...{end_commit} 之間的變更文件...")
        output = self.run_git_command(
            f"git diff --name-only {start_commit}..{end_commit}"
        )
        files = [f for f in output.split('\n') if f]
        return files
    
    def get_file_latest_status(self, file_path: str, end_commit: str) -> Dict:
        """
        獲取文件在 end_commit 時的最新狀態
        返回: 文件是否存在、行數、最後修改提交等信息
        """
        # 檢查文件是否在 end_commit 時存在
        exists = self.run_git_command(
            f"git cat-file -e {end_commit}:{file_path} 2>/dev/null && echo 'exists' || echo 'missing'"
        )
        
        file_exists = exists == 'exists'
        
        # 獲取文件最後修改該文件的提交
        last_commit = self.run_git_command(
            f"git log --follow -1 --format='%H' {end_commit} -- {file_path}"
        )
        
        # 獲取文件在 end_commit 時的行數
        if file_exists:
            line_count = self.run_git_command(
                f"git show {end_commit}:{file_path} | wc -l"
            )
            try:
                line_count = int(line_count)
            except:
                line_count = 0
        else:
            line_count = 0
        
        return {
            'exists': file_exists,
            'line_count': line_count,
            'last_commit': last_commit[:7] if last_commit else 'unknown',
            'full_last_commit': last_commit if last_commit else 'unknown'
        }
    
    def get_user_mode(self) -> str:
        """
        選擇分析模式
        模式 1: 只顯示新代碼 (新增行)
        模式 2: 顯示所有更改 (新增 + 刪除)
        """
        self.log('section', '🎯 第二步: 選擇分析模式')
        
        print(f"\n{Colors.CYAN}1. 只顯示新代碼 (新增行){Colors.ENDC}")
        print(f"   📝 只統計在選擇範圍內 新增 的代碼行數")
        
        print(f"\n{Colors.CYAN}2. 顯示所有更改 (新增 + 刪除){Colors.ENDC}")
        print(f"   📝 統計在選擇範圍內 新增 和 刪除 的代碼行數")
        
        mode = input(f"\n{Colors.CYAN}請選擇 (1 或 2) {Colors.GRAY}[預設: 1]{Colors.CYAN}: {Colors.ENDC}").strip() or "1"
        
        result = "new_only" if mode == "1" else "all_changes"
        mode_text = "僅新代碼" if mode == "1" else "所有更改"
        
        self.log('success', f"已選擇模式: {mode_text}")
        return result
    
    def get_file_diff(self, start_commit: str, end_commit: str, file_path: str, mode: str) -> Dict:
        """
        獲取單個文件的差異
        只計算在 start_commit..end_commit 範圍內的變更
        """
        if mode == "new_only":
            added = self.run_git_command(
                f"git diff {start_commit}..{end_commit} -- {file_path} | grep '^+' | grep -v '^+++' | wc -l"
            )
            return {
                'file': file_path,
                'added_lines': int(added) if added.isdigit() else 0,
                'removed_lines': 0,
                'total_changes': int(added) if added.isdigit() else 0
            }
        else:
            added = self.run_git_command(
                f"git diff {start_commit}..{end_commit} -- {file_path} | grep '^+' | grep -v '^+++' | wc -l"
            )
            removed = self.run_git_command(
                f"git diff {start_commit}..{end_commit} -- {file_path} | grep '^-' | grep -v '^---' | wc -l"
            )
            added_count = int(added) if added.isdigit() else 0
            removed_count = int(removed) if removed.isdigit() else 0
            return {
                'file': file_path,
                'added_lines': added_count,
                'removed_lines': removed_count,
                'total_changes': added_count + removed_count
            }
    
    def get_file_locations(self, files: List[str]) -> Dict[str, str]:
        """詢問文件位置"""
        self.log('section', '📂 第三步: 設定文件位置')
        
        locations = {}
        for i, file in enumerate(files, 1):
            default_location = f"docs/{file}"
            location = input(f"\n{Colors.CYAN}[{i}/{len(files)}] 文件 '{file}' 位置 {Colors.GRAY}[預設: {default_location}]{Colors.CYAN}: {Colors.ENDC}").strip()
            locations[file] = location or default_location
        
        self.log('success', f"已設定 {len(files)} 個文件的位置")
        return locations
    
    def generate_github_url(self, file_path: str, branch: str = "main") -> str:
        """
        生成 GitHub 上的文件 URL
        """
        repo_owner = "Penter405"
        repo_name = "code"
        return f"https://github.com/{repo_owner}/{repo_name}/blob/{branch}/{file_path}"
    
    def generate_raw_github_url(self, file_path: str, branch: str = "main") -> str:
        """
        生成 GitHub 原始文件 URL (用於直接獲取內容)
        """
        repo_owner = "Penter405"
        repo_name = "code"
        return f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{file_path}"
    
    def update_metadata(self, file_info: List[Dict], locations: Dict[str, str], mode: str, branch: str = "main"):
        """更新元數據 - 包含 GitHub URLs"""
        self.log('section', '💾 第四步: 更新元數據')
        
        for info in file_info:
            file_key = info['file']
            self.metadata[file_key] = {
                'file_name': file_key,
                'location': locations.get(file_key, f"docs/{file_key}"),
                'github_url': self.generate_github_url(file_key, branch),
                'raw_github_url': self.generate_raw_github_url(file_key, branch),
                'last_updated': datetime.now().isoformat(),
                'mode': mode,
                'added_lines': info['added_lines'],
                'removed_lines': info['removed_lines'],
                'total_changes': info['total_changes'],
                'repo': 'Penter405/code',
                'branch': branch
            }
        
        self.save_metadata()
        self.log('success', f"已保存 {len(file_info)} 個文件的元數據到 {self.metadata_file}")
        
        # 打印 GitHub URLs
        print(f"\n{Colors.CYAN}GitHub 文件位置:{Colors.ENDC}")
        for file_key in self.metadata:
            url = self.metadata[file_key].get('github_url', '')
            print(f"  • {file_key}: {url}")
    
    def save_to_database(self, start_commit: str, end_commit: str, mode: str,
                        file_info: List[Dict], locations: Dict[str, str], commits: List[Dict]):
        """保存數據到數據庫"""
        self.log('section', '💾 保存數據到數據庫')
        
        # 獲取倉庫信息
        repo_name = "code"
        repo_owner = "Penter405"
        branch = self.run_git_command("git rev-parse --abbrev-ref HEAD")
        
        # 創建分析記錄
        analysis_id = self.db.create_analysis_record(
            repo_name=repo_name,
            repo_owner=repo_owner,
            branch=branch,
            start_commit=start_commit,
            end_commit=end_commit,
            mode=mode,
            total_files=len(file_info)
        )
        
        print(f"\n{Colors.BLUE}分析 ID: {Colors.YELLOW}{analysis_id}{Colors.ENDC}")
        
        # 插入文件變更
        for info in file_info:
            self.db.insert_file_change(
                analysis_id=analysis_id,
                file_name=info['file'],
                file_location=locations[info['file']],
                added_lines=info['added_lines'],
                removed_lines=info['removed_lines'],
                total_changes=info['total_changes']
            )
        
        # 插入提交信息
        for commit in commits:
            self.db.insert_commit(
                analysis_id=analysis_id,
                commit_hash=commit['hash'],
                author=commit['author'],
                email=commit['email'],
                commit_date=commit['date'],
                message=commit['message']
            )
        
        # 導出 JSON 用於 Web 查看
        json_path = self.db.export_to_json(analysis_id, 
            os.path.join(self.docs_path, f"analysis_{analysis_id}.json"))
        
        self.log('success', f"數據已保存到數據庫")
        print(f"  • 分析記錄已創建: {analysis_id}")
        print(f"  • JSON 導出: {json_path}")
    
    def load_metadata(self):
        """載入元數據"""
        if os.path.exists(self.metadata_file):
            with open(self.metadata_file, 'r', encoding='utf-8') as f:
                self.metadata = json.load(f)
        else:
            self.metadata = {}
    
    def save_metadata(self):
        """保存元數據"""
        with open(self.metadata_file, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)
    
    def run(self):
        """執行主程序"""
        try:
            commits = self.get_all_commits()
            if not commits:
                self.log('error', "找不到提交記錄")
                return
            
            start_commit, end_commit = self.get_commit_range(commits)
            
            # 獲取在範圍內變更的文件
            changed_files = self.get_changed_files(start_commit, end_commit)
            
            if not changed_files:
                self.log('warning', "在此範圍內沒有變更的文件")
                return
            
            print(f"\n{Colors.GREEN}找到 {len(changed_files)} 個在選定範圍內變更的文件:{Colors.ENDC}")
            for f in changed_files:
                print(f"  {Colors.CYAN}• {f}{Colors.ENDC}")
            
            # 選擇分析模式
            mode = self.get_user_mode()
            
            print(f"\n{Colors.BLUE}正在分析文件變更...{Colors.ENDC}")
            file_info = []
            for i, file in enumerate(changed_files, 1):
                print(f"  [{i}/{len(changed_files)}] {file}...", end='', flush=True)
                diff_info = self.get_file_diff(start_commit, end_commit, file, mode)
                file_info.append(diff_info)
                print(f" {Colors.GREEN}✓{Colors.ENDC}")
            
            # 獲取文件位置
            locations = self.get_file_locations(changed_files)
            
            # 保存到數據庫
            self.save_to_database(start_commit, end_commit, mode, file_info, locations, commits)
            
            # 獲取分支名
            branch = self.run_git_command("git rev-parse --abbrev-ref HEAD")
            
            # 同時保存 JSON 以兼容舊的 index.html (包含 GitHub URLs)
            self.update_metadata(file_info, locations, mode, branch)
            
            print(f"\n{Colors.BOLD}{Colors.GREEN}{'='*60}")
            print("✨ 流程完成！")
            print(f"{'='*60}{Colors.ENDC}\n")
            
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}程序被用戶中斷{Colors.ENDC}")
            sys.exit(0)
        except Exception as e:
            self.log('error', f"發生錯誤: {str(e)}")
            import traceback
            traceback.print_exc()
            sys.exit(1)

if __name__ == "__main__":
    repo_path = sys.argv[1] if len(sys.argv) > 1 else None
    analyzer = CommitAnalyzer(repo_path=repo_path)
    analyzer.run()