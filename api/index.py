from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import os
import sqlite3
import json
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Database functions
def init_db():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'detection_stats.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS detections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            camera_id TEXT,
            object_type TEXT,
            confidence REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS motion_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            camera_id TEXT,
            motion_detected BOOLEAN,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

# Routes
@app.route('/')
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/cameras')
@login_required
def cameras():
    return render_template('cameras.html')

@app.route('/zones')
@login_required
def zones():
    return render_template('zones.html')

@app.route('/alerts')
@login_required
def alerts():
    return render_template('alerts.html')

@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

@app.route('/snapshots')
@login_required
def snapshots():
    return render_template('snapshots.html')

@app.route('/stats')
@login_required
def get_stats():
    try:
        camera_id = request.args.get('camera_id', '0')
        db_path = os.path.join(os.path.dirname(__file__), '..', 'detection_stats.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get recent detections
        cursor.execute('''
            SELECT object_type, COUNT(*) as count
            FROM detections
            WHERE camera_id = ? AND timestamp > datetime('now', '-1 hour')
            GROUP BY object_type
        ''', (camera_id,))

        detections = cursor.fetchall()

        # Get motion events
        cursor.execute('''
            SELECT motion_detected, COUNT(*) as count
            FROM motion_events
            WHERE camera_id = ? AND timestamp > datetime('now', '-1 hour')
            GROUP BY motion_detected
        ''', (camera_id,))

        motion_events = cursor.fetchall()

        conn.close()

        return jsonify({
            'success': True,
            'detections': [{'object_type': d[0], 'count': d[1]} for d in detections],
            'motion_events': [{'motion_detected': m[0], 'count': m[1]} for m in motion_events]
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/mobile')
@login_required
def mobile():
    return render_template('mobile.html')

# Vercel serverless function handler
def handler(request):
    with app.test_request_context():
        return app.full_dispatch_request()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
