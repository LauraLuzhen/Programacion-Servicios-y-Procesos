# DIRECTOR (Id, DNI, Nombre, Apellidos, Nacionalidad)

import datetime
from pydantic import BaseModel
import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException

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

class User(BaseModel):
    dni: str
    nombre: str
    apellidos: str
    nacionalidad: str
    disabled: bool # Me permite saber si el us uario está activo o no

class UserDB(User):
    password: str

users_db = {
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
    "Guillermo": {
        "dni": "29519783L",
        "nombre": "Guillermo Simón",
        "apellidos": "Villanueva Sánchez",
        "nacionalidad": "argentina",
        "disabled": False,
        "password": "secret3",
    }
}

@router.post("/register", status_code=201)
def register(user: UserDB):
    if user.nombre not in users_db:
        hashed_password = password_hash.hash(user.password)
        user.password = hashed_password
        users_db[user.nombre] = user
        return user
    raise HTTPException(status_code=409, detail="El usuario ya existe")

# Importamos el Depends del fastapi
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form.username)
    if user:
        #Si el usuario existe en la bd comprobamos la contraseña
        if password_hash.verify(form.password, user["password"]):
            #Si la contraseña es correcta creamos el token
            expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = {"sub": user.username, "exp": expire}
            # generamos el token
            token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
            return {"access_token": token, "token_type": "bearer"}
        # raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    raise HTTPException(status_code=404, detail="El usuario no existe")