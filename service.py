from sqlalchemy.orm import Session
import model, schemas

def get_all_books(db: Session):
    return db.query(model.Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(model.Book).filter(model.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    