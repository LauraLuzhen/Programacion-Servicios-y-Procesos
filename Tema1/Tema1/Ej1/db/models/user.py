from typing import Optional
from pydantic import BaseModel

# Entidad User
class User(BaseModel):
    id: Optional[str] = None  # MongoDB genera _id automáticamente
    name: str
    surname: str
    age: int
