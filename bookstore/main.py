import json
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.responses import JSONResponse
from models import Book
from pydantic import BaseModel

app = FastAPI()

# get book by id endpoint
@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id": book_id,
        "title": "Sukumar Samagra",
        "author": "Sukumar Roy"
    }
    
# path parameter endpoint for author
# get author by id endpoint
@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    return {
        "author_id": author_id,
        "name": "Ernest Hemingway"
    }
    
# query parameter at endpoint to get books by year
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

class BookResponse(BaseModel): # Managing response formats
    title: str
    author: str
  
# list of books, but only with their titles and authors
@app.get("/allbooks", response_model = list[BookResponse])
async def read_all_books() -> list[BookResponse]:
    return [
        {
            "id": 1,
            "title": "1984",
            "author": "George Orwell"
        },
        {
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
        },
    ]
    
    
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": "Oops! Something went wrong"
        },
    )

@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)

"""
# This custom handler will catch any RequestValidationError error and return a plain text
# response with the details of the error.
# for example, to call the POST /book endpoint with a number type of title instead of
# a string, you will get a response with a status code of 400
"""
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
    ):
    return PlainTextResponse(
        "This is a plain text response:"
        f" \n{json.dumps(exc.errors(), indent=2)}",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
"""
#     This is a plain text response: 
# [
#   {
#     "type": "string_type",
#     "loc": [
#       "body",
#       "author"
#     ],
#     "msg": "Input should be a valid string",
#     "input": 2005
#   }
# ]
 """