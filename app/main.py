from fastapi import FastAPI
from app.routes import books
from app.database import engine
from app.models import Base

app = FastAPI(title="📚 Book Review API")

Base.metadata.create_all(bind=engine)

# Include the books router
app.include_router(books.router)

# Add this root route
@app.get("/")
def root():
    return {"message": "📚 Welcome to the Book Review API!"}
