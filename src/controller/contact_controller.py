# -*- coding: utf-8 -*-
import os
import sys

# 添加src目录到Python路径
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, current_dir)

from flask import Blueprint, request, jsonify
from database import get_all_contacts, add_contact, update_contact, delete_contact, get_contact_by_id

# 创建蓝图（用于组织路由）
contact_bp = Blueprint('contacts', __name__)

# 剩下的代码保持不变...

@contact_bp.route('/contacts', methods=['GET'])
def get_contacts():
    """获取所有联系人 - GET /contacts"""
    try:
        contacts = get_all_contacts()
        return jsonify({
            'success': True,
            'data': contacts,
            'count': len(contacts)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'获取联系人失败: {str(e)}'
        }), 500

@contact_bp.route('/contacts', methods=['POST'])
def create_contact():
    """创建新联系人 - POST /contacts"""
    try:
        data = request.get_json()
        
        # 验证必要字段
        if not data or 'name' not in data or 'phone' not in data:
            return jsonify({
                'success': False,
                'message': '姓名和电话是必填字段'
            }), 400
        
        name = data['name']
        phone = data['phone']
        email = data.get('email', '')
        
        # 添加联系人
        contact_id = add_contact(name, phone, email)
        
        return jsonify({
            'success': True,
            'message': '联系人添加成功',
            'data': {'id': contact_id}
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'添加联系人失败: {str(e)}'
        }), 500

@contact_bp.route('/contacts/<int:contact_id>', methods=['PUT'])
def modify_contact(contact_id):
    """修改联系人 - PUT /contacts/1"""
    try:
        data = request.get_json()
        
        # 检查联系人是否存在
        existing_contact = get_contact_by_id(contact_id)
        if not existing_contact:
            return jsonify({
                'success': False,
                'message': '联系人不存在'
            }), 404
        
        # 验证必要字段
        if not data or 'name' not in data or 'phone' not in data:
            return jsonify({
                'success': False,
                'message': '姓名和电话是必填字段'
            }), 400
        
        name = data['name']
        phone = data['phone']
        email = data.get('email', '')
        
        # 更新联系人
        success = update_contact(contact_id, name, phone, email)
        
        if success:
            return jsonify({
                'success': True,
                'message': '联系人更新成功'
            })
        else:
            return jsonify({
                'success': False,
                'message': '更新联系人失败'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'更新联系人失败: {str(e)}'
        }), 500

@contact_bp.route('/contacts/<int:contact_id>', methods=['DELETE'])
def remove_contact(contact_id):
    """删除联系人 - DELETE /contacts/1"""
    try:
        # 检查联系人是否存在
        existing_contact = get_contact_by_id(contact_id)
        if not existing_contact:
            return jsonify({
                'success': False,
                'message': '联系人不存在'
            }), 404
        
        # 删除联系人
        success = delete_contact(contact_id)
        
        if success:
            return jsonify({
                'success': True,
                'message': '联系人删除成功'
            })
        else:
            return jsonify({
                'success': False,
                'message': '删除联系人失败'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'删除联系人失败: {str(e)}'
        }), 500