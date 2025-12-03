# Database Setup Guide

## Quick Start (SQLite - Default)

SQLite is configured by default and requires no setup. The database file will be created automatically at `backend/instance/metalmapper.db` when you first run the application.

```bash
cd backend
python run.py
```

## Environment Configuration

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` with your configuration (optional for SQLite):
   ```bash
   # For SQLite (default)
   DATABASE_URL=sqlite:///instance/metalmapper.db
   ```

## PostgreSQL Setup

### 1. Install PostgreSQL

**macOS:**
```bash
brew install postgresql@15
brew services start postgresql@15
```

**Ubuntu/Debian:**
```bash
sudo apt-get install postgresql postgresql-contrib
sudo systemctl start postgresql
```

### 2. Create Database

```bash
# Connect to PostgreSQL
psql postgres

# Create database and user
CREATE DATABASE metalmapper;
CREATE USER metalmapper_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE metalmapper TO metalmapper_user;
\q
```

### 3. Update .env

```bash
DATABASE_URL=postgresql://metalmapper_user:your_password@localhost:5432/metalmapper
```

### 4. Install PostgreSQL Driver

Add to `requirements.txt`:
```
psycopg2-binary==2.9.9
```

Then install:
```bash
pip install psycopg2-binary
```

## MySQL Setup

### 1. Install MySQL

**macOS:**
```bash
brew install mysql
brew services start mysql
```

**Ubuntu/Debian:**
```bash
sudo apt-get install mysql-server
sudo systemctl start mysql
```

### 2. Create Database

```bash
# Connect to MySQL
mysql -u root -p

# Create database and user
CREATE DATABASE metalmapper CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'metalmapper_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON metalmapper.* TO 'metalmapper_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 3. Update .env

```bash
DATABASE_URL=mysql+pymysql://metalmapper_user:your_password@localhost:3306/metalmapper
```

### 4. Install MySQL Driver

Add to `requirements.txt`:
```
PyMySQL==1.1.0
```

Then install:
```bash
pip install PyMySQL
```

## Database Initialization

The database tables are automatically created when you run the Flask application:

```bash
cd backend
python run.py
```

The `db.create_all()` function in `app/__init__.py` will create all tables defined in your models.

## Seeding Data

To seed the database with sample bars:

```bash
cd backend
python seeds/seed_bars.py
```

## Database Location

- **SQLite**: `backend/instance/metalmapper.db`
- **PostgreSQL/MySQL**: As configured in `DATABASE_URL`

## Connection Pooling

For PostgreSQL and MySQL, connection pooling is configured with:
- Pool size: 10 connections
- Max overflow: 20 connections
- Connection recycling: 5 minutes
- Connection verification: Enabled (pool_pre_ping)

## Troubleshooting

### SQLite Database Locked
If you get a "database is locked" error:
- Make sure only one process is accessing the database
- Check for stale lock files in the instance directory

### PostgreSQL Connection Issues
- Verify PostgreSQL is running: `brew services list` or `sudo systemctl status postgresql`
- Check connection string format: `postgresql://user:pass@host:port/dbname`
- Verify user permissions: `psql -U metalmapper_user -d metalmapper`

### MySQL Connection Issues
- Verify MySQL is running: `brew services list` or `sudo systemctl status mysql`
- Check connection string format: `mysql+pymysql://user:pass@host:port/dbname`
- Verify user permissions: `mysql -u metalmapper_user -p metalmapper`

