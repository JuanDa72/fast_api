from fastapi import FastAPI, status, HTTPException
from typing import Optional
from pydantic import BaseModel

books = [
	{
		"id": 1,
		"titulo": "Cien anos de soledad",
		"autor": "Gabriel Garcia Marquez",
		"anio": 1967,
		"genero": "Realismo magico",
		"disponible": True,
	},
	{
		"id": 2,
		"titulo": "Don Quijote de la Mancha",
		"autor": "Miguel de Cervantes",
		"anio": 1605,
		"genero": "Novela",
		"disponible": True,
	},
	{
		"id": 3,
		"titulo": "1984",
		"autor": "George Orwell",
		"anio": 1949,
		"genero": "Distopia",
		"disponible": False,
	},
	{
		"id": 4,
		"titulo": "El principito",
		"autor": "Antoine de Saint-Exupery",
		"anio": 1943,
		"genero": "Fabula",
		"disponible": True,
	},
]

app = FastAPI()

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


class Book(BaseModel):
    id: int
    titulo: str
    autor: str
    anio: int
    genero: str
    disponible: bool

@app.post("/books")
def create_book(book: Book):
    #Model dump transform the book object into a dictionary
    new_book = book.model_dump()
    books.append(new_book)
    return {"message": "Book created successfully", "book": new_book}


class BookPut(BaseModel):
    titulo: str
    autor: str
    anio: int
    genero: str
    disponible: bool

@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookPut):
    for index, b in enumerate(books):
        if b["id"] == book_id:
            updated_book = book.model_dump()
            updated_book["id"] = book_id
            books[index] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

class BookUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    anio: Optional[int] = None
    genero: Optional[str] = None
    disponible: Optional[bool] = None

@app.patch("/books/{book_id}")
def partial_update_book(book_id: int, book: BookUpdate):
    for index, existing_book in enumerate(books):
        if existing_book["id"] == book_id:
            update_data=book.model_dump(exclude_unset=True)
            books[index].update(update_data)
            return {"message": "Book updated successfully", "book": books[index]}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(index)
            return {"message": "Book deleted successfully", "book": deleted_book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")




