import bcrypt
import json
from flask import session, request, jsonify
from functools import wraps

# Load secrets
# Load secrets from environment variables
secrets = {
    'secret_key': os.getenv('SECRET_KEY'),
    'master_password_hash': os.getenv('MASTER_PASSWORD_HASH'),
    'api_keys': os.getenv('API_KEYS', {})
}

def authenticate_user(password):
    """Verify password against stored hash"""
    stored_hash = secrets['master_password_hash'].encode('utf-8')
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash)

def require_auth(f):
    """Decorator to require authentication for routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function