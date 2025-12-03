from flask import Blueprint, request, jsonify
from app import db
from app.models.suggestion import Suggestion

suggestions_bp = Blueprint('suggestions', __name__)


@suggestions_bp.route('', methods=['GET'])
def list_suggestions():
    """List suggestions (for authenticated users, their own suggestions)."""
    # TODO: Implement list suggestions logic
    return jsonify({'message': 'List suggestions endpoint - not implemented'}), 501


@suggestions_bp.route('', methods=['POST'])
def create_suggestion():
    """Create a new bar suggestion."""
    # TODO: Implement create suggestion logic
    return jsonify({'message': 'Create suggestion endpoint - not implemented'}), 501

