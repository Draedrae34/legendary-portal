from flask import Blueprint, request, jsonify
import os
import json
from auth import require_auth

business_bp = Blueprint('business', __name__)

# Load config
with open('../config/workshop_config.json') as f:
    config = json.load(f)

@business_bp.route('/metrics')
@require_auth
def get_metrics():
    # Placeholder metrics - in real implementation, would calculate from data
    return jsonify({
        'revenue': 0,
        'products': 0,
        'orders': 0,
        'trends': []
    })

@business_bp.route('/products')
@require_auth
def get_products():
    products_dir = os.path.join(config['paths']['product_workspace'], 'products')
    products = []
    if os.path.exists(products_dir):
        for root, dirs, files in os.walk(products_dir):
            for file in files:
                if file.endswith('.json'):
                    try:
                        with open(os.path.join(root, file)) as f:
                            product_data = json.load(f)
                            products.append(product_data)
                    except:
                        pass
    return jsonify({'products': products})

@business_bp.route('/orders')
@require_auth
def get_orders():
    # Placeholder - would need order management system
    return jsonify({'orders': []})

@business_bp.route('/products', methods=['POST'])
@require_auth
def add_product():
    data = request.get_json()
    # Placeholder for adding products
    return jsonify({'success': True, 'product': data})