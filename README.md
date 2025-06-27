# 📚 Book Review API 

A backend exercise to build a Book Review service using FastAPI, SQLAlchemy, Redis, and Pytest.

### ✅ Features
#### API Endpoints:
* GET /books – List all books
* POST /books – Add a new book
* GET /books/{id}/reviews – Get reviews for a specific book
* POST /books/{id}/reviews – Add a review to a book

#### Documentation:
* Auto-generated Swagger UI (/docs)

#### Data Layer:
* SQLite or PostgreSQL with SQLAlchemy
* Alembic for database migrations
* Index on reviews.book_id for optimized queries

#### Caching:
* Redis integration for /books endpoint
* Cache-first fetch, fallback to DB, populate Redis
* Handles Redis unavailability gracefully

#### Testing:
* Unit tests for core endpoints
* Integration test for cache-miss behavior

### 🛠️ Tech Stack
* Backend: FastAPI (Python)
* Database: SQLite / PostgreSQL
* ORM: SQLAlchemy
* Cache: Redis (Mock/Local)
* Migrations: Alembic
* Testing: Pytest

### 📦 Setup & Installation
* Clone the repo:
  git clone https://github.com/Sumasribhogi2003/book_review_app.git
  cd book_review_app
* Create and activate a virtual environment:
  python -m venv venv
  source venv/bin/activate  (On Windows: venv\Scripts\activate)
* Install dependencies:
  pip install -r requirements.txt
* (Optional) Start Redis locally if testing caching.


