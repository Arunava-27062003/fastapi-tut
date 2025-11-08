from pydantic import BaseModel, Field

"""
Here, Book is a Pydantic BaseModel class with three fields: title, author, and year. Each
field is typed, ensuring that any data conforming to this model will have these attributes with the
specified data types.
"""
class Book(BaseModel):
    title: str = Field(...,min_length=1, max_length=100) # Validating request data
    author: str = Field(...,min_length=1, max_length=100) # Validating request data
    year: int = Field(...,gt=1900, lt=2100) # Validating request data