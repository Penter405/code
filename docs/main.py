#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Portfolio Manager - 主程序
CLI 工作流 + tkinter GUI 管理工具

工作流:
  Step 0: 選擇分支 (從哪個 branch 獲取代碼)
  Step 1: 選擇提交範圍
  Step 2: 選擇分析模式
  Step 3: 選擇章節/資料夾
  Step 4: 設定文件位置
  Step 5: 保存到數據庫 + 靜態代碼
  Step 6: 導出 JSON
  Step 7: 打開 GUI
"""

import subprocess
import json
import os
import sys
import io
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
from typing import List, Dict, Tuple, Optional
from pathlib import Path
from portfolio_db import PortfolioDB

# Fix Windows encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


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


class PortfolioManager:
    """Portfolio 管理器 - CLI 工作流"""

    def __init__(self, repo_path: str = None):
        if repo_path is None:
            repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.repo_path = repo_path
        self.docs_path = os.path.join(repo_path, "docs")

        # 使用新的 portfolio DB
        self.db = PortfolioDB(os.path.join(self.docs_path, "portfolio.db"))

        self.log('info', f"Repo: {self.repo_path}")
        self.log('info', f"Docs: {self.docs_path}")
        self.log('info', f"DB: {self.db.db_path}")

    def log(self, level: str, message: str):
        """統一日誌"""
        levels = {
            'info': f"{Colors.BLUE}[INFO] {message}{Colors.ENDC}",
            'success': f"{Colors.GREEN}[OK] {message}{Colors.ENDC}",
            'warning': f"{Colors.YELLOW}[WARN] {message}{Colors.ENDC}",
            'error': f"{Colors.RED}[ERR] {message}{Colors.ENDC}",
            'section': f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}\n  {message}\n{'='*60}{Colors.ENDC}",
        }
        print(levels.get(level, message))

    def run_git(self, command: str) -> str:
        """執行 Git 命令"""
        try:
            result = subprocess.run(
                command, shell=True, cwd=self.repo_path,
                capture_output=True, text=True, check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            self.log('error', f"Git error: {e.stderr.strip()}")
            return ""

    # =========================================================================
    # Step 0: 選擇分支
    # =========================================================================

    def step_select_branch(self) -> Optional[str]:
        """選擇要分析的分支 (代碼所在分支)"""
        self.log('section', 'Step 0: Select Branch (code source)')

        # 先 fetch
        self.log('info', 'Fetching remote branches...')
        self.run_git('git fetch --all')

        # 獲取分支列表
        output = self.run_git("git branch -a --format='%(refname:short)'")
        if not output:
            self.log('error', 'Cannot list branches')
            return None

        raw = [b.strip().strip("'") for b in output.split('\n') if b.strip()]
        branches = set()
        for b in raw:
            if b.startswith('origin/'):
                b = b[7:]
            if b and b != 'HEAD':
                branches.add(b)

        branches = sorted(list(branches))
        current = self.run_git("git rev-parse --abbrev-ref HEAD")

        print(f"\n{Colors.CYAN}Current branch: {current}{Colors.ENDC}")
        print(f"\nAvailable branches:")
        for i, b in enumerate(branches, 1):
            marker = " *" if b == current else "  "
            print(f"  {marker} {i}. {b}")

        print(f"\n{Colors.GRAY}(Enter to use current: {current}){Colors.ENDC}")
        choice = input(f"{Colors.CYAN}Branch to analyze (number or name): {Colors.ENDC}").strip()

        selected = current
        if choice:
            if choice.isdigit() and 1 <= int(choice) <= len(branches):
                selected = branches[int(choice) - 1]
            elif choice in branches:
                selected = choice
            else:
                self.log('error', f'Invalid branch: {choice}')
                return None

        self.log('success', f'Analyzing branch: {selected}')
        return selected

    # =========================================================================
    # Step 1: 提交範圍
    # =========================================================================

    def step_commit_range(self, branch: str) -> Optional[Tuple[str, str]]:
        """選擇提交範圍"""
        self.log('section', 'Step 1: Select Commit Range')

        # 獲取該分支的提交
        output = self.run_git(
            f'git log origin/{branch} --pretty=format:"%H|%ai|%s" --max-count=50'
        )
        if not output:
            # 嘗試不帶 origin/
            output = self.run_git(
                f'git log {branch} --pretty=format:"%H|%ai|%s" --max-count=50'
            )

        if not output:
            self.log('error', f'No commits found on {branch}')
            return None

        commits = []
        for line in output.split('\n'):
            line = line.strip().strip('"')
            if line:
                parts = line.split('|', 2)
                if len(parts) == 3:
                    commits.append({
                        'hash': parts[0],
                        'date': parts[1],
                        'message': parts[2]
                    })

        if not commits:
            self.log('error', 'No commits parsed')
            return None

        print(f"\n{Colors.YELLOW}Branch '{branch}' has {len(commits)} commits (showing last 50):{Colors.ENDC}")
        print(f"  Oldest: {commits[-1]['hash'][:7]} - {commits[-1]['message']}")
        print(f"  Newest: {commits[0]['hash'][:7]} - {commits[0]['message']}")

        default_start = commits[-1]['hash']
        default_end = commits[0]['hash']

        print(f"\n{Colors.GRAY}(Enter for defaults){Colors.ENDC}")
        start = input(
            f"{Colors.CYAN}Start commit {Colors.GRAY}[default: {default_start[:7]}]{Colors.CYAN}: {Colors.ENDC}"
        ).strip() or default_start

        end = input(
            f"{Colors.CYAN}End commit {Colors.GRAY}[default: {default_end[:7]} (HEAD)]{Colors.CYAN}: {Colors.ENDC}"
        ).strip() or default_end

        self.log('success', f'Range: {start[:7]}...{end[:7]}')
        return (start, end)

    # =========================================================================
    # Step 2: 獲取變更文件
    # =========================================================================

    def step_get_changed_files(self, branch: str, start: str, end: str) -> List[Dict]:
        """獲取變更文件列表"""
        self.log('section', 'Step 2: Scanning Changed Files')

        # Both selected commits are included: compare the parent of start to end.
        # For a root commit, ``start^`` does not exist, so diff-tree is used.
        commits_out = self.run_git(
            f"git log --format='%H|%ai|%s' {start}^..{end}"
        )

        # 如果用的是相同 commit，至少包含 end commit 自身
        if not commits_out and start == end:
            commits_out = self.run_git(
                f"git log --format='%H|%ai|%s' -1 {end}"
            )

        commit_list = []
        if commits_out:
            for line in commits_out.split('\n'):
                line = line.strip().strip("'")
                if line:
                    parts = line.split('|', 2)
                    if len(parts) == 3:
                        commit_list.append({
                            'hash': parts[0],
                            'date': parts[1],
                            'message': parts[2]
                        })

        # 獲取變更的文件列表
        diff_output = self.run_git(f"git diff --name-only {start}^..{end}")
        if not diff_output:
            diff_output = self.run_git(f"git diff-tree --no-commit-id --name-only -r {start}")
        if not diff_output and start != end:
            # 嘗試 log 方式
            diff_output = self.run_git(
                f"git log --name-only --format='' {start}^..{end}"
            )

        if not diff_output:
            self.log('warning', 'No changed files found')
            return []

        # 去重
        files = list(set(f.strip() for f in diff_output.split('\n') if f.strip()))
        
        self.log('success', f'Found {len(files)} changed files')
        for f in files:
            print(f"  {Colors.CYAN}* {f}{Colors.ENDC}")

        # 獲取最後一個提交的信息
        last_commit = commit_list[0] if commit_list else {
            'hash': end[:7], 'date': datetime.now().isoformat(), 'message': 'unknown'
        }

        return [{
            'file_path': f,
            'file_name': os.path.basename(f),
            'commit_hash': last_commit['hash'],
            'commit_time': last_commit['date'],
            'commit_name': last_commit['message'],
        } for f in files]

    # =========================================================================
    # Step 3: 選擇章節/資料夾
    # =========================================================================

    def step_select_folder(self) -> Optional[int]:
        """選擇或創建資料夾"""
        self.log('section', 'Step 3: Select Chapter / Folder')

        folders = self.db.get_all_folders()

        if folders:
            print(f"\n{Colors.YELLOW}Existing folders:{Colors.ENDC}")
            for i, f in enumerate(folders, 1):
                count = f.get('file_count', 0)
                print(f"  {i}. {f['name']} ({count} files)")
            print(f"  {len(folders)+1}. {Colors.GREEN}+ Create new folder{Colors.ENDC}")
        else:
            print(f"\n{Colors.YELLOW}No folders yet. Creating one.{Colors.ENDC}")

        print(f"\n{Colors.GRAY}(Enter a number or type a new folder name){Colors.ENDC}")
        choice = input(f"{Colors.CYAN}Folder: {Colors.ENDC}").strip()

        if not choice:
            self.log('error', 'No folder selected')
            return None

        # 選擇現有的
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(folders):
                folder = folders[idx - 1]
                self.log('success', f'Selected folder: {folder["name"]}')
                return folder['id']
            elif idx == len(folders) + 1:
                # 創建新的
                name = input(f"{Colors.CYAN}New folder name: {Colors.ENDC}").strip()
                if not name:
                    self.log('error', 'Empty name')
                    return None
                fid = self.db.create_folder(name)
                self.log('success', f'Created folder: {name} (id={fid})')
                return fid

        # 直接輸入名稱 → 找或建
        existing = self.db.get_folder_by_name(choice)
        if existing:
            self.log('success', f'Using existing folder: {choice}')
            return existing['id']
        else:
            fid = self.db.create_folder(choice)
            self.log('success', f'Created new folder: {choice} (id={fid})')
            return fid

    # =========================================================================
    # Step 4: 保存到 DB + 靜態代碼
    # =========================================================================

    def step_save_files(self, files: List[Dict], folder_id: int, branch: str):
        """保存文件到數據庫並複製靜態代碼"""
        self.log('section', 'Step 4: Saving Files to DB')

        saved = 0
        skipped = 0
        updated = 0

        for i, f in enumerate(files, 1):
            file_name = f['file_name']
            file_path = f['file_path']

            github_url = PortfolioDB.generate_github_url(file_path, branch)
            raw_github_url = PortfolioDB.generate_raw_github_url(file_path, branch)

            print(f"\n  [{i}/{len(files)}] {Colors.CYAN}{file_path}{Colors.ENDC}")

            # 檢查重複
            dup = self.db.check_duplicate(file_name, folder_id, branch)
            if dup:
                print(f"    {Colors.YELLOW}[DUPLICATE] Already exists in this folder!{Colors.ENDC}")
                print(f"    Existing: branch={dup['branch']}, commit={dup['commit_name'][:40]}")
                choice = input(f"    {Colors.CYAN}Update? (y/n) {Colors.GRAY}[default: n]{Colors.CYAN}: {Colors.ENDC}").strip().lower()
                if choice == 'y':
                    self.db.update_file(
                        dup['id'], f['commit_time'], f['commit_name'],
                        github_url, raw_github_url, branch, file_path
                    )
                    # 保存靜態代碼
                    code = self.db.fetch_code_from_branch(branch, file_path, self.repo_path)
                    if code:
                        self.db.save_static_code(dup['id'], code)
                        print(f"    {Colors.GREEN}Updated + code saved{Colors.ENDC}")
                    else:
                        print(f"    {Colors.GREEN}Updated (code fetch failed){Colors.ENDC}")
                    updated += 1
                else:
                    print(f"    {Colors.GRAY}Skipped{Colors.ENDC}")
                    skipped += 1
                continue

            # 添加新文件
            file_id, is_new = self.db.add_file(
                file_name=file_name,
                folder_id=folder_id,
                commit_time=f['commit_time'],
                commit_name=f['commit_name'],
                github_url=github_url,
                raw_github_url=raw_github_url,
                branch=branch,
                file_path=file_path,
            )

            if is_new:
                # 保存靜態代碼
                code = self.db.fetch_code_from_branch(branch, file_path, self.repo_path)
                if code:
                    self.db.save_static_code(file_id, code)
                    print(f"    {Colors.GREEN}Saved + code copied{Colors.ENDC}")
                else:
                    print(f"    {Colors.YELLOW}Saved (code fetch failed - will use GitHub URL){Colors.ENDC}")
                saved += 1
            else:
                print(f"    {Colors.GRAY}Already exists{Colors.ENDC}")
                skipped += 1

        print(f"\n{Colors.GREEN}Summary: {saved} saved, {updated} updated, {skipped} skipped{Colors.ENDC}")

    # =========================================================================
    # Step 5: 導出 JSON
    # =========================================================================

    def step_export_json(self):
        """導出 portfolio_data.json"""
        self.log('section', 'Step 5: Exporting JSON')
        path = self.db.export_portfolio_json()
        self.log('success', f'Exported: {path}')

    # =========================================================================
    # Main Run
    # =========================================================================

    def run(self):
        """執行 CLI 工作流"""
        try:
            print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}")
            print(f"  Portfolio Manager")
            print(f"{'='*60}{Colors.ENDC}\n")

            print(f"What would you like to do?")
            print(f"  1. Add files from a branch (full workflow)")
            print(f"  2. Open folder management GUI")
            print(f"  3. Export portfolio_data.json only")

            choice = input(f"\n{Colors.CYAN}Choice {Colors.GRAY}[default: 2]{Colors.CYAN}: {Colors.ENDC}").strip() or "2"

            if choice == "1":
                self._run_full_workflow()
            elif choice == "2":
                self.step_export_json()
                self._open_gui()
            elif choice == "3":
                self.step_export_json()
            else:
                self.log('error', 'Invalid choice')

        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Cancelled by user{Colors.ENDC}")
            sys.exit(0)
        except Exception as e:
            self.log('error', f'Error: {str(e)}')
            import traceback
            traceback.print_exc()
            sys.exit(1)

    def _run_full_workflow(self):
        """完整的添加文件工作流"""
        branch = self.step_select_branch()
        if not branch:
            return

        result = self.step_commit_range(branch)
        if not result:
            return
        start, end = result

        files = self.step_get_changed_files(branch, start, end)
        if not files:
            return

        folder_id = self.step_select_folder()
        if not folder_id:
            return

        self.step_save_files(files, folder_id, branch)
        self.step_export_json()

        print(f"\n{Colors.BOLD}{Colors.GREEN}{'='*60}")
        print(f"  Done! Opening GUI...")
        print(f"{'='*60}{Colors.ENDC}\n")

        self._open_gui()

    def _open_gui(self):
        """打開 tkinter GUI"""
        gui = PortfolioGUI(self.db, self)
        gui.run()


# =============================================================================
# tkinter GUI
# =============================================================================

class PortfolioGUI:
    """Portfolio 管理 GUI"""

    def __init__(self, db: PortfolioDB, manager: PortfolioManager = None):
        self.db = db
        self.manager = manager
        self.root = tk.Tk()
        self.root.title("Portfolio Manager")
        self.root.geometry("1400x800")
        self.root.minsize(1050, 650)
        self._configure_style()
        self._build_ui()
        self._refresh_folders()

    def _configure_style(self):
        """配置主題和顏色"""
        self.root.configure(bg='#1e1e2e')

        self.style = ttk.Style()
        self.style.theme_use('clam')

        # 顏色
        self.bg = '#1e1e2e'
        self.bg_secondary = '#313244'
        self.bg_surface = '#45475a'
        self.text = '#cdd6f4'
        self.text_secondary = '#a6adc8'
        self.accent = '#89b4fa'
        self.green = '#a6e3a1'
        self.red = '#f38ba8'
        self.yellow = '#f9e2af'

        # Treeview 樣式
        self.style.configure('Folder.Treeview',
                             background=self.bg_secondary,
                             foreground=self.text,
                             fieldbackground=self.bg_secondary,
                             borderwidth=0,
                             font=('Segoe UI', 10))
        self.style.configure('Folder.Treeview.Heading',
                             background=self.bg_surface,
                             foreground=self.text,
                             font=('Segoe UI', 10, 'bold'))
        self.style.map('Folder.Treeview',
                       background=[('selected', self.accent)],
                       foreground=[('selected', '#1e1e2e')])

        self.style.configure('File.Treeview',
                             background=self.bg_secondary,
                             foreground=self.text,
                             fieldbackground=self.bg_secondary,
                             borderwidth=0,
                             font=('Consolas', 9))
        self.style.configure('File.Treeview.Heading',
                             background=self.bg_surface,
                             foreground=self.text,
                             font=('Segoe UI', 9, 'bold'))
        self.style.map('File.Treeview',
                       background=[('selected', self.accent)],
                       foreground=[('selected', '#1e1e2e')])

        # Button 樣式
        self.style.configure('Action.TButton',
                             background=self.bg_surface,
                             foreground=self.text,
                             font=('Segoe UI', 9),
                             padding=(8, 4))
        self.style.map('Action.TButton',
                       background=[('active', self.accent)])

        self.style.configure('Danger.TButton',
                             background='#45475a',
                             foreground=self.red,
                             font=('Segoe UI', 9),
                             padding=(8, 4))

    def _build_ui(self):
        """構建 UI"""
        # 頂部工具欄
        toolbar = tk.Frame(self.root, bg=self.bg, height=40)
        toolbar.pack(fill=tk.X, padx=8, pady=(8, 0))

        title_lbl = tk.Label(toolbar, text="Portfolio Manager",
                             fg=self.accent, bg=self.bg,
                             font=('Segoe UI', 14, 'bold'))
        title_lbl.pack(side=tk.LEFT, padx=4)

        # 工具欄按鈕 (右側)
        btn_frame = tk.Frame(toolbar, bg=self.bg)
        btn_frame.pack(side=tk.RIGHT)

        ttk.Button(btn_frame, text="Export JSON", style='Action.TButton',
                   command=self._export_json).pack(side=tk.RIGHT, padx=2)
        ttk.Button(btn_frame, text="Refresh", style='Action.TButton',
                   command=self._refresh_all).pack(side=tk.RIGHT, padx=2)
        ttk.Button(btn_frame, text="Add Branch Files", style='Action.TButton',
                   command=self._open_branch_import).pack(side=tk.RIGHT, padx=2)

        # 主面板 (PanedWindow)
        paned = tk.PanedWindow(self.root, orient=tk.HORIZONTAL,
                               bg=self.bg, sashwidth=4, sashrelief=tk.FLAT)
        paned.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        # ====== 左側：資料夾面板 ======
        left_frame = tk.Frame(paned, bg=self.bg_secondary)
        paned.add(left_frame, width=340, minsize=240)

        # 資料夾工具欄
        folder_toolbar = tk.Frame(left_frame, bg=self.bg_secondary)
        folder_toolbar.pack(fill=tk.X, padx=4, pady=4)

        tk.Label(folder_toolbar, text="Folders", fg=self.text,
                 bg=self.bg_secondary, font=('Segoe UI', 11, 'bold')).pack(side=tk.LEFT, padx=4)

        ttk.Button(folder_toolbar, text="+", style='Action.TButton', width=3,
                   command=self._create_folder).pack(side=tk.RIGHT, padx=1)
        ttk.Button(folder_toolbar, text="Ren", style='Action.TButton', width=4,
                   command=self._rename_folder).pack(side=tk.RIGHT, padx=1)
        ttk.Button(folder_toolbar, text="Del", style='Danger.TButton', width=4,
                   command=self._delete_folder).pack(side=tk.RIGHT, padx=1)

        # 資料夾列表
        self.folder_tree = ttk.Treeview(
            left_frame, columns=('files', 'updated'),
            show='tree headings', style='Folder.Treeview'
        )
        self.folder_tree.heading('#0', text='Name')
        self.folder_tree.heading('files', text='Files')
        self.folder_tree.heading('updated', text='Updated')
        self.folder_tree.column('#0', width=150, minwidth=100)
        self.folder_tree.column('files', width=50, minwidth=40, anchor='center')
        self.folder_tree.column('updated', width=90, minwidth=70)
        self.folder_tree.pack(fill=tk.BOTH, expand=True, padx=4, pady=(0, 4))
        self.folder_tree.bind('<<TreeviewSelect>>', self._on_folder_select)

        # ====== 中間：選中資料夾的子資料夾與文件 ======
        right_frame = tk.Frame(paned, bg=self.bg_secondary)
        paned.add(right_frame, minsize=450)

        # 文件工具欄
        file_toolbar = tk.Frame(right_frame, bg=self.bg_secondary)
        file_toolbar.pack(fill=tk.X, padx=4, pady=4)

        self.file_title = tk.Label(file_toolbar, text="Select a folder",
                                   fg=self.text, bg=self.bg_secondary,
                                   font=('Segoe UI', 11, 'bold'))
        self.file_title.pack(side=tk.LEFT, padx=4)

        ttk.Button(file_toolbar, text="Delete File", style='Danger.TButton',
                   command=self._delete_file).pack(side=tk.RIGHT, padx=1)
        ttk.Button(file_toolbar, text="Move File", style='Action.TButton',
                   command=self._move_file).pack(side=tk.RIGHT, padx=1)

        # 文件列表
        self.file_tree = ttk.Treeview(
            right_frame,
            columns=('branch', 'path', 'commit', 'time'),
            show='headings', style='File.Treeview'
        )
        self.file_tree.heading('branch', text='Branch')
        self.file_tree.heading('path', text='File Path')
        self.file_tree.heading('commit', text='Commit')
        self.file_tree.heading('time', text='Time')
        self.file_tree.column('branch', width=150, minwidth=100)
        self.file_tree.column('path', width=460, minwidth=260)
        self.file_tree.column('commit', width=360, minwidth=180)
        self.file_tree.column('time', width=170, minwidth=130)

        # 滾動條
        file_scroll = ttk.Scrollbar(right_frame, orient=tk.VERTICAL,
                                    command=self.file_tree.yview)
        self.file_tree.configure(yscrollcommand=file_scroll.set)

        self.file_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(4, 0), pady=(0, 4))
        file_scroll.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 4), pady=(0, 4))

        # ====== 最右側：未保存的 branch import buffer ======
        buffer_frame = tk.Frame(paned, bg=self.bg_secondary)
        paned.add(buffer_frame, width=390, minsize=280)
        buffer_toolbar = tk.Frame(buffer_frame, bg=self.bg_secondary)
        buffer_toolbar.pack(fill=tk.X, padx=4, pady=4)
        tk.Label(buffer_toolbar, text="Buffer (drag files to the middle)", fg=self.text, bg=self.bg_secondary,
                 font=('Segoe UI', 11, 'bold')).pack(side=tk.LEFT, padx=4)
        ttk.Button(buffer_toolbar, text="Save selected", style='Action.TButton',
                   command=self._save_selected_buffer).pack(side=tk.RIGHT)
        self.buffer_tree = ttk.Treeview(buffer_frame, columns=('branch', 'path'), show='headings', style='File.Treeview')
        self.buffer_tree.heading('branch', text='Branch')
        self.buffer_tree.heading('path', text='Unsaved file')
        self.buffer_tree.column('branch', width=110, minwidth=80)
        self.buffer_tree.column('path', width=260, minwidth=160)
        self.buffer_tree.pack(fill=tk.BOTH, expand=True, padx=4, pady=(0, 4))
        self.buffer_files = {}
        self.buffer_tree.bind('<ButtonPress-1>', self._start_buffer_drag)
        self.buffer_tree.bind('<ButtonRelease-1>', self._drop_buffer_file)

        # 底部狀態欄
        status_bar = tk.Frame(self.root, bg=self.bg_surface, height=24)
        status_bar.pack(fill=tk.X)

        self.status_label = tk.Label(status_bar, text="Ready",
                                     fg=self.text_secondary, bg=self.bg_surface,
                                     font=('Segoe UI', 8), anchor='w')
        self.status_label.pack(fill=tk.X, padx=8, pady=2)

    # =========================================================================
    # 資料夾操作
    # =========================================================================

    def _refresh_folders(self):
        """刷新資料夾列表"""
        self.folder_tree.delete(*self.folder_tree.get_children())
        folders = self.db.get_all_folders()
        by_parent = {}
        for folder in folders:
            by_parent.setdefault(folder.get('parent_id'), []).append(folder)

        def insert_children(parent_id, parent_item=''):
            for f in sorted(by_parent.get(parent_id, []), key=lambda item: item['name'].lower()):
                updated = f.get('last_file_update') or f.get('updated_at') or ''
                if updated:
                    updated = str(updated)[:16]
                item = self.folder_tree.insert(parent_item, tk.END, iid=str(f['id']), text=f['name'],
                                               values=(f.get('file_count', 0), updated), open=True)
                insert_children(f['id'], item)

        insert_children(None)
        self._set_status(f"{len(folders)} folders")

    def _refresh_files(self, folder_id: int):
        """Show direct child folders and files in the middle pane."""
        self.file_tree.delete(*self.file_tree.get_children())
        for child in self.db.get_child_folders(folder_id):
            self.file_tree.insert('', tk.END, iid=f"folder-{child['id']}", values=(
                'folder', f"📁 {child['name']}", '', ''))
        files = self.db.get_files_in_folder(folder_id)
        for f in files:
            updated = f.get('last_file_update') or f.get('updated_at') or ''
            commit_msg = (f['commit_name'] or '')[:50]
            commit_time = str(f.get('commit_time') or '')[:16]
            self.file_tree.insert('', tk.END, iid=str(f['id']), values=(
                f['branch'], f['file_path'], commit_msg, commit_time))
        self._set_status(f"{len(files)} files and {len(self.db.get_child_folders(folder_id))} child folders")

    def _refresh_all(self):
        """刷新全部"""
        self._refresh_folders()
        # 清空文件面板
        self.file_tree.delete(*self.file_tree.get_children())
        self.file_title.config(text="Select a folder")

    def _on_folder_select(self, event):
        """選中資料夾時，顯示其中的文件"""
        sel = self.folder_tree.selection()
        if not sel:
            return
        folder_id = int(sel[0])
        folder = self.db.get_folder_by_id(folder_id)
        if folder:
            self.file_title.config(text=f"{folder['name']}")
            self._refresh_files(folder_id)

    def _create_folder(self):
        """創建新資料夾"""
        name = simpledialog.askstring("Create Folder", "Folder name:",
                                      parent=self.root)
        if name and name.strip():
            selected = self.folder_tree.selection()
            parent_id = int(selected[0]) if selected else None
            fid = self.db.create_folder(name.strip(), parent_id)
            if fid > 0:
                self._refresh_folders()
                self._set_status(f"Created folder: {name.strip()}")
            else:
                messagebox.showwarning("Warning", "Folder already exists!")

    def _rename_folder(self):
        """重命名資料夾"""
        sel = self.folder_tree.selection()
        if not sel:
            messagebox.showinfo("Info", "Select a folder first")
            return

        folder_id = int(sel[0])
        folder = self.db.get_folder_by_id(folder_id)
        if not folder:
            return

        new_name = simpledialog.askstring("Rename Folder",
                                          f"Rename '{folder['name']}' to:",
                                          parent=self.root,
                                          initialvalue=folder['name'])
        if new_name and new_name.strip():
            if self.db.rename_folder(folder_id, new_name.strip()):
                self._refresh_folders()
                self._set_status(f"Renamed to: {new_name.strip()}")
            else:
                messagebox.showwarning("Warning", "Name already exists!")

    def _delete_folder(self):
        """刪除資料夾"""
        sel = self.folder_tree.selection()
        if not sel:
            messagebox.showinfo("Info", "Select a folder first")
            return

        folder_id = int(sel[0])
        folder = self.db.get_folder_by_id(folder_id)
        if not folder:
            return

        files = self.db.get_files_in_folder(folder_id)
        msg = f"Delete folder '{folder['name']}'?"
        if files:
            msg += f"\n\nThis will also delete {len(files)} files and their static code!"

        if messagebox.askyesno("Confirm Delete", msg, icon='warning'):
            self.db.delete_folder(folder_id, delete_files=True)
            self._refresh_all()
            self._set_status(f"Deleted folder: {folder['name']}")

    # =========================================================================
    # 文件操作
    # =========================================================================

    def _delete_file(self):
        """刪除文件"""
        sel = self.file_tree.selection()
        if not sel:
            messagebox.showinfo("Info", "Select a file first")
            return

        if sel[0].startswith('folder-'):
            messagebox.showinfo("Info", "Select a file, not a child folder.")
            return

        file_id = int(sel[0])
        values = self.file_tree.item(sel[0], 'values')
        file_path = values[1] if values else 'unknown'

        if messagebox.askyesno("Confirm Delete",
                               f"Delete '{file_path}'?\nThis removes the DB record and static code."):
            self.db.delete_file(file_id)
            # 刷新當前資料夾
            folder_sel = self.folder_tree.selection()
            if folder_sel:
                self._refresh_files(int(folder_sel[0]))
                self._refresh_folders()
            self._set_status(f"Deleted: {file_path}")

    def _move_file(self):
        """移動文件到另一個資料夾"""
        sel = self.file_tree.selection()
        if not sel:
            messagebox.showinfo("Info", "Select a file first")
            return

        if sel[0].startswith('folder-'):
            messagebox.showinfo("Info", "Select a file, not a child folder.")
            return

        file_id = int(sel[0])

        # 獲取所有資料夾
        folders = self.db.get_all_folders()
        if len(folders) < 2:
            messagebox.showinfo("Info", "Need at least 2 folders to move files.")
            return

        # 簡單的移動對話框
        move_win = tk.Toplevel(self.root)
        move_win.title("Move File")
        move_win.geometry("300x350")
        move_win.configure(bg=self.bg)
        move_win.transient(self.root)
        move_win.grab_set()

        tk.Label(move_win, text="Move to folder:", fg=self.text, bg=self.bg,
                 font=('Segoe UI', 11, 'bold')).pack(pady=(12, 8))

        listbox = tk.Listbox(move_win, bg=self.bg_secondary, fg=self.text,
                             selectbackground=self.accent,
                             selectforeground=self.bg,
                             font=('Segoe UI', 10), borderwidth=0,
                             highlightthickness=0)
        listbox.pack(fill=tk.BOTH, expand=True, padx=12, pady=4)

        folder_ids = []
        current_folder = self.folder_tree.selection()
        for f in folders:
            if current_folder and str(f['id']) == current_folder[0]:
                continue  # 不列出當前資料夾
            listbox.insert(tk.END, f['name'])
            folder_ids.append(f['id'])

        def do_move():
            idx = listbox.curselection()
            if not idx:
                messagebox.showinfo("Info", "Select a target folder")
                return
            target_id = folder_ids[idx[0]]
            if self.db.move_file(file_id, target_id):
                move_win.destroy()
                if current_folder:
                    self._refresh_files(int(current_folder[0]))
                self._refresh_folders()
                self._set_status("File moved successfully")
            else:
                messagebox.showwarning("Error", "Move failed. Duplicate name in target folder?")

        ttk.Button(move_win, text="Move", style='Action.TButton',
                   command=do_move).pack(pady=8)

    # =========================================================================
    # Branch import workflow (the GUI equivalent of the terminal workflow)
    # =========================================================================

    def _open_branch_import(self):
        """Open an explicit, confirm-before-save branch import dialog."""
        if not self.manager:
            messagebox.showerror("Unavailable", "Branch import needs a repository manager.")
            return

        win = tk.Toplevel(self.root)
        win.title("Add Files from a Branch")
        win.geometry("900x650")
        win.minsize(760, 520)
        win.configure(bg=self.bg)
        win.transient(self.root)
        win.grab_set()

        state = {'commits': [], 'files': []}
        form = tk.Frame(win, bg=self.bg)
        form.pack(fill=tk.X, padx=18, pady=16)

        tk.Label(form, text="Branch", fg=self.text, bg=self.bg).grid(row=0, column=0, sticky='w', pady=5)
        branch_var = tk.StringVar()
        branch_box = ttk.Combobox(form, textvariable=branch_var, state='readonly', width=55)
        branch_box.grid(row=0, column=1, sticky='ew', padx=(12, 0), pady=5)
        form.columnconfigure(1, weight=1)

        tk.Label(form, text="Start commit", fg=self.text, bg=self.bg).grid(row=1, column=0, sticky='w', pady=5)
        start_var = tk.StringVar()
        start_entry = tk.Entry(form, textvariable=start_var, bg=self.bg_secondary, fg=self.text,
                               insertbackground=self.text, relief=tk.FLAT)
        start_entry.grid(row=1, column=1, sticky='ew', padx=(12, 0), pady=5)

        tk.Label(form, text="End commit", fg=self.text, bg=self.bg).grid(row=2, column=0, sticky='w', pady=5)
        end_var = tk.StringVar()
        end_entry = tk.Entry(form, textvariable=end_var, bg=self.bg_secondary, fg=self.text,
                             insertbackground=self.text, relief=tk.FLAT)
        end_entry.grid(row=2, column=1, sticky='ew', padx=(12, 0), pady=5)

        hint = tk.Label(form, text="Select a branch. Empty commits will be confirmed before their branch defaults are used.",
                        fg=self.text_secondary, bg=self.bg, anchor='w')
        hint.grid(row=3, column=0, columnspan=2, sticky='ew', pady=(4, 0))

        tk.Label(form, text="Scan adds files to the unsaved buffer. Drag each file to a folder in the middle pane.",
                 fg=self.text_secondary, bg=self.bg, anchor='w').grid(row=4, column=0, columnspan=2, sticky='ew', pady=(14, 5))

        preview = ttk.Treeview(win, columns=('path', 'commit', 'time'), show='headings', style='File.Treeview')
        preview.heading('path', text='Files that will be imported after confirmation')
        preview.heading('commit', text='Latest commit')
        preview.heading('time', text='Commit time')
        preview.column('path', width=460, minwidth=260)
        preview.column('commit', width=270, minwidth=140)
        preview.column('time', width=160, minwidth=110)
        preview.pack(fill=tk.BOTH, expand=True, padx=18, pady=(12, 6))

        button_row = tk.Frame(win, bg=self.bg)
        button_row.pack(fill=tk.X, padx=18, pady=(4, 16))

        def git_output(args):
            result = subprocess.run(args, cwd=self.manager.repo_path, capture_output=True, text=True)
            return result.stdout.strip() if result.returncode == 0 else ''

        def branch_ref(branch):
            """Use a local branch when present, otherwise its tracked origin ref."""
            if git_output(['git', 'rev-parse', '--verify', f'{branch}^{{commit}}']):
                return branch
            return f'origin/{branch}'

        def load_commits(*_):
            branch = branch_var.get()
            output = git_output(['git', 'log', branch_ref(branch), '--pretty=format:%H|%ai|%s', '--max-count=50'])
            state['commits'] = []
            for line in output.splitlines():
                parts = line.split('|', 2)
                if len(parts) == 3:
                    state['commits'].append(parts)
            if state['commits']:
                # Display defaults in gray; do not save or scan until Scan is pressed.
                start_entry.delete(0, tk.END)
                end_entry.delete(0, tk.END)
                start_entry.insert(0, state['commits'][-1][0])
                end_entry.insert(0, state['commits'][0][0])
                hint.config(text=f"{len(state['commits'])} commits loaded. Default: oldest → newest (HEAD).")
            else:
                hint.config(text="No commits found on this branch.")

        def scan():
            branch = branch_var.get()
            if not branch:
                messagebox.showinfo("Branch required", "Choose a branch first.", parent=win)
                return
            if not state['commits']:
                load_commits()
            if not state['commits']:
                messagebox.showerror("No commits", f"No commits found on '{branch}'.", parent=win)
                return

            default_start, default_end = state['commits'][-1][0], state['commits'][0][0]
            start, end = start_var.get().strip(), end_var.get().strip()
            if not start or not end:
                if not messagebox.askyesno("Use defaults?",
                                           "A start or end commit is empty. Use the branch defaults (oldest → newest)?",
                                           parent=win):
                    return
                start, end = start or default_start, end or default_end
                start_var.set(start)
                end_var.set(end)

            if not git_output(['git', 'rev-parse', '--verify', f'{start}^{{commit}}']) or not git_output(['git', 'rev-parse', '--verify', f'{end}^{{commit}}']):
                messagebox.showerror("Invalid commit", "Enter valid commit hashes for this repository.", parent=win)
                return

            state['files'] = self.manager.step_get_changed_files(branch, start, end)
            preview.delete(*preview.get_children())
            for index, file_data in enumerate(state['files']):
                preview.insert('', tk.END, iid=str(index), values=(file_data['file_path'], file_data['commit_name'], file_data['commit_time']))
            hint.config(text=f"Found {len(state['files'])} changed files. Add them to the buffer to choose destinations.")

        def confirm_import():
            if not state['files']:
                messagebox.showinfo("Scan first", "Scan the selected commit range before confirming.", parent=win)
                return
            if not messagebox.askyesno("Confirm import",
                                       f"Add {len(state['files'])} files from '{branch_var.get()}' to the unsaved buffer?",
                                       parent=win):
                return
            self._add_to_buffer(state['files'], branch_var.get())
            win.destroy()

        ttk.Button(button_row, text="Cancel", style='Action.TButton', command=win.destroy).pack(side=tk.RIGHT)
        ttk.Button(button_row, text="Confirm → Buffer", style='Action.TButton', command=confirm_import).pack(side=tk.RIGHT, padx=6)
        ttk.Button(button_row, text="Scan files", style='Action.TButton', command=scan).pack(side=tk.LEFT)

        branches = self._get_local_branches()
        branch_box['values'] = branches
        if branches:
            current = git_output(['git', 'branch', '--show-current'])
            branch_var.set(current if current in branches else branches[0])
            load_commits()
        else:
            hint.config(text="No local or tracked remote branches are available.")
        branch_box.bind('<<ComboboxSelected>>', load_commits)

    def _get_local_branches(self) -> List[str]:
        """List existing refs without fetching or changing repository state."""
        if not self.manager:
            return []
        result = subprocess.run(['git', 'branch', '-a', '--format=%(refname:short)'], cwd=self.manager.repo_path,
                                capture_output=True, text=True)
        branches = set()
        for name in result.stdout.splitlines():
            name = name.strip()
            if name.startswith('origin/'):
                name = name[7:]
            if name and name != 'HEAD':
                branches.add(name)
        return sorted(branches)

    def _show_import_preview(self, files: List[Dict]):
        """Keep the scanned files visible in the enlarged right-most panel."""
        self.file_tree.delete(*self.file_tree.get_children())
        self.file_title.config(text=f"Import preview — {len(files)} files (not saved yet)")
        for index, file_data in enumerate(files):
            self.file_tree.insert('', tk.END, iid=f"preview-{index}", values=(
                '', file_data['file_path'], file_data['commit_name'][:50], file_data['commit_time']))

    def _add_to_buffer(self, files: List[Dict], branch: str):
        """Stage scanned files only; this intentionally does not write files or DB rows."""
        for file_data in files:
            key = f"buffer-{len(self.buffer_files)}"
            self.buffer_files[key] = {**file_data, 'branch': branch}
            self.buffer_tree.insert('', tk.END, iid=key, values=(branch, file_data['file_path']))
        self._set_status(f"{len(files)} files added to buffer; drag them to a destination folder")

    def _start_buffer_drag(self, event):
        self._drag_buffer_item = self.buffer_tree.identify_row(event.y)
        if self._drag_buffer_item:
            # Keep receiving the release event even after the pointer leaves
            # the buffer tree.  This is required for click-hold-drag in Tk.
            self.buffer_tree.grab_set()
            self._set_status("Dragging buffer file — release over a child folder in the middle pane")

    def _drop_buffer_file(self, event):
        item = getattr(self, '_drag_buffer_item', '')
        try:
            if not item or item not in self.buffer_files:
                return
            # Dropping on a child-folder row targets it; otherwise use the
            # selected left folder when the release is anywhere in the middle.
            destination = None
            widget = self.root.winfo_containing(event.x_root, event.y_root)
            in_middle = widget == self.file_tree or str(widget).startswith(str(self.file_tree))
            if in_middle:
                tree_y = event.y_root - self.file_tree.winfo_rooty()
                target = self.file_tree.identify_row(tree_y)
                if target.startswith('folder-'):
                    destination = int(target.split('-', 1)[1])
                else:
                    selected = self.folder_tree.selection()
                    destination = int(selected[0]) if selected else None
            if destination is None:
                self._set_status("Drop in the middle pane after selecting a destination folder on the left")
                return
            self._save_buffer_item(item, destination)
        finally:
            self._drag_buffer_item = ''
            # ``grab_release`` is safe if another widget already released it.
            try:
                self.buffer_tree.grab_release()
            except tk.TclError:
                pass

    def _save_selected_buffer(self):
        selected = self.buffer_tree.selection()
        folders = self.folder_tree.selection()
        if not selected or not folders:
            messagebox.showinfo("Select file and folder", "Select a buffer file and a destination folder on the left.")
            return
        self._save_buffer_item(selected[0], int(folders[0]))

    def _save_buffer_item(self, item: str, folder_id: int):
        file_data = self.buffer_files.get(item)
        if not file_data:
            return
        folder = self.db.get_folder_by_id(folder_id)
        if not folder or not messagebox.askyesno(
                "Save file", f"Save {file_data['file_path']} into '{folder['name']}'?\n\n"
                "This is the point where the database and docs/branch copy are written."):
            return
        saved, updated, skipped = self._save_imported_files([file_data], folder_id, file_data['branch'], self.root)
        if saved or updated:
            self.buffer_tree.delete(item)
            self.buffer_files.pop(item, None)
            self.db.export_portfolio_json()
            self._refresh_folders()
            self.folder_tree.selection_set(str(folder_id))
            self._on_folder_select(None)
        self._set_status(f"Saved {saved}, updated {updated}, skipped {skipped}")

    def _save_imported_files(self, files: List[Dict], folder_id: int, branch: str, parent) -> Tuple[int, int, int]:
        """Save files using the same duplicate/update choices as the terminal flow."""
        saved = updated = skipped = 0
        for file_data in files:
            file_name, file_path = file_data['file_name'], file_data['file_path']
            github_url = PortfolioDB.generate_github_url(file_path, branch)
            raw_url = PortfolioDB.generate_raw_github_url(file_path, branch)
            duplicate = self.db.check_duplicate(file_name, folder_id, branch)
            if duplicate:
                update = messagebox.askyesno(
                    "Duplicate file", f"{file_path} already exists in this folder (from {duplicate['branch']}).\n\nUpdate it?",
                    parent=parent)
                if not update:
                    skipped += 1
                    continue
                self.db.update_file(duplicate['id'], file_data['commit_time'], file_data['commit_name'],
                                    github_url, raw_url, branch, file_path)
                file_id = duplicate['id']
                updated += 1
            else:
                file_id, is_new = self.db.add_file(file_name, folder_id, file_data['commit_time'],
                                                   file_data['commit_name'], github_url, raw_url, branch, file_path)
                if not is_new:
                    skipped += 1
                    continue
                saved += 1
            code = self.db.fetch_code_from_branch(branch, file_path, self.manager.repo_path)
            if code is not None:
                self.db.save_static_code(file_id, code)
        return saved, updated, skipped

    # =========================================================================
    # 工具
    # =========================================================================

    def _export_json(self):
        """導出 JSON"""
        path = self.db.export_portfolio_json()
        self._set_status(f"Exported: {os.path.basename(path)}")
        messagebox.showinfo("Export Complete",
                            f"Exported to:\n{path}")

    def _set_status(self, text: str):
        """設置狀態欄文字"""
        self.status_label.config(text=text)

    def run(self):
        """運行 GUI"""
        self.root.mainloop()
        # One main.py run is enough for the static site: this writes both
        # portfolio_data.json and the file://-friendly portfolio_data.js.
        self.db.export_portfolio_json()


# =============================================================================
# Entry Point
# =============================================================================

if __name__ == "__main__":
    repo_path = sys.argv[1] if len(sys.argv) > 1 else None
    manager = PortfolioManager(repo_path=repo_path)
    manager.run()
