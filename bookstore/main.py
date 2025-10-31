from fastapi import FastAPI
from models import Book

app = FastAPI()

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id": book_id,
        "title": "Sukumar Samagra",
        "author": "Sukumar Roy"
    }
    
# path parameter endpoint
@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    return {
        "author_id": author_id,
        "name": "Ernest Hemingway"
    }
    
# query parameter at endpoint
@app.get("/books")
async def read_books(year: int = None): # here year is a optional parameter
    if year:
        return {
            "year": year,
            "book": ["Book 1", "Book 2"]
        }
    return { "books": ["All Books"] }

# add endpoint to our application where users can add new books
# user sends a POST request to the /book endpoint with JSON data
@app.post("/book")
async def create_book(book: Book):
    return book