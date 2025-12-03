"""Test script to verify database connection and setup."""
import sys
from app import create_app, db
from app.models import User, Bar, Checkin, Rating, Suggestion


def test_database_connection():
    """Test database connection and table creation."""
    print("=" * 60)
    print("MetalMapper Database Connection Test")
    print("=" * 60)
    
    try:
        # Create app and get database URI
        app = create_app()
        
        with app.app_context():
            # Test 1: Check database URI
            db_uri = app.config['SQLALCHEMY_DATABASE_URI']
            print(f"\n✓ Database URI: {db_uri}")
            
            # Test 2: Test database connection
            print("\n[1/5] Testing database connection...")
            try:
                db.engine.connect()
                print("✓ Database connection successful!")
            except Exception as e:
                print(f"✗ Database connection failed: {e}")
                return False
            
            # Test 3: Create tables
            print("\n[2/5] Creating database tables...")
            try:
                db.create_all()
                print("✓ Tables created successfully!")
            except Exception as e:
                print(f"✗ Table creation failed: {e}")
                return False
            
            # Test 4: Verify tables exist
            print("\n[3/5] Verifying tables exist...")
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            expected_tables = ['users', 'bars', 'checkins', 'ratings', 'suggestions']
            
            all_tables_exist = True
            for table in expected_tables:
                if table in tables:
                    print(f"  ✓ Table '{table}' exists")
                else:
                    print(f"  ✗ Table '{table}' missing")
                    all_tables_exist = False
            
            if not all_tables_exist:
                print("✗ Some tables are missing!")
                return False
            
            # Test 5: Test basic CRUD operations
            print("\n[4/5] Testing basic database operations...")
            try:
                # Count existing records
                user_count = User.query.count()
                bar_count = Bar.query.count()
                print(f"  ✓ Users in database: {user_count}")
                print(f"  ✓ Bars in database: {bar_count}")
                
                # Test insert (if no bars exist, create a test bar)
                if bar_count == 0:
                    print("\n  Creating test bar...")
                    test_bar = Bar(
                        name='Test Metal Bar',
                        address='123 Test Street',
                        city='London',
                        state='England',
                        zip_code='SW1A 1AA',
                        description='Test bar for connection verification'
                    )
                    db.session.add(test_bar)
                    db.session.commit()
                    print("  ✓ Test bar created successfully!")
                    
                    # Verify it was created
                    created_bar = Bar.query.filter_by(name='Test Metal Bar').first()
                    if created_bar:
                        print(f"  ✓ Verified: Bar ID {created_bar.id} exists")
                        # Clean up test bar
                        db.session.delete(created_bar)
                        db.session.commit()
                        print("  ✓ Test bar cleaned up")
                else:
                    # Just verify we can query
                    first_bar = Bar.query.first()
                    print(f"  ✓ Can query bars: Found '{first_bar.name}'")
                
            except Exception as e:
                print(f"  ✗ Database operations failed: {e}")
                import traceback
                traceback.print_exc()
                return False
            
            # Test 6: Check table schemas
            print("\n[5/5] Verifying table schemas...")
            try:
                users_columns = [col['name'] for col in inspector.get_columns('users')]
                bars_columns = [col['name'] for col in inspector.get_columns('bars')]
                
                expected_user_cols = ['id', 'username', 'email', 'password_hash', 'created_at', 'is_admin']
                expected_bar_cols = ['id', 'name', 'address', 'city', 'state', 'zip_code', 'latitude', 'longitude', 'description', 'created_at', 'updated_at']
                
                user_cols_ok = all(col in users_columns for col in expected_user_cols)
                bar_cols_ok = all(col in bars_columns for col in expected_bar_cols)
                
                if user_cols_ok:
                    print("  ✓ Users table schema is correct")
                else:
                    print(f"  ✗ Users table missing columns. Found: {users_columns}")
                
                if bar_cols_ok:
                    print("  ✓ Bars table schema is correct")
                else:
                    print(f"  ✗ Bars table missing columns. Found: {bars_columns}")
                
                if not (user_cols_ok and bar_cols_ok):
                    return False
                    
            except Exception as e:
                print(f"  ✗ Schema verification failed: {e}")
                return False
            
            print("\n" + "=" * 60)
            print("✓ All database tests passed!")
            print("=" * 60)
            return True
            
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = test_database_connection()
    sys.exit(0 if success else 1)

