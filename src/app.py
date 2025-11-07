# -*- coding: utf-8 -*-
import os
import sys

# 添加src目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from flask import Flask
from flask_cors import CORS
from database import init_database
from controller.contact_controller import contact_bp

def create_app():
    """创建Flask应用"""
    app = Flask(__name__)
    
    # 启用CORS，允许前端访问
    CORS(app)
    
    # 初始化数据库
    init_database()
    
    # 注册蓝图（路由）
    app.register_blueprint(contact_bp)
    
    # 根路由，用于测试服务是否正常
    @app.route('/')
    def hello():
        return {
            'message': '通讯录后端服务运行正常！',
            'endpoints': {
                '获取所有联系人': 'GET /contacts',
                '添加联系人': 'POST /contacts',
                '修改联系人': 'PUT /contacts/<id>',
                '删除联系人': 'DELETE /contacts/<id>'
            }
        }
    
    return app

if __name__ == '__main__':
    app = create_app()
    # 运行在5000端口，允许外部访问
    app.run(host='0.0.0.0', port=5000, debug=True)