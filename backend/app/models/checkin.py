from app import db
from datetime import datetime


class Checkin(db.Model):
    """Checkin model."""
    __tablename__ = 'checkins'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    bar_id = db.Column(db.Integer, db.ForeignKey('bars.id'), nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert checkin to dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'bar_id': self.bar_id,
            'notes': self.notes,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    
    def __repr__(self):
        return f'<Checkin {self.id} - User {self.user_id} at Bar {self.bar_id}>'

