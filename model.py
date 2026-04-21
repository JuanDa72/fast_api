#To define the type of the variables
from sqlalchemy import Column, Integer, VARCHAR
#Base to create the models
from database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(VARCHAR(255), nullable=False)
    autor = Column(VARCHAR(255), nullable=False)
    anio = Column(Integer, nullable=False)
    genero = Column(VARCHAR(255), nullable=False)
    disponible = Column(Integer, nullable=False)
