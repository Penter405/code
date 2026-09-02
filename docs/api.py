#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from flask import Flask, jsonify, request
    from flask_cors import CORS
except ImportError as e:
    print(f"❌ 缺少必要的 Python 包: {e}")
    print("請運行: pip install -r requirements.txt")
    exit(1)

import os
import json
import urllib.request
from database import Database
from portfolio_db import PortfolioDB

app = Flask(__name__)
CORS(app)

# 初始化數據庫
db = Database(os.path.join(os.path.dirname(__file__), "analysis.db"))
portfolio_db = PortfolioDB(os.path.join(os.path.dirname(__file__), "portfolio.db"))


def portfolio_folder_id(analysis_id):
    """Folder cards use a stable API id while retaining the old UI routes."""
    if not analysis_id.startswith('folder-'):
        return None
    try:
        return int(analysis_id.split('-', 1)[1])
    except ValueError:
        return None

@app.route('/api/health', methods=['GET'])
def health_check():
    """健康檢查"""
    return jsonify({
        'status': 'ok',
        'message': 'API 服務正常'
    })

@app.route('/api/analyses', methods=['GET'])
def get_analyses():
    """Return PortfolioDB folders in the card format consumed by index.html."""
    try:
        records = []
        for folder in portfolio_db.get_all_folders():
            files = portfolio_db.get_files_in_folder(folder['id'])
            records.append({
                'analysis_id': f"folder-{folder['id']}",
                'repo_owner': 'Penter405', 'repo_name': 'code',
                'branch': 'multiple branches', 'mode': 'saved files',
                'start_commit': '0000000', 'end_commit': '0000000',
                'total_files': folder.get('file_count', 0),
                'created_at': folder.get('created_at', ''),
                'folder_name': folder['name'], 'parent_id': folder.get('parent_id'),
                'static_files': files,
            })
        return jsonify({
            'success': True,
            'data': records,
            'count': len(records)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analysis/<analysis_id>', methods=['GET'])
def get_analysis(analysis_id):
    """獲取特定分析"""
    try:
        record = db.get_analysis_record(analysis_id)
        if not record:
            return jsonify({
                'success': False,
                'error': '分析記錄不存在'
            }), 404
        
        files = db.get_file_changes(analysis_id)
        commits = db.get_commits(analysis_id)
        statistics = db.get_statistics(analysis_id)
        
        return jsonify({
            'success': True,
            'data': {
                'analysis': record,
                'files': files,
                'commits': commits,
                'statistics': statistics
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analysis/<analysis_id>/files', methods=['GET'])
def get_analysis_files(analysis_id):
    """獲取特定分析的文件變更"""
    try:
        folder_id = portfolio_folder_id(analysis_id)
        if folder_id is None:
            files = db.get_file_changes(analysis_id)
        else:
            files = []
            for file_data in portfolio_db.get_files_in_folder(folder_id):
                files.append({
                    **file_data,
                    'file_location': file_data['file_path'],
                    'added_lines': 0, 'removed_lines': 0, 'total_changes': 0,
                })
        return jsonify({
            'success': True,
            'data': files,
            'count': len(files)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analysis/<analysis_id>/commits', methods=['GET'])
def get_analysis_commits(analysis_id):
    """獲取特定分析的提交"""
    try:
        commits = db.get_commits(analysis_id)
        return jsonify({
            'success': True,
            'data': commits,
            'count': len(commits)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analysis/<analysis_id>/statistics', methods=['GET'])
def get_analysis_statistics(analysis_id):
    """獲取統計信息"""
    try:
        stats = db.get_statistics(analysis_id)
        return jsonify({
            'success': True,
            'data': stats
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/database/info', methods=['GET'])
def get_database_info():
    """獲取數據庫信息"""
    try:
        info = portfolio_db.get_db_info()
        info['total_analyses'] = info['total_folders']
        info['total_commits'] = 0
        return jsonify({
            'success': True,
            'data': info
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/file/content', methods=['GET'])
def get_file_content():
    """獲取文件內容"""
    raw_url = request.args.get('url', '')
    if not raw_url:
        return jsonify({'success': False, 'error': '缺少 URL 參數'}), 400
    try:
        req = urllib.request.Request(raw_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
        return jsonify({'success': True, 'content': content})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/portfolio/file/<int:file_id>/content', methods=['GET'])
def get_saved_branch_file_content(file_id):
    """Read only a branch copy registered in PortfolioDB (never an arbitrary path)."""
    try:
        file_data = next((f for f in portfolio_db.get_all_files() if f['id'] == file_id), None)
        if not file_data or not file_data.get('static_path'):
            return jsonify({'success': False, 'error': 'Saved branch copy not found'}), 404
        docs_dir = os.path.realpath(os.path.dirname(__file__))
        path = os.path.realpath(os.path.join(docs_dir, file_data['static_path']))
        if os.path.commonpath([docs_dir, path]) != docs_dir or not os.path.isfile(path):
            return jsonify({'success': False, 'error': 'Saved branch copy not found'}), 404
        with open(path, encoding='utf-8', errors='replace') as source:
            return jsonify({'success': True, 'content': source.read()})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/search', methods=['GET'])
def search_analyses():
    """搜尋分析記錄"""
    try:
        query = request.args.get('q', '').lower()
        repo_name = request.args.get('repo', '').lower()
        
        records = db.get_all_analysis_records()
        
        filtered = records
        if query:
            filtered = [r for r in filtered if query in r.get('analysis_id', '').lower()]
        if repo_name:
            filtered = [r for r in filtered if repo_name in r.get('repo_name', '').lower()]
        
        return jsonify({
            'success': True,
            'data': filtered,
            'count': len(filtered)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    """404 錯誤處理"""
    return jsonify({
        'success': False,
        'error': '端點未找到'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """500 錯誤處理"""
    return jsonify({
        'success': False,
        'error': '內部服務器錯誤'
    }), 500

if __name__ == '__main__':
    print("🚀 API 服務啟動於 http://localhost:5000")
    print("📖 API 文檔:")
    print("  • GET  /api/health - 健康檢查")
    print("  • GET  /api/analyses - 獲取所有分析")
    print("  • GET  /api/analysis/<id> - 獲取特定分析")
    print("  • GET  /api/analysis/<id>/files - 獲取文件變更")
    print("  • GET  /api/analysis/<id>/commits - 獲取提交信息")
    print("  • GET  /api/analysis/<id>/statistics - 獲取統計")
    print("  • GET  /api/database/info - 獲取數據庫信息")
    print("  • GET  /api/search?q=<query>&repo=<repo> - 搜尋分析")
    app.run(debug=True, port=5000, host='0.0.0.0')
