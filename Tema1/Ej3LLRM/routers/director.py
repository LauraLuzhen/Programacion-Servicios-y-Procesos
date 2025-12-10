# Laura Luzhen Rodríguez Morán

from fastapi import APIRouter , HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/directors", tags=["directors"])


class Director(BaseModel):
    id: int
    dni: str
    nombre: str
    apellidos: str
    nacionalidad: str

directors_list = [
    Director(id=1, dni="11111111A", nombre="Laura", apellidos="Rodríguez Morán", nacionalidad="española"),
    Director(id=2, dni="22222222B", nombre="Mohammed", apellidos="Alí Jhonson", nacionalidad="afroamericana"),
    Director(id=3, dni="33333333C", nombre="Guillermo", apellidos="Villanueva Roldán", nacionalidad="china"),
    Director(id=4, dni="44444444D", nombre="Ana", apellidos="Apelli Dos", nacionalidad="española"),
    Director(id=5, dni="55555555E", nombre="Hugo", apellidos="Apelli Dos", nacionalidad="española"),
]

# GET
# Todos los directores
@router.get("/")
def directors():
    return directors_list
# Función para buscar director por id
def search_director(id: int):
    directors = [director for director in directors_list if director.id == id]

    if len(directors) != 0:
        return directors
    raise HTTPException(status_code=404, detail="Director no encontrado")
# Por el id
@router.get("/{id}")
def director_id(id: int):
    return search_director(id)
# Por query id
@router.get("")
def director_query(id: int):
    return search_director(id)


# POST
# Conseguimos el próximo id
def next_id():
    return (max(directors_list, key=id).id+1)
# Realizamos el post
@router.post("/", status_code=201, response_model=Director)
def add_director(director: Director):
    director.id = next_id()
    directors_list.append(director)
    return director


# PUT
@router.put("/{id}", response_model=Director)
def modify_director(id: int, director: Director):
    for index, saved_director in enumerate(directors_list):
        if saved_director.id == id:
            director.id = id
            directors_list[index] = director
            return director
    raise HTTPException(status_code=404, detail="Director no encontrado")


# DELETE
@router.delete("/{id}")
def delete_director(id: int):
    for saved_director in directors_list:
        if saved_director.id == id:
            directors_list.remove(saved_director)
            return {}
    raise HTTPException(status_code=404, detail="Director no encontrado")