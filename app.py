import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Hardcoded secrets - should be detected
DATABASE_PASSWORD = "admin123456789"
STRIPE_KEY = "sk_live_1234567890abcdefghijklmnopqrstuvwxyz"

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    conn = sqlite3.connect('app.db')
    cursor = conn.execute(query)
    return str(cursor.fetchall())

@app.route('/render')
def render():
    template = request.args.get('template')
    # Command injection vulnerability
    os.system(f"cat {template}")
    return "done"
