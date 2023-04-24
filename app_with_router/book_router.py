from fastapi import APIRouter
from pydantic import BaseModel

tag_name = 'Book'
book_router = APIRouter()

class Book(BaseModel):
    name: str
    price: str
    description: str

all_books = [{"name": "Real Estate Investing for Cash Flow",
    "price": "$50",
    "description": "Book to start your real estate journey"}]

@book_router.get('/', tags=[tag_name])
def books():
    return all_books

@book_router.post('/', tags=[tag_name])
def add_book(book: Book):
    all_books.append(book.dict())
    return all_books