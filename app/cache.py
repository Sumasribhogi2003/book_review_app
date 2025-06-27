import redis
import json
from fastapi import HTTPException

# Connect to Redis (mock or real)
try:
    r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
    # Ping to check connection
    r.ping()
except redis.RedisError as e:
    print("⚠️ Redis not available:", str(e))
    r = None

BOOKS_CACHE_KEY = "books_cache"

def get_books_from_cache():
    if not r:
        raise ConnectionError("Redis not available")
    cached_data = r.get(BOOKS_CACHE_KEY)
    if cached_data:
        return json.loads(cached_data)
    return None

def set_books_to_cache(books):
    if not r:
        raise ConnectionError("Redis not available")
    r.set(BOOKS_CACHE_KEY, json.dumps(books), ex=60)  # Cache for 60 seconds
