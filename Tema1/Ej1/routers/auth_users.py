from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import PyJWTError
from pwdlib import PasswordHash

# Configuración
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5
SECRET_KEY = "b372149bb728e23081bbc3a12d21d10b693c5bd2fa4e2ed0a8e3abcbd972e7c8"
password_hash = PasswordHash.recommended()
router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Modelos
class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool | None = False

class UserDB(User):
    hashed_password: str

# Base de usuarios (directores)
fake_users_db = {
    "juan": {
        "username": "juan",
        "fullname": "Juan Rodríguez Villanueva",
        "email": "juanrv@gmail.com",
        "hashed_password": password_hash.hash("juan123"),
        "disabled": False
    },
    "ana": {
        "username": "ana",
        "fullname": "Ana Morán Peña",
        "email": "anamp@gmail.com",
        "hashed_password": password_hash.hash("ana123"),
        "disabled": False
    }
}

# pip install pyjwt
# pip install "pwdlib[argon2]"

# Dependencia para buscar usuario desde el token
async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=401,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        username = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM).get("sub")
        if username is None:
            raise exception
    except PyJWTError:
        raise exception
    user = User(**fake_users_db[username])
    if user.disabled:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return user

# Registrar nuevo usuario
@router.post("/register", status_code=201)
async def register_user(user: UserDB):
    new_password = password_hash.hash(user.hashed_password)
    user.hashed_password = new_password
    fake_users_db[user.username] = user.model_dump()
    return user

# Login
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = fake_users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    user = UserDB(**user_db)
    if not password_hash.verify(form.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = {"sub": user.username, "exp": expire}
    token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

# Obtener usuario actual
@router.get("/auth/me")
async def me(user: User = Depends(auth_user)):
    return user
