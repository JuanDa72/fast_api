from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
import service, schemas
from dependencies import get_db

#Use tags to group the endpoints in the documentation
router=APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    return service.get_all_books(db)


@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = service.get_book_by_id(db, book_id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return db_book


@router.post("/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    existing_book = service.get_book_by_name(db, book.titulo)
    if existing_book:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book with this title already exists")
    
    db_book = service.create_book(db, book)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating book")
    return db_book


@router.put("/{book_id}", response_model=schemas.BookResponse)
def replace_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = service.put_book(db, book_id, book)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return db_book


@router.patch("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = service.update_book(db, book_id, book)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return db_book


@router.delete("/{book_id}", response_model=schemas.BookResponse)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted_book=service.delete_book(db, book_id)
    if not deleted_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    return deleted_book