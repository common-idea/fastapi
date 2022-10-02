from fastapi import FastAPI
from uuid import UUID
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()

BOOKS = []

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    description: Optional[str] = Field(title="Description of the book",min_length=1)
    rating: int = Field(gt=-1,lt=101)
    
    class Config:
        schema_extra = {
            "example" : {
                "id" : "891286916919-9832yi-y6273t2-2y63273",
                "title" : "Computer science book",
                "author" : "A very nice description",
                "rating" : 75
            }
        }
    
@app.get("/")
def list_books():
    return BOOKS

@app.post("/")
def create_book(book:Book):
    BOOKS.append(book)
    return book