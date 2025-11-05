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

# GET
# Todos los directores
@app.get("/directors")
def directors():
    return directors_list
# Función para buscar director por id
def search_director(id: int):
    directors = [director for director in directors_list if director.id == id]

    if len(directors) != 0:
        return directors
    raise HTTPException(status_code=404, detail="Director no encontrado")
# Por el id
@app.get("/directors/{id}")
def director_id(id: int):
    return search_director(id)
# Por query id
@app.get("/directors/")
def director_query(id: int):
    return search_director(id)


# POST
# Conseguimos el próximo id
def next_id():
    return (max(directors_list, key=id).id+1)
# Realizamos el post
@app.post("/directors", status_code=201, response_model=Director)
def add_director(director: Director):
    director.id = next_id()
    directors_list.append(director)
    return director


# PUT
@app.put("/directors/{id}", response_model=Director)
def modify_director(id: int, director: Director):
    for index, saved_director in enumerate(directors_list):
        if saved_director.id == id:
            director.id = id
            directors_list[index] = director
            return director
    raise HTTPException(status_code=404, detail="Director no encontrado")


# DELETE
@app.delete("/directors/{id}")
def delete_director(id: int):
    for saved_director in directors_list:
        if saved_director.id == id:
            directors_list.remove(saved_director)
            return {}
    raise HTTPException(status_code=404, detail="Director no encontrado")