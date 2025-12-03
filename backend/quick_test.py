"""Quick database connection test."""
from app import create_app, db

app = create_app()

with app.app_context():
    # Test connection
    try:
        db.engine.connect()
        print("✓ Database connection successful!")
        print(f"✓ Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        # Create tables
        db.create_all()
        print("✓ Tables created!")
        
        # Check tables
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"✓ Tables found: {', '.join(tables)}")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        raise

