# DIRECTOR (Id, DNI, Nombre, Apellidos, email)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/directors", tags=["directors"])

# Entidad director
class Director(BaseModel):
    id: int
    dni: str
    nombre: str
    apellidos: str
    email: str

# Lista de directores
directores_list = [
    Director(id=1, dni="12345678A", nombre="Juan", apellidos="Rodríguez Villanueva", email="juanrv@gmail.com"),
    Director(id=2, dni="21436587B", nombre="Ana", apellidos="Rodríguez Villanueva", email="anarv@gmail.com"),
    Director(id=3, dni="87654321C", nombre="Ana", apellidos="Morán Peña", email="anamp@gmail.com"),
    Director(id=4, dni="78563412D", nombre="Julio", apellidos="Peña Sicilia", email="juliops@gmail.com"),
    Director(id=5, dni="11223344E", nombre="Paco", apellidos="García Sicilia", email="pacogs@gmail.com"),
]

# GET
# Todos los directores
@router.get("/")
def directores():
    return directores_list
# Método para buscar al usuario por el id
def search_id(id : int):
    directors = [director for director in directores_list if director.id == id]
    if len(directors) != 0:
        return directors
    else:
        raise HTTPException(status_code=404, detail="Director no encotrado")
# Conseguir con id
@router.get("/{id}")
def director_id(id : int):
    return search_id(id)
# Conseguir query con id
@router.get("")
def director_queryid(id : int):
    return search_id(id)


# POST
@router.post("/", status_code=201, response_model=Director)
def add_director(director : Director):
    director.id = next_id()
    directores_list.append(director)
    return director
# Método para conseguir el próximo id
def next_id():
    return (max(directores_list, key=id).id+1)


# PUT
@router.put("/{id}", response_model=Director)
def modify_director(id : int, director : Director):
    for index, saved in enumerate(directores_list):
        if saved.id == id:
            director.id = id
            directores_list[index] = director
            return director
    raise HTTPException(status_code=404, detail="Director no encontrado")


# DELETE
@router.delete("/{id}")
def delete_director(id : int):
    for saved in directores_list:
        if saved.id == id:
            directores_list.remove(saved)
            return {}
    raise HTTPException(status_code=404, detail="Director no encontrado")