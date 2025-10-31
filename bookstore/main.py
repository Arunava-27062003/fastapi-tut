from fastapi import FastAPI

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