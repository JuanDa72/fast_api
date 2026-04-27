from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
import service, schemas
from dependencies import get_db
from fastapi.security import OAuth2PasswordRequestForm
import utils

router=APIRouter(prefix="/users", tags=["users"])


#Secctions for user
@router.post("/users/", response_model=schemas.UserResponse) 
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = service.create_user(db, user)
    if not new_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="User with this username or email already exists"
        )
    
    return new_user


@router.post("/login/")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user=service.get_user_by_username(db, form_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="credenciales invalidas")
    
    if not utils.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="credenciales invalidas")
    
    token_data={"sub": user.username}
    token=utils.create_access_token(token_data)
    return {"access_token": token, "token_type": "bearer"}
    
