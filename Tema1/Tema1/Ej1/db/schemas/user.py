def user_schema(user) -> dict:
    """Convierte un documento de MongoDB en un diccionario compatible con User"""
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "surname": user["surname"],
        "age": user["age"]
    }

def users_schema(users) -> list:
    """Convierte una lista de documentos de MongoDB en una lista de diccionarios User"""
    return [user_schema(user) for user in users]
