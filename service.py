from sqlalchemy.orm import Session
import model, schemas

def get_all_books(db: Session):
    return db.query(model.Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(model.Book).filter(model.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    #First, we convert into a dictionary, then we unpack the dictionary to create a Book instance
    db_book=model.Book(**book.model_dump().values())
    db.add(db_book)

    #Commit the transaction to save the book in the database
    db.commit()

    #Refresh the instance to get the generated ID and other default values
    db.refresh(db_book)

    return db_book

def update_book(db: Session, book_id: int, book: schemas.BookUpdate):
    db_book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not db_book:
        return None
    
    update_data = book.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not db_book:
        return None
    
    db.delete(db_book)
    db.commit()
    return db_book