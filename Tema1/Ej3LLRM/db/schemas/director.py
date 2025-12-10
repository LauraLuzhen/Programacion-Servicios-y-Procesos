def director_schema(director) -> dict:
    return {
        "id": str(director["_id"]),
        "dni": director["dni"],
        "nombre": director["nombre"],
        "apellidos": director["apellidos"],
        "nacionalidad": director["nacionalidad"]
        }

def directors_schema(directors) -> list:
    return [director_schema(director) for  director in directors]