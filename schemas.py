from pydantic import BaseModel, ConfigDict

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