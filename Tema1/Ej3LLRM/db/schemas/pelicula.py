def pelicula_schema(pelicula) -> dict:
    return {
        "id": str(pelicula["_id"]),
        "titulo": pelicula["titulo"],
        "duracion": pelicula["duracion"],
        "idDirector": pelicula["idDirector"]
        }

def peliculas_schema(peliculas) -> list:
    return [pelicula_schema(pelicula) for  pelicula in peliculas]