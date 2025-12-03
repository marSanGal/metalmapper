from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# Importing config module triggers load_dotenv() in config.py before Config class evaluation
from app import config

db = SQLAlchemy()


def create_app(config_class=None):
    """Application factory pattern."""
    app = Flask(__name__)
    
    # Determine configuration class
    if config_class is None:
        env = os.environ.get('FLASK_ENV', 'development')
        from app.config import config
        config_class = config.get(env, config['default'])
    
    app.config.from_object(config_class)
    
    # Apply SQLAlchemy engine options for connection pooling (PostgreSQL/MySQL)
    # SQLite doesn't use these options
    if 'postgresql' in app.config['SQLALCHEMY_DATABASE_URI'] or 'mysql' in app.config['SQLALCHEMY_DATABASE_URI']:
        if hasattr(config_class, 'SQLALCHEMY_ENGINE_OPTIONS'):
            app.config['SQLALCHEMY_ENGINE_OPTIONS'] = config_class.SQLALCHEMY_ENGINE_OPTIONS
    
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

