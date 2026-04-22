from pydantic import BaseModel, ConfigDict
from typing import Optional

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

