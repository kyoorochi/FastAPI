from pydantic import BaseModel
from typing import Optional, List

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None # 옵션으로 있으면 넣고, 없으면 None으로 처리

class CreateBook(BaseModel):
    title: str
    author: str
    description: Optional[str] = None

class SearchBook(BaseModel): # BookDetail - GET
    results: Optional[Book] # Book

class SearchBooks(BaseModel): # BookList - GET
    results: List[Book] # [Book, Book, Book, ...]