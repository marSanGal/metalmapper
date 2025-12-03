"""Seed script for populating bars with 10 test bars."""
from app import create_app, db
from app.models.bar import Bar


def seed_bars():
    """Seed database with 10 test bars."""
    app = create_app()
    
    with app.app_context():
        # Clear existing bars (optional - comment out if you want to keep existing data)
        # Bar.query.delete()
        
        # Check if bars already exist
        existing_count = Bar.query.count()
        if existing_count > 0:
            print(f'Database already contains {existing_count} bars.')
            response = input('Do you want to add more bars? (y/n): ')
            if response.lower() != 'y':
                print('Skipping seed.')
                return
        
        # 10 Test bars in London, UK
        bars = [
            {
                'name': 'The Black Heart',
                'address': '3 Greenland Place',
                'city': 'London',
                'state': 'England',
                'zip_code': 'NW1 0AP',
                'latitude': 51.5406,
                'longitude': -0.1378,
                'description': 'Legendary metal bar in Camden Town. Features live bands every weekend, extensive craft beer selection, and a dark, atmospheric vibe perfect for metalheads.'
            },
            {
                'name': 'The Devonshire Arms',
                'address': '33 Kentish Town Road',
                'city': 'London',
                'state': 'England',
                'zip_code': 'NW1 8NL',
                'latitude': 51.5439,
                'longitude': -0.1419,
                'description': 'Classic metal pub in Camden with a killer jukebox. Known for their metal-themed cocktails and friendly staff. Great place to catch local bands.'
            },
            {
                'name': 'The Crobar',
                'address': '17 Manette Street',
                'city': 'London',
                'state': 'England',
                'zip_code': 'W1D 4AR',
                'latitude': 51.5142,
                'longitude': -0.1308,
                'description': 'Underground metal bar in Soho. Dark, intimate atmosphere with an impressive collection of metal memorabilia. Cash only, no pretensions.'
            },
            {
                'name': 'The Big Red',
                'address': '385 Holloway Road',
                'city': 'London',
                'state': 'England',
                'zip_code': 'N7 0RY',
                'latitude': 51.5567,
                'longitude': -0.1117,
                'description': 'Metal bar in Islington with a stage for live bands. Hosts local and touring metal acts. Great selection of beers and spirits.'
            },
            {
                'name': 'The Unicorn',
                'address': '227 Camden High Street',
                'city': 'London',
                'state': 'England',
                'zip_code': 'NW1 7BU',
                'latitude': 51.5401,
                'longitude': -0.1414,
                'description': 'Traditional pub with heavy metal leanings. Known for their metal nights and themed events. Friendly atmosphere and decent pub grub.'
            },
            {
                'name': 'The Underworld',
                'address': '174 Camden High Street',
                'city': 'London',
                'state': 'England',
                'zip_code': 'NW1 7NE',
                'latitude': 51.5392,
                'longitude': -0.1425,
                'description': 'Iconic underground metal venue in Camden. Hosts extreme metal shows, metal trivia nights, and has a legendary mosh pit area.'
            },
            {
                'name': 'The Fighting Cocks',
                'address': '75 Old Street',
                'city': 'London',
                'state': 'England',
                'zip_code': 'EC1V 9HX',
                'latitude': 51.5238,
                'longitude': -0.0975,
                'description': 'Metal bar in Shoreditch with industrial vibes. Great sound system, extensive whiskey selection, and regular metal DJ nights.'
            },
            {
                'name': 'The Intrepid Fox',
                'address': '97 Wardour Street',
                'city': 'London',
                'state': 'England',
                'zip_code': 'W1F 0UD',
                'latitude': 51.5139,
                'longitude': -0.1350,
                'description': 'Gothic metal bar in Soho. Dark atmosphere with metal and goth music. Known for their themed events and metal karaoke nights.'
            },
            {
                'name': 'The World\'s End',
                'address': '174 Camden High Street',
                'city': 'London',
                'state': 'England',
                'zip_code': 'NW1 7NE',
                'latitude': 51.5390,
                'longitude': -0.1426,
                'description': 'Metal pub in Camden with a great selection of ales and craft beers. The walls are covered in metal posters and band stickers.'
            },
            {
                'name': 'The Dev',
                'address': '363 Kentish Town Road',
                'city': 'London',
                'state': 'England',
                'zip_code': 'NW5 2TJ',
                'latitude': 51.5512,
                'longitude': -0.1408,
                'description': 'Local metal pub in Kentish Town. No-frills atmosphere with cheap drinks, loud music, and a loyal metalhead following.'
            }
        ]
        
        added_count = 0
        for bar_data in bars:
            # Check if bar already exists by name
            existing_bar = Bar.query.filter_by(name=bar_data['name']).first()
            if not existing_bar:
                bar = Bar(**bar_data)
                db.session.add(bar)
                added_count += 1
            else:
                print(f'Bar "{bar_data["name"]}" already exists, skipping...')
        
        db.session.commit()
        print(f'\n✓ Successfully seeded {added_count} new bars')
        print(f'Total bars in database: {Bar.query.count()}')


if __name__ == '__main__':
    seed_bars()

