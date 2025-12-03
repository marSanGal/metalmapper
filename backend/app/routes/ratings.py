from flask import Blueprint, request, jsonify
from app import db
from app.models.rating import Rating

ratings_bp = Blueprint('ratings', __name__)


@ratings_bp.route('/<int:bar_id>/ratings', methods=['GET'])
def list_ratings(bar_id):
    """List ratings for a specific bar."""
    # TODO: Implement list ratings logic
    return jsonify({'message': f'List ratings for bar {bar_id} endpoint - not implemented'}), 501


@ratings_bp.route('/<int:bar_id>/ratings', methods=['POST'])
def create_rating(bar_id):
    """Create or update a rating for a bar."""
    # TODO: Implement create/update rating logic
    return jsonify({'message': f'Create rating for bar {bar_id} endpoint - not implemented'}), 501

