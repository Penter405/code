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
from database import Database

app = Flask(__name__)
CORS(app)

# 初始化數據庫
db = Database(os.path.join(os.path.dirname(__file__), "analysis.db"))

@app.route('/api/health', methods=['GET'])
def health_check():
    """健康檢查"""
    return jsonify({
        'status': 'ok',
        'message': 'API 服務正常'
    })

@app.route('/api/analyses', methods=['GET'])
def get_analyses():
    """獲取所有分析記錄"""
    try:
        records = db.get_all_analysis_records()
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
        files = db.get_file_changes(analysis_id)
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
        info = db.get_db_info()
        return jsonify({
            'success': True,
            'data': info
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

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