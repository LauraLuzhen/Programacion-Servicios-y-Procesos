from typing import Optional
from pydantic import BaseModel

class Pelicula(BaseModel):
    id: Optional[str] = None
    titulo: str
    duracion: float
    idDirector: int