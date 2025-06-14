from uuid import UUID
from fastapi import APIRouter, HTTPException
from database import users
from schemas.user import Response, User, UserCreate
from services.user_service import user_service

router = APIRouter()


@router.get("")
def get_users():
    return users

@router.get("/{user_id}")
def get_user_by_id(id: str):
    user = user_service.get_user_by_id(id)
    if not users:
        raise HTTPException(status_code=404, detail="User Not found")
    return user


@router.post("")
def create_user(user_in: UserCreate):
    user = user_service.create_user(user_in)
    return Response(message="User added successfully", data=user)


@router.put("/{user_id}")
def update_user(user_id: str, updated_user: User):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User Not found")
    users[user_id] = updated_user
    return updated_user


@router.delete("/{user_id}")
def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User Not found")
    del users[user_id]

@router.patch("/{user_id}")
def deactivate_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User Not found")
    user = users[user_id]
    user.is_active = False
    users[user_id] = user
    return user

