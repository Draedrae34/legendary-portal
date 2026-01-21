from flask import Flask, request, jsonify, send_from_directory, redirect, session, make_response
from flask_cors import CORS
import json
import os
from datetime import datetime, timedelta
import jwt
import bcrypt
from auth import authenticate_user, require_auth
from ai_control import ai_control_bp
from music_api import music_bp
from business_api import business_bp

app = Flask(__name__, static_folder='../workshop', static_url_path='/workshop')
CORS(app)

# Load config
with open('../config/workshop_config.json') as f:
    config = json.load(f)

with open('../config/workshop_config.json') as f:
    config = json.load(f)

app.secret_key = os.getenv('SECRET_KEY')

# Register blueprints
app.register_blueprint(ai_control_bp, url_prefix='/api/ai')
app.register_blueprint(music_bp, url_prefix='/api/music')
app.register_blueprint(business_bp, url_prefix='/api/business')

@app.route('/workshop/')
def workshop_index():
    if 'user' in session:
        return redirect('/workshop/dashboard.html')
    return send_from_directory('../workshop', 'index.html')

@app.route('/workshop/<path:filename>')
def workshop_files(filename):
    if 'user' not in session and filename != 'index.html':
        return redirect('/workshop/')
    return send_from_directory('../workshop', filename)

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    password = data.get('password', '')

    if authenticate_user(password):
        session['user'] = 'owner'
        session.permanent = True
        app.permanent_session_lifetime = timedelta(hours=config['session']['expiration_hours'])
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'message': 'Invalid password'}), 401

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({'success': True})

@app.route('/api/auth/status')
def auth_status():
    authenticated = 'user' in session
    return jsonify({'authenticated': authenticated})

@app.route('/')
def root():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

if __name__ == '__main__':
    app.run(
        host=config['server']['host'],
        port=config['server']['port'],
        debug=config['server']['debug']
    )