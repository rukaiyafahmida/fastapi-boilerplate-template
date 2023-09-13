from typing import Optional, List
from sqlalchemy import or_, select, and_
from sqlalchemy.orm import Session
from app.user.models import User
from app.user.schemas import LoginResponseSchema, ReadUserSchema
from core.db import get_db
from core.exceptions import (
    PasswordDoesNotMatchException,
    DuplicateEmailOrNicknameException,
    UserNotFoundException,
)
from core.utils.token_helper import TokenHelper
from app.user.services.password_helper import PasswordHelper
from fastapi.responses import JSONResponse

class UserService:
    def __init__(self, ):
        ...


    async def create_user(
        self, email: str, password1: str, password2: str, name: str, session: Session
    ) -> None:
        if password1 != password2:
            raise PasswordDoesNotMatchException
        if not PasswordHelper.validate_password(password1):
            return JSONResponse(
                content="Password does not follow our protocol. Make sure the password contains at least 8 characters, uppercase, lowercase, special characters, numbers and has no spaces.",
                code=400
            )
        encrypted_password = PasswordHelper.bcrypt(password1)
        
        query = select(User).where(or_(User.email == email, User.name == name))
        result = await session.execute(query)
        is_exist = result.scalars().first()
        if is_exist:
            raise DuplicateEmailOrNicknameException

        user = User(email=email, password=encrypted_password, name=name)
        session.add(user)
        session.commit()
        session.refresh(user)
        return ReadUserSchema.from_orm(user)


    # async def is_admin(self, user_id: int) -> bool:
    #     result = await session.execute(select(User).where(User.id == user_id))
    #     user = result.scalars().first()
    #     if not user:
    #         return False

    #     if user.is_admin is False:
    #         return False

    #     return True

    # async def login(self, email: str, password: str) -> LoginResponseSchema:
    #     result = await session.execute(
    #         select(User).where(and_(User.email == email, password == password))
    #     )
    #     user = result.scalars().first()
    #     if not user:
    #         raise UserNotFoundException

    #     response = LoginResponseSchema(
    #         token=TokenHelper.encode(payload={"user_id": user.id}),
    #         refresh_token=TokenHelper.encode(payload={"sub": "refresh"}),
    #     )
    #     return response
