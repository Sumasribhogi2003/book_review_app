from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    reviews = relationship("Review", back_populates="book")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False, index=True)
    content = Column(String, nullable=False)
    
    book = relationship("Book", back_populates="reviews")

# Index for faster filtering on book_id
Index("ix_reviews_book_id", Review.book_id)
