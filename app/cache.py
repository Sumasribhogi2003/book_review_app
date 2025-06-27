import redis
import json

# Connect to Redis (mock or real)
try:
    r = redis.Redis(
        host="localhost",
        port=6379,
        db=0,
        decode_responses=True,
        socket_connect_timeout=1  # Avoids long hanging
    )
    r.ping()
except redis.RedisError as e:
    print("⚠️ Redis not available:", str(e))
    r = None

BOOKS_CACHE_KEY = "books_cache"


def get_books_from_cache():
    if not r:
        return None  # ✅ Don’t raise — just skip cache
    try:
        cached_data = r.get(BOOKS_CACHE_KEY)
        if cached_data:
            return json.loads(cached_data)
    except Exception as e:
        print(f"⚠️ Redis get failed: {e}")
    return None


def set_books_to_cache(books):
    if not r:
        return  # ✅ Skip silently if Redis is unavailable
    try:
        r.set(BOOKS_CACHE_KEY, json.dumps(books), ex=60)
    except Exception as e:
        print(f"⚠️ Redis set failed: {e}")
