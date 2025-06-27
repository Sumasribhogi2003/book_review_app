from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal
from app.cache import get_books_from_cache, set_books_to_cache

router = APIRouter()


# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ GET /books — Fetch all books (with Redis cache)
@router.get("/books", response_model=list[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    try:
        # Try to get books from cache
        cached_books = get_books_from_cache()
        if cached_books:
            return cached_books
    except Exception as e:
        print("⚠️ Cache error:", str(e))  # Log error and fallback to DB

    # Fallback to DB if cache miss or error
    books = db.query(models.Book).all()
    books_data = [schemas.Book.model_validate(book).model_dump() for book in books]

    try:
        set_books_to_cache(books_data)
    except Exception as e:
        print("⚠️ Failed to write to cache:", str(e))

    return books_data


# ✅ POST /books — Add a new book
@router.post("/books", response_model=schemas.Book)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# ✅ GET /books/{book_id}/reviews — Get reviews for a book
@router.get("/books/{book_id}/reviews", response_model=list[schemas.Review])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()


# ✅ POST /books/{book_id}/reviews — Add a review to a book
@router.post("/books/{book_id}/reviews", response_model=schemas.Review)
def add_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db_review = models.Review(content=review.content, book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
