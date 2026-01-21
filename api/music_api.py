from flask import Blueprint, request, jsonify
import os
import json
from auth import require_auth

music_bp = Blueprint('music', __name__)

# Load config
with open('../config/workshop_config.json') as f:
    config = json.load(f)

@music_bp.route('/projects')
@require_auth
def get_projects():
    projects_dir = os.path.join(config['paths']['music_workspace'], 'projects')
    if os.path.exists(projects_dir):
        projects = [d for d in os.listdir(projects_dir) if os.path.isdir(os.path.join(projects_dir, d))]
        return jsonify({'projects': projects})
    return jsonify({'projects': []})

@music_bp.route('/beats')
@require_auth
def get_beats():
    beats_dir = os.path.join(config['paths']['music_workspace'], 'beats')
    if os.path.exists(beats_dir):
        beats = [f for f in os.listdir(beats_dir) if f.endswith('.mp3')]
        return jsonify({'beats': beats})
    return jsonify({'beats': []})

@music_bp.route('/lyrics')
@require_auth
def get_lyrics():
    lyrics_dir = os.path.join(config['paths']['music_workspace'], 'lyrics')
    if os.path.exists(lyrics_dir):
        lyrics = [f for f in os.listdir(lyrics_dir) if f.endswith('.txt')]
        return jsonify({'lyrics': lyrics})
    return jsonify({'lyrics': []})

@music_bp.route('/projects', methods=['POST'])
@require_auth
def create_project():
    data = request.get_json()
    project_name = data.get('name')
    if not project_name:
        return jsonify({'success': False, 'error': 'Project name required'}), 400

    projects_dir = os.path.join(config['paths']['music_workspace'], 'projects')
    project_path = os.path.join(projects_dir, project_name)
    os.makedirs(project_path, exist_ok=True)
    return jsonify({'success': True, 'project': project_name})

@music_bp.route('/upload', methods=['POST'])
@require_auth
def upload_file():
    # Placeholder for file upload - would need to handle multipart/form-data
    return jsonify({'success': False, 'error': 'Not implemented yet'})