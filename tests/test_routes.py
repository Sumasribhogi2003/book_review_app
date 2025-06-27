from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_book():
    response = client.post("/books", json={"title": "Test Book", "author": "John Doe"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["author"] == "John Doe"
    assert "id" in data

def test_add_review_to_book():
    # Create a book first
    book_resp = client.post("/books", json={"title": "Review Book", "author": "Jane"})
    book_id = book_resp.json()["id"]

    # Add a review to it
    review_resp = client.post(f"/books/{book_id}/reviews", json={"content": "Great read!"})
    assert review_resp.status_code == 200
    review = review_resp.json()
    assert review["content"] == "Great read!"
    assert review["book_id"] == book_id
