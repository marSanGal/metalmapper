from app import db
from datetime import datetime


class Rating(db.Model):
    """Rating model."""
    __tablename__ = 'ratings'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    bar_id = db.Column(db.Integer, db.ForeignKey('bars.id'), nullable=False, index=True)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 scale
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Ensure one rating per user per bar and add check constraint
    __table_args__ = (
        db.UniqueConstraint('user_id', 'bar_id', name='unique_user_bar_rating'),
        db.CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
        db.Index('idx_bar_rating', 'bar_id', 'rating'),  # For aggregating ratings
    )
    
    def to_dict(self):
        """Convert rating to dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'bar_id': self.bar_id,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __repr__(self):
        return f'<Rating {self.rating} - User {self.user_id} for Bar {self.bar_id}>'

