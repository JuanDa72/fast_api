#To define the type of the variables
from sqlalchemy import Column, Integer, VARCHAR, DateTime, ForeignKey
#Base to create the models
from database import Base
from sqlalchemy.orm import relationship
#To make relations between tables 
from datetime import datetime, timezone 
#To know the hour of the loan

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(VARCHAR(255), nullable=False)
    autor = Column(VARCHAR(255), nullable=False)
    anio = Column(Integer, nullable=False)
    genero = Column(VARCHAR(255), nullable=False)
    disponible = Column(Integer, nullable=False)

    #relacion
    prestamos = relationship("Loan", back_populates="book", cascade="all, delete-orphan")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(VARCHAR(255), unique=True, index=True, nullable=False)
    email = Column(VARCHAR(255), unique=True, index=True, nullable=False)
    hashed_password = Column(VARCHAR(255), nullable=False)
    is_active = Column(Integer, default=1)

    #nuevo
    role= Column(VARCHAR(50), default="user", nullable=False)

    prestamos= relationship("Loan", back_populates="user", cascade="all, delete-orphan")


class Loan(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    fecha_prestamo = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    fecha_devolucion = Column(DateTime, nullable=True)

    user=relationship("User", back_populates="prestamos")
    book=relationship("Book", back_populates="prestamos")