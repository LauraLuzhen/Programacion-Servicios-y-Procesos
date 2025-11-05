# DIRECTOR (Id, DNI, Nombre, Apellidos, Nacionalidad)

from pydantic import BaseModel
import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, HTTPException

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Cambiamos de terminal y ponemos: openssl rand -hex 32
# Clave de cifrado del token
SECRET_KEY = "0b39e375e88068503d4057f0a717bf1fa220c82341cd9cecf662820cba50d256"
# Algoritmo de cifrado del token
ALGORITHM = "HS256"
# Duración del token en minutos
ACCESS_TOKEN_EXPIRE_MINUTES = 5
# Objeto para hashear las contraseñas
password_hash = PasswordHash.recommended()

class Director(BaseModel):
    dni: str
    nombre: str
    apellidos: str
    nacionalidad: str
    disabled: bool # Me permite saber si el us uario está activo o no

class DirectorDB(Director):
    password: str

directors_db = {
    "laura": {
        "dni": "12345678A",
        "nombre": "Laura",
        "apellidos": "Rodríguez Morán",
        "nacionalidad": "española",
        "disabled": False,
        "password": "secret1",
    },
    "juan": {
        "dni": "87654321B",
        "nombre": "Juan",
        "apellidos": "Pérez Gómez",
        "nacionalidad": "mexicana",
        "disabled": True,
        "password": "secret2",
    },
    "guille": {
        "dni": "11223344C",
        "nombre": "Guillermo",
        "apellidos": "López Sánchez",
        "nacionalidad": "argentina",
        "disabled": False,
        "password": "secret3",
    }
}

@router.post("/register", status_code=201)
def register(director: DirectorDB):
    if director.nombre not in directors_db:
        hashed_password = password_hash.hash(director.password)
        director.password = hashed_password
        directors_db[director.nombre] = director
        return director
    raise HTTPException(status_code=409, detail="El director ya existe")
