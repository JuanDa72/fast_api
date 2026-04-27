from sqlalchemy.orm import Session
import model, schemas
from utils import get_password_hash

def get_all_books(db: Session):
    return db.query(model.Book).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(model.Book).filter(model.Book.id == book_id).first()


def get_book_by_name(db: Session, titulo: str):
    return db.query(model.Book).filter(model.Book.titulo == titulo).first()


def create_book(db: Session, book: schemas.BookCreate):
    #First, we convert into a dictionary, then we unpack the dictionary to create a Book instance
    db_book=model.Book(**book.model_dump())
    db.add(db_book)

    try:
        db.commit()
        db.refresh(db_book)
        return db_book
    
    except Exception as e:
        db.rollback()
        print(f"Error creating book: {e}")
        return None

def put_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not db_book:
        return None
    
    update_data=book.model_dump()
    for key, value in update_data.items():
        setattr(db_book, key, value)

    try:
        db.commit()
        db.refresh(db_book)
        return db_book
    
    except Exception as e:
        db.rollback()
        print(f"Error updating book: {e}")
        return None


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
    
    try:
        db.delete(db_book)
        db.commit()
        return db_book
    
    except Exception as e:
        db.rollback()
        print(f"Error deleting book: {e}")
        return None
    

#Sections for users

def get_user_by_username(db: Session, username: str):
    return db.query(model.User).filter(model.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(model.User).filter(model.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):

    if get_user_by_email(db, user.email) or get_user_by_username(db, user.username):
        print("User with this email or username already exists")
        return None

    hashed_password = get_password_hash(user.password)
    db_user = model.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)

    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    
    except Exception as e:
        db.rollback()
        print(f"Error creating user: {e}")
        return None
    

    

