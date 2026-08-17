"""
KAVACH Test App - Python Backend
⚠️ INTENTIONALLY VULNERABLE - FOR TESTING ONLY

This file contains 3 known vulnerabilities:
1. SQL Injection (line ~30)
2. Command Injection (line ~45)
3. Weak Cryptography - MD5 (line ~60)
"""

import os
import hashlib
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database connection
def get_db():
    return sqlite3.connect('users.db')


# ============================================================
# VULNERABILITY 1: SQL Injection
# ============================================================
# BAD: User input is concatenated directly into SQL query
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    
    conn = get_db()
    cursor = conn.cursor()
    
    # VULNERABLE: SQL injection via string concatenation
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
// KAVACH-FIX: SQL Injection
    cursor.execute(query)
    
    result = cursor.fetchall()
    conn.close()
    return jsonify(result)


# ============================================================
# VULNERABILITY 2: Command Injection
# ============================================================
# BAD: User input passed directly to shell command
@app.route('/ping')
def ping_host():
    host = request.args.get('host')
    
    # VULNERABLE: command injection via os.system()
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
// KAVACH-FIX: Command Injection
    
    return jsonify({'status': 'pinged', 'exit_code': result})


# ============================================================
# VULNERABILITY 3: Weak Cryptography (MD5)
# ============================================================
# BAD: Using MD5 for password hashing (broken since 2004)
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # VULNERABLE: MD5 is cryptographically broken
    import bcrypt
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
// KAVACH-FIX: Weak Cryptography - MD5
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, hashed)
    )
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'registered', 'username': username})


# ============================================================
# Safe endpoint (should NOT be flagged)
# ============================================================
@app.route('/health')
def health():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
// KAVACH-FIX: Avoid App Run With Bad Host and Debug Enabled
