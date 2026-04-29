from dependencies import get_db, get_current_user
import model, schemas
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/loans", tags=["loans"])

@router.post("/loans/", response_model=schemas.loanResponse)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(get_current_user)):
    db_book = db.query(model.Book).filter(model.Book.id == loan.book_id).first()
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    if db_book.disponible <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book not available for loan")
    
    #Obtaining the user id from the token, so we don't need to send it in the request body
    db_loan = model.Loan(user_id=current_user.id, book_id=loan.book_id)
    db.add(db_loan)
    db_book.disponible -= 1
    try:
        db.commit()
        db.refresh(db_loan)
        return db_loan
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error occurred while creating loan")