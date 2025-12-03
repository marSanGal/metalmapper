# MetalMapper Database Schema

## Table Definitions

### 1. Users Table
Stores user account information.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique user identifier |
| username | VARCHAR(80) | UNIQUE, NOT NULL, INDEXED | Username for login |
| email | VARCHAR(120) | UNIQUE, NOT NULL, INDEXED | User email address |
| password_hash | VARCHAR(255) | NOT NULL | Hashed password (Werkzeug) |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Account creation timestamp |
| is_admin | BOOLEAN | DEFAULT FALSE, NOT NULL | Admin privileges flag |

**Relationships:**
- One-to-Many with Checkins
- One-to-Many with Ratings
- One-to-Many with Suggestions

---

### 2. Bars Table
Stores metal bar/venue information.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique bar identifier |
| name | VARCHAR(200) | NOT NULL | Bar name |
| address | VARCHAR(500) | NULLABLE | Street address |
| city | VARCHAR(100) | NULLABLE | City name |
| state | VARCHAR(50) | NULLABLE | State/Province |
| zip_code | VARCHAR(20) | NULLABLE | ZIP/Postal code |
| latitude | FLOAT | NULLABLE | GPS latitude coordinate |
| longitude | FLOAT | NULLABLE | GPS longitude coordinate |
| description | TEXT | NULLABLE | Bar description |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Creation timestamp |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP, ON UPDATE | Last update timestamp |

**Relationships:**
- One-to-Many with Checkins
- One-to-Many with Ratings

---

### 3. Checkins Table
Tracks user check-ins at bars.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique checkin identifier |
| user_id | INTEGER | FOREIGN KEY (users.id), NOT NULL | User who checked in |
| bar_id | INTEGER | FOREIGN KEY (bars.id), NOT NULL | Bar where checkin occurred |
| notes | TEXT | NULLABLE | Optional notes about the visit |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Checkin timestamp |

**Relationships:**
- Many-to-One with User
- Many-to-One with Bar

**Indexes:**
- Composite index on (user_id, bar_id) for quick lookups
- Index on created_at for chronological queries

---

### 4. Ratings Table
Stores user ratings and reviews for bars.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique rating identifier |
| user_id | INTEGER | FOREIGN KEY (users.id), NOT NULL | User who gave the rating |
| bar_id | INTEGER | FOREIGN KEY (bars.id), NOT NULL | Bar being rated |
| rating | INTEGER | NOT NULL, CHECK (1-5) | Rating value (1-5 scale) |
| comment | TEXT | NULLABLE | Optional review comment |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Rating creation timestamp |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP, ON UPDATE | Last update timestamp |

**Relationships:**
- Many-to-One with User
- Many-to-One with Bar

**Constraints:**
- UNIQUE constraint on (user_id, bar_id) - one rating per user per bar
- CHECK constraint: rating must be between 1 and 5

**Indexes:**
- Composite index on (user_id, bar_id)
- Index on bar_id for aggregating ratings per bar

---

### 5. Suggestions Table
Stores user-submitted bar suggestions awaiting admin approval.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Unique suggestion identifier |
| user_id | INTEGER | FOREIGN KEY (users.id), NOT NULL | User who submitted suggestion |
| name | VARCHAR(200) | NOT NULL | Suggested bar name |
| address | VARCHAR(500) | NULLABLE | Street address |
| city | VARCHAR(100) | NULLABLE | City name |
| state | VARCHAR(50) | NULLABLE | State/Province |
| zip_code | VARCHAR(20) | NULLABLE | ZIP/Postal code |
| description | TEXT | NULLABLE | Bar description |
| status | VARCHAR(20) | DEFAULT 'pending' | Status: pending, approved, rejected |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Submission timestamp |
| reviewed_at | DATETIME | NULLABLE | Review timestamp |
| reviewed_by | INTEGER | FOREIGN KEY (users.id), NULLABLE | Admin who reviewed |

**Relationships:**
- Many-to-One with User (submitter)
- Many-to-One with User (reviewer/admin)

**Indexes:**
- Index on status for filtering pending suggestions
- Index on user_id for user's suggestions
- Index on created_at for chronological sorting

---

## Entity Relationship Diagram

```
Users
  ├── Checkins (1:N)
  ├── Ratings (1:N)
  └── Suggestions (1:N as submitter)
       └── Suggestions.reviewed_by (1:N as reviewer)

Bars
  ├── Checkins (1:N)
  └── Ratings (1:N)
```

## Notes

- All timestamps use UTC timezone
- Password hashing uses Werkzeug's security utilities
- Foreign keys have CASCADE delete for related records
- Rating values are constrained to 1-5 scale
- One rating per user per bar (enforced by unique constraint)
- Suggestions workflow: pending → approved/rejected

