from uuid import UUID

from fastapi import HTTPException

from schemas.user import User, UserCreate

from database import users


class UserService:


    @staticmethod
    def create_user(user_in: UserCreate):
        for user in users.values():
            if user.email == user_in.email:
                raise HTTPException(status_code=400, detail=" User with email already exists")
        user = User(
            id=str(UUID(int=len(users) + 1)),
            **user_in.model_dump(),
        )
        users[user.id] = user
        return user
    

    @staticmethod
    def get_user_by_id(user_id):
        user = users.get(str(user_id))
        if not users:
            return None
        return user
    

    @staticmethod
    def delete_user(user_id: UUID):
        user = users.get(str(user_id))
        if not user:
            return None

        del users[user.id]
        return True
 

user_service = UserService()