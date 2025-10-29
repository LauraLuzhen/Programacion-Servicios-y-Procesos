# Laura Luzhen Rodríguez Morán

from http.client import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
from director import Director, directors_list

app = FastAPI()

class Pelicula(BaseModel):
    id: int
    titulo: str
    duracion: float
    idDirector: int

peliculas_list = [
    Pelicula(id=1, titulo="La bella y la bestia", duracion=120.2, idDirector=2),
    Pelicula(id=2, titulo="Cenicienta", duracion=90.3, idDirector=1),
    Pelicula(id=3, titulo="La princesa y el sapo", duracion=93.1, idDirector=4)
]

# GET
# Todas las películas
@app.get("/peliculas")
def peliculas():
    return peliculas_list
# Función para buscar la película por id
def search_pelicula(id: int):
    peliculas = [pelicula for pelicula in peliculas_list if pelicula.id == id]

    if len(peliculas) != 0:
        return peliculas
    raise HTTPException(status_code=404, detail="Película no encontrada")
# Por el id
@app.get("/peliculas/{id}")
def pelicula_id(id: int):
    return search_pelicula(id)
# Por query id
@app.get("/peliculas/")
def pelicula_query(id: int):
    return search_pelicula(id)


# POST
# Conseguimos el próximo id
def next_id():
    return (max(peliculas_list, key=id).id+1)
# Realizamos el post
@app.post("/peliculas", status_code=201, response_model=Pelicula)
def add_director(pelicula: Pelicula):
    pelicula.id = next_id()

    director_ids = [director.id for director in directors_list]

    if pelicula.idDirector not in director_ids:
        raise HTTPException(status_code=500, detail="El id del director no se ha encontrado")
    else:
        peliculas_list.append(pelicula)
        return pelicula


# PUT
@app.put("/peliculas/{id}", response_model=Pelicula)
def modify_pelicula(id: int, pelicula: Pelicula):
    for index, saved_pelicula in enumerate(peliculas_list):
        if saved_pelicula.id == id:
            saved_pelicula.id = id
            director_ids = [director.id for director in directors_list]

            if pelicula.idDirector not in director_ids:
                raise HTTPException(status_code=500, detail="El id del director no se ha encontrado")
            else:
                peliculas_list[index] = pelicula
                return pelicula

    raise HTTPException(status_code=404, detail="Película no encontrada")


# DELETE
@app.delete("/peliculas/{id}")
def delete_pelicula(id: int):
    for saved_pelicula in peliculas_list:
        if saved_pelicula.id == id:
            peliculas_list.remove(saved_pelicula)
            return {}
    raise HTTPException(status_code=404, detail="Película no encontrada")