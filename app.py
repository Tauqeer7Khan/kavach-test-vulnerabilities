import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Hardcoded secrets - should be detected
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
if not DATABASE_PASSWORD:
    raise Error('DATABASE_PASSWORD missing')
// KAVACH-FIX: Hardcoded Secret
STRIPE_KEY = os.getenv('STRIPE_KEY')
if not STRIPE_KEY:
    raise Error('STRIPE_KEY missing')
// KAVACH-FIX: Hardcoded Secret

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    # SQL Injection vulnerability
    query = "SELECT * FROM users WHERE id = ?"
cursor = conn.execute(query, (user_id,))
// KAVACH-FIX: SQL Injection
    conn = sqlite3.connect('app.db')
    cursor = conn.execute(query)
    return str(cursor.fetchall())

@app.route('/render')
def render():
    template = request.args.get('template')
    # Command injection vulnerability
    import shlex
os.system(f"cat {shlex.quote(template)}")
// KAVACH-FIX: Command Injection
    return "done"
