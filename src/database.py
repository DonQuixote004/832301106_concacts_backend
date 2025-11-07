# -*- coding: utf-8 -*-
import sqlite3
import os

# 数据库文件路径
DATABASE_PATH = 'contacts.db'

def get_db_connection():
    """获取数据库连接"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # 让返回结果像字典一样访问
    return conn

def init_database():
    """初始化数据库，创建表"""
    if not os.path.exists(DATABASE_PATH):
        conn = get_db_connection()
        try:
            conn.execute('''
                CREATE TABLE contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            print("数据库表创建成功！")
        except Exception as e:
            print(f"创建表时出错: {e}")
        finally:
            conn.close()

def get_all_contacts():
    """获取所有联系人"""
    conn = get_db_connection()
    try:
        contacts = conn.execute('SELECT * FROM contacts ORDER BY created_at DESC').fetchall()
        # 将Row对象转换为字典列表
        return [dict(contact) for contact in contacts]
    finally:
        conn.close()

def add_contact(name, phone, email=""):
    """添加新联系人"""
    conn = get_db_connection()
    try:
        cursor = conn.execute(
            'INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)',
            (name, phone, email)
        )
        conn.commit()
        return cursor.lastrowid  # 返回新创建的联系人ID
    finally:
        conn.close()

def update_contact(contact_id, name, phone, email=""):
    """更新联系人信息"""
    conn = get_db_connection()
    try:
        conn.execute(
            'UPDATE contacts SET name=?, phone=?, email=? WHERE id=?',
            (name, phone, email, contact_id)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"更新联系人时出错: {e}")
        return False
    finally:
        conn.close()

def delete_contact(contact_id):
    """删除联系人"""
    conn = get_db_connection()
    try:
        conn.execute('DELETE FROM contacts WHERE id=?', (contact_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"删除联系人时出错: {e}")
        return False
    finally:
        conn.close()

def get_contact_by_id(contact_id):
    """根据ID获取单个联系人"""
    conn = get_db_connection()
    try:
        contact = conn.execute('SELECT * FROM contacts WHERE id=?', (contact_id,)).fetchone()
        return dict(contact) if contact else None
    finally:
        conn.close()