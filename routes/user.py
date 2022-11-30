from fastapi import APIRouter, HTTPException, Response, status
from config.db import db
from schemas.user import userEntity, usersEntity
from models.user import User, UpdateUser
from passlib.hash import sha256_crypt
from bson import ObjectId

user = APIRouter()

@user.post('/user/new', tags=['users'])
def create_new_user(user: User):
    new_user = dict(user)
    new_user['password'] = sha256_crypt.hash(new_user['password'])

    id = db['users'].insert_one(new_user).inserted_id
    found_user = db['users'].find_one({'_id': id })

    return userEntity(found_user)

@user.get('/users', tags=['users'])
def get_all_users():
    users = db['users'].find()

    return usersEntity(users)

@user.get('/users/{user_id}', tags=['users'])
def get_user_by_id(user_id: str):
    try:
        found_user = db['users'].find_one({'_id': ObjectId(user_id)})
    except Exception:
        raise HTTPException(status_code=500, detail=f'{user_id} is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string.')

    return userEntity(found_user)

@user.put('/users/edit/{user_id}', tags=['users'])
def update_user(user_id: str, user: UpdateUser):
    db['users'].find_one_and_update({'_id': ObjectId(user_id)}, {'$set': dict(user)})

    updated_user = db['users'].find_one({'_id': ObjectId(user_id)})

    return userEntity(updated_user)

@user.delete('/users/delete/{user_id}', tags=['users'])
def delete_user(user_id: str):
    try:
        deleted_user = db['users'].find_one_and_delete({'_id': ObjectId(user_id)})

        if not deleted_user:
            return HTTPException(status_code=404, detail=f'User does not exist to delete.')

    except Exception:
        raise HTTPException(status_code=500, detail=f'{user_id} is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string.')

    return Response({"msg": "user deleted successfully."}, status_code=status.HTTP_204_NO_CONTENT)