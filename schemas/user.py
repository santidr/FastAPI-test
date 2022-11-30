from models.user import User

def userEntity(user: User) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]