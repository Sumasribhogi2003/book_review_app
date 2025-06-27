import json
from fastapi.testclient import TestClient
from app.main import app
from app.cache import r, BOOKS_CACHE_KEY

client = TestClient(app)

def test_cache_miss_get_books():
    # Ensure Redis key is deleted to simulate a cache miss
    if r:
        r.delete(BOOKS_CACHE_KEY)

    # Add a book to DB (to ensure data exists even if cache is empty)
    client.post("/books", json={"title": "Cache Test Book", "author": "Cache Author"})

    # First request - should fetch from DB and set cache
    response = client.get("/books")
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)
    assert any(b["title"] == "Cache Test Book" for b in books)

    # Second request - should fetch from cache (manually check if Redis contains it)
    if r:
        cached_data = r.get(BOOKS_CACHE_KEY)
        assert cached_data is not None
        cached_books = json.loads(cached_data)
        assert any(b["title"] == "Cache Test Book" for b in cached_books)
