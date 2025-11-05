# SUPERMERCADO(Id, Fecha, Superficie, Dirección, IdDirector)

from fastapi import APIRouter, HTTPException 
from pydantic import BaseModel
from routers.director import directores_list

router = APIRouter(prefix="/supermarkets", tags=["supermarkets"])

# Entidad Supermercado
class Supermercado(BaseModel):
    id: int
    fecha: str
    superficie: str
    direccion: str
    id_director: int

# Lista de supermercados
supermarkets_list = [
    Supermercado(id=1, fecha="01/12/2016", superficie="plana", direccion="Calle Alfonso 14", id_director=5),
    Supermercado(id=2, fecha="12/06/2011", superficie="plana", direccion="Calle Federico 9", id_director=5),
    Supermercado(id=3, fecha="06/11/2022", superficie="plana", direccion="Calle María Luisa 18", id_director=3),
    Supermercado(id=4, fecha="25/12/2018", superficie="plana", direccion="Plaza Aljarafe 1", id_director=4),
    Supermercado(id=5, fecha="02/09/2025", superficie="plana", direccion="Calle Alfonso 2", id_director=2),
]

# GET
# Listado de todos los supermercados
@router.get("/")
def supermarkets():
    return supermarkets_list
# Método que busca por id
def search(id : int):
    supermarkets = [supermarket for supermarket in supermarkets_list if supermarket.id == id]
    if len(supermarkets) != 0:
        return supermarkets
    else:
        raise HTTPException(status_code=404, detail="Supermercado no encontrado")
# Get con id
@router.get("/{id}")
def supermarket_getid(id : int):
    return search(id)
# Get con id query
@router.get("")
def supermarket_getqueryid(id : int):
    return search(id)


# POST
@router.post("/", status_code=201, response_model=Supermercado)
def supermarket_post(supermarket: Supermercado):
    supermarket.id = next_id()
    directors_id = [director.id for director in directores_list]

    if supermarket.id_director not in directors_id:
        raise HTTPException(status_code=404, detail="El id del director no existe")
    else:
        supermarkets_list.append(supermarket)
        return supermarket
# Método para conseguir el próximo id
def next_id():
    return (max(supermarkets_list, key=id).id+1)


# PUT
@router.put("/{id}", response_model=Supermercado)
def supermarket_put(id : int, supermarket : Supermercado):
    for index, saved in enumerate(supermarkets_list):
        if saved.id == id:
            directors_id = [director.id for director in directores_list]

            if supermarket.id_director not in directors_id:
                raise HTTPException(status_code=404, detail="El id del director no existe")
            else:
                supermarket.id = id
                supermarkets_list[index] = supermarket
                return supermarket
        else:
            raise HTTPException(status_code=404, detail="El supermercado no encontrado")
        

# DELETE
@router.delete("/{id}")
def supermarket_delete(id : int):
    for saved in supermarkets_list:
        if saved.id == id:
            supermarkets_list.remove(saved)
            return {}
        else: 
            raise HTTPException(status_code=404, detail="El supermercado no existe")