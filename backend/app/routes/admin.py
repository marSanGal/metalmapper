from flask import Blueprint, request, jsonify
from app import db
from app.models.suggestion import Suggestion

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/suggestions', methods=['GET'])
def list_all_suggestions():
    """List all suggestions (admin only)."""
    # TODO: Implement admin list suggestions logic
    return jsonify({'message': 'Admin list suggestions endpoint - not implemented'}), 501


@admin_bp.route('/suggestions/<int:suggestion_id>/approve', methods=['POST'])
def approve_suggestion(suggestion_id):
    """Approve a suggestion (admin only)."""
    # TODO: Implement approve suggestion logic
    return jsonify({'message': f'Approve suggestion {suggestion_id} endpoint - not implemented'}), 501


@admin_bp.route('/suggestions/<int:suggestion_id>/reject', methods=['POST'])
def reject_suggestion(suggestion_id):
    """Reject a suggestion (admin only)."""
    # TODO: Implement reject suggestion logic
    return jsonify({'message': f'Reject suggestion {suggestion_id} endpoint - not implemented'}), 501

