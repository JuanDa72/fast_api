from fastapi import FastAPI
from database import engine
import model
from router_books import router as book_router

#Create the database tables
model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Books API", description="API for managing books", version="1.0.0")
app.include_router(book_router)

@app.get("/")
def read_root():
    return {"Message":"Welcome to the Books API"}