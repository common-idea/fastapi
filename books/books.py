from fastapi import FastAPI
from enum import Enum


app = FastAPI()

books = {}

class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


for i in range(1,6):
    books.update({f'book_{i}':{'title':f"title {i}",'author':f"Author {i}"}})

@app.get("/books")
def list_books():
    return books

@app.post("/")
def create_book(title,author):
    current_book_id = 0
    for book in books:
        x = int(book.split('_')[-1])
        if x > current_book_id:
            current_book_id = x
    books[f"book_{current_book_id + 1}"] = {'title':title,'author':author}
    return books

@app.put("/{book_name}")
def update_book(book_name:str,title:str,author:str):
    books[book_name] = {"title":title,"author":author}
    return books

@app.get("/books/{books_title}")
def list_books(books_title: int):
    return books.get(f"book_{books_title}")

@app.get("/directions/{direction_name}")
def get_direction(direction_name:DirectionName):
    if direction_name == DirectionName.north:
        return {"direction":DirectionName.north,"sub":"Up"}
    if direction_name == DirectionName.south:
        return {"direction":DirectionName.south,"sub":"Down"}
    if direction_name == DirectionName.east:
        return {"direction":DirectionName.east,"sub":"Left"}
    return {"direction":DirectionName.west,"sub":"Right"}