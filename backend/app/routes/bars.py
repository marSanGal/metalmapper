from flask import Blueprint, request, jsonify
from app import db
from app.models.bar import Bar

bars_bp = Blueprint('bars', __name__)


@bars_bp.route('', methods=['GET'])
def list_bars():
    """List all bars."""
    # TODO: Implement list bars logic
    return jsonify({'message': 'List bars endpoint - not implemented'}), 501


@bars_bp.route('/<int:bar_id>', methods=['GET'])
def get_bar(bar_id):
    """Get bar details by ID."""
    # TODO: Implement get bar logic
    return jsonify({'message': f'Get bar {bar_id} endpoint - not implemented'}), 501

