from pydantic import BaseModel

"""
Here, Book is a Pydantic BaseModel class with three fields: title, author, and year. Each
field is typed, ensuring that any data conforming to this model will have these attributes with the
specified data types.
"""
class Book(BaseModel):
    title: str
    author: str
    year: int