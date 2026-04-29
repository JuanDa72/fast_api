from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from datetime import datetime

class BookBase(BaseModel):
    titulo: str
    autor: str
    anio: int
    genero: str
    disponible: bool=1

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BookUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    anio: Optional[int] = None
    genero: Optional[str] = None
    disponible: Optional[bool] = None   


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool
    role: str

    model_config = ConfigDict(from_attributes=True)


#section for loans
class LoanCreate(BaseModel):
    book_id: int
    #user id is going to be obtained from the token

class loanResponse(BaseModel):
    id: int
    user_id: int
    book_id: int
    fecha_prestamo: datetime
    fecha_devolucion: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


