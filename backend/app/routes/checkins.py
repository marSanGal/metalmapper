from flask import Blueprint, request, jsonify
from app import db
from app.models.checkin import Checkin

checkins_bp = Blueprint('checkins', __name__)


@checkins_bp.route('/<int:bar_id>/checkins', methods=['GET'])
def list_checkins(bar_id):
    """List checkins for a specific bar."""
    # TODO: Implement list checkins logic
    return jsonify({'message': f'List checkins for bar {bar_id} endpoint - not implemented'}), 501


@checkins_bp.route('/<int:bar_id>/checkins', methods=['POST'])
def create_checkin(bar_id):
    """Create a new checkin for a bar."""
    # TODO: Implement create checkin logic
    return jsonify({'message': f'Create checkin for bar {bar_id} endpoint - not implemented'}), 501

