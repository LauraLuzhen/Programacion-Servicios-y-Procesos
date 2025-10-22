# Laura Luzhen Rodríguez Morán

from http.client import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Director(BaseModel):
    id: int
    dni: str
    nombre: str
    apellidos: str
    nacionalidad: str

directors_list = [
    Director(id=1, dni="11111111A", nombre="Hugo", apellidos="Domínguez Ferrer", nacionalidad="española"),
    Director(id=2, dni="22222222B", nombre="Mohammed", apellidos="Alí Jhonson", nacionalidad="afroamericana"),
    Director(id=3, dni="33333333C", nombre="Mike", apellidos="Tyson Rodríguez", nacionalidad="chino"),
    Director(id=4, dni="44444444D", nombre="Nombre", apellidos="Apelli Dos", nacionalidad="teclado"),
    Director(id=5, dni="55555555E", nombre="Hugo", apellidos="Otroaplli Dos", nacionalidad="teclado"),
]

# Todos los directores
@app.get("/directors")
def directors():
    return directors_list

# Función para buscar director por id
def search_director(id: int):
    directors = [director for director in directors_list if director.id == id]

    if len(directors) != 0:
        return directors[0]
    raise HTTPException(status_code=404, detail="Director no encontrado")

# Por el id
@app.get("/directors/{id}")
def director_id(id: int):
    return search_director(id)
# Por query id
@app.get("/directors/")
def director_query(id: int):
    return search_director(id)

# post
def next_id():
    return (max(directors_list, key=lambda director: director.id).id + 1)