from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    """Application factory pattern."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    
    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.bars import bars_bp
    from app.routes.checkins import checkins_bp
    from app.routes.ratings import ratings_bp
    from app.routes.suggestions import suggestions_bp
    from app.routes.admin import admin_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(bars_bp, url_prefix='/api/bars')
    app.register_blueprint(checkins_bp, url_prefix='/api/bars')
    app.register_blueprint(ratings_bp, url_prefix='/api/bars')
    app.register_blueprint(suggestions_bp, url_prefix='/api/suggestions')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app

