from flask import Blueprint, request, jsonify
import subprocess
import os
import json
from auth import require_auth

ai_control_bp = Blueprint('ai_control', __name__)

# Load config
with open('../config/workshop_config.json') as f:
    config = json.load(f)

# Load secrets from environment variables
secrets = {
    'api_keys': os.getenv('API_KEYS', {})
}

@ai_control_bp.route('/run_owner', methods=['POST'])
@require_auth
def run_owner_ai():
    try:
        script_path = config['paths']['run_owner_ai']
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, cwd='../../')
        return jsonify({
            'success': True,
            'output': result.stdout,
            'error': result.stderr
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@ai_control_bp.route('/status')
@require_auth
def ai_status():
    # Placeholder for AI status - could check running processes
    return jsonify({'status': 'idle', 'last_run': None})

@ai_control_bp.route('/music/generate_beat', methods=['POST'])
@require_auth
def generate_beat():
    try:
        script_path = os.path.join(config['paths']['music_workspace'], 'generate_beat.py')
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, cwd='../../')
        return jsonify({
            'success': True,
            'output': result.stdout,
            'error': result.stderr
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@ai_control_bp.route('/music/generate_lyrics', methods=['POST'])
@require_auth
def generate_lyrics():
    try:
        script_path = os.path.join(config['paths']['music_workspace'], 'generate_lyrics.py')
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, cwd='../../')
        return jsonify({
            'success': True,
            'output': result.stdout,
            'error': result.stderr
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@ai_control_bp.route('/music/produce_song', methods=['POST'])
@require_auth
def produce_song():
    try:
        script_path = os.path.join(config['paths']['music_workspace'], 'run_music_package.py')
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, cwd='../../')
        return jsonify({
            'success': True,
            'output': result.stdout,
            'error': result.stderr
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500