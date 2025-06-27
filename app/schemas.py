from pydantic import BaseModel
from typing import List


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


class ReviewCreate(BaseModel):
    content: str


class Review(ReviewCreate):
    id: int
    book_id: int

    model_config = {
        "from_attributes": True
    }
