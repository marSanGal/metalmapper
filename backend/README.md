# MetalMapper Backend

Flask API backend for MetalMapper.

## Setup

1. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python run.py
```

The API will be available at `http://localhost:5000`

## Database

The application uses SQLite by default. The database file will be created automatically at `metalmapper.db` in the backend directory.

To seed sample bars:
```bash
python seeds/seed_bars.py
```

## API Endpoints

- `/api/auth/register` - Register a new user
- `/api/auth/login` - Login user
- `/api/auth/me` - Get current user
- `/api/bars` - List all bars
- `/api/bars/<id>` - Get bar details
- `/api/bars/<id>/checkins` - List/create checkins for a bar
- `/api/bars/<id>/ratings` - List/create ratings for a bar
- `/api/suggestions` - List/create bar suggestions
- `/api/admin/suggestions` - Admin endpoints for managing suggestions

