from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str] = None
    username: str
    fullname: str
    emil: str
    disbled: bool