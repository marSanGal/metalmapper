from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model):
    """User model with password hashing."""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    
    # Relationships
    checkins = db.relationship('Checkin', backref='user', lazy=True, cascade='all, delete-orphan')
    ratings = db.relationship('Rating', backref='user', lazy=True, cascade='all, delete-orphan')
    suggestions = db.relationship('Suggestion', foreign_keys='Suggestion.user_id', backref='user', lazy=True, cascade='all, delete-orphan')
    reviewed_suggestions = db.relationship('Suggestion', foreign_keys='Suggestion.reviewed_by', backref='reviewer', lazy=True)
    
    def set_password(self, password):
        """Hash and set password."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check password against hash."""
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """Convert user to dictionary."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_admin': self.is_admin
        }
    
    def __repr__(self):
        return f'<User {self.username}>'

