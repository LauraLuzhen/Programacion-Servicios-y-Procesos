from datetime import *
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Librería JWT
import jwt

# Para trabajar las excepciones de los tokens
from jwt.exceptions import PyJWTError

# Librería para aplicar un hash a la contraseña
from pwdlib import PasswordHash

# Definimos el algoritmo de encriptación
ALGORITHM = "HS256"

# Duración del token
ACCESS_TOKEN_EXPIRE_MINUTES = 1

# Clave que se utilizará como semilla para generar el token
# openssl rand -hex 32
SECRET_KEY = "72fd45b13487001ab0d5f17b1a4b37711da8be523d5e60a18f82fc327632934a"

# Objeto que se utilizará para el cálculo del hash y 
# la verificación de las contraseñas
password_hash = PasswordHash.recommended()

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    fullname:str
    email:str
    disabled: bool | None = False

class UserDB(User):
    hashed_password: str

fake_users_db = {
    "laura": {
        "username": "Laura",
        "fullname": "Laura Rodríguez Morán",
        "email": "ll.rodriguez@iesnervion.es",
        "hashed_password": password_hash.hash("1234"),
        "disabled": False
    }
}

def search_user_db(username: str):
    if username in fake_users_db:
        return UserDB(fake_users_db[username])
    

async def auth_user(token:str = Depends(oauth2)):    
    exception = HTTPException(status_code=401, 
                            detail="Credenciales de autenticación inválidas", 
                            headers={"WWW-Authenticate" : "Bearer"})
    try:        
        username = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM).get("sub")
        if username is None:
            raise HTTPException(status_code=401, 
                            detail="Credenciales de autenticación inválidas", 
                            headers={"WWW-Authenticate" : "Bearer"})       
    except PyJWTError:
        raise HTTPException(status_code=401, 
                            detail="Credenciales de autenticación inválidas", 
                            headers={"WWW-Authenticate" : "Bearer"})
    user = User(**fake_users_db[username])

    if user.disabled:
        raise HTTPException(status_code=400, 
                            detail="Usuario inactivo")   
    return user


@router.post("/register", status_code=201)
async def register_user(user: UserDB):
    print("entro en el registro")
    new_password = password_hash.hash(user.hashed_password)
    user.hashed_password = new_password
    fake_users_db[user.username] = user.model_dump()
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):    
    user_db = fake_users_db.get(form.username)   
    if not user_db:
        raise HTTPException(status_code = 400, detail="Usuario no encontrado")
    user = UserDB(**fake_users_db[form.username])

    if not password_hash.verify(form.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")  

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = {"sub" : user.username, "exp":expire}
    token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token" : token, "token_type": "bearer"}


@router.get("/auth/me")
async def me(user: User = Depends(auth_user)):
    return user