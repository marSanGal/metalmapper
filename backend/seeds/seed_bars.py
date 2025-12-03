"""Seed script for populating bars."""
from app import create_app, db
from app.models.bar import Bar


def seed_bars():
    """Seed database with sample bars."""
    app = create_app()
    
    with app.app_context():
        # Clear existing bars (optional - comment out if you want to keep existing data)
        # Bar.query.delete()
        
        # Sample bars
        bars = [
            {
                'name': 'The Metal Bar',
                'address': '123 Metal Street',
                'city': 'Los Angeles',
                'state': 'CA',
                'zip_code': '90001',
                'latitude': 34.0522,
                'longitude': -118.2437,
                'description': 'A great metal bar with live music'
            },
            {
                'name': 'Rock & Roll Tavern',
                'address': '456 Rock Avenue',
                'city': 'New York',
                'state': 'NY',
                'zip_code': '10001',
                'latitude': 40.7128,
                'longitude': -74.0060,
                'description': 'Classic rock and metal venue'
            }
        ]
        
        for bar_data in bars:
            bar = Bar(**bar_data)
            db.session.add(bar)
        
        db.session.commit()
        print(f'Seeded {len(bars)} bars')


if __name__ == '__main__':
    seed_bars()

