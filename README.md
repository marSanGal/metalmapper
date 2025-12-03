# MetalMapper

A full-stack monorepo application for mapping and discovering metal bars.

## Project Structure

```
metalmapper/
├── backend/          # Flask API
│   ├── app/         # Application code
│   ├── seeds/       # Database seed scripts
│   └── run.py       # Application entry point
└── frontend/         # React application
    ├── src/         # Source code
    └── public/      # Static assets
```

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask server:
```bash
python run.py
```

The API will be available at `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The app will be available at `http://localhost:3000`

## Features

- User authentication (register/login)
- Browse metal bars
- View bar details
- Check in at bars
- Rate bars
- Suggest new bars
- Admin panel for managing suggestions

## Tech Stack

**Backend:**
- Python 3
- Flask
- SQLAlchemy
- SQLite

**Frontend:**
- React
- Vite
- React Router
- Axios

## Development

This is a monorepo structure. Both backend and frontend can be developed independently. The frontend is configured to proxy API requests to the backend during development.

