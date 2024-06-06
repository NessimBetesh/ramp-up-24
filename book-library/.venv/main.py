from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID

app = FastAPI()
class Book(BaseModel):
    id: UUID
    title: str
    author: str
    year: int

class BookCreate(BaseModel):
    title: str
    author: str
    year: int

books = []

@app.post("/books/", response_model=Book)
def create_book(book: BookCreate):
    new_book = Book(id=uuid4(), **book.dict())
    books.append(new_book)
    return new_book

@app.get("/books/", response_model=List[Book])
def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: UUID):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException("Book not found")

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: UUID, updated_book: BookCreate):
    for book in books:
        if book.id == book_id:
            book.title = updated_book.title
            book.author = updated_book.author
            book.year = updated_book.year
            return book
    raise HTTPException("Book not found")

@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: UUID):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return book
    raise HTTPException("Book not found")