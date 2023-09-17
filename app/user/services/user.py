from typing import Optional, List
from sqlalchemy import or_, select, and_
from sqlalchemy.orm import Session
from app.user.models import User
from app.user.schemas import LoginResponseSchema, ReadUserSchema
from core.db import session
from core.exceptions import (
    PasswordDoesNotMatchException,
    DuplicateEmailException,
    UserNotFoundException,
    PasswordNotValidException,
)
from core.utils.token_helper import TokenHelper
from app.user.services.password_helper import PasswordHelper
from fastapi.responses import JSONResponse

class UserService:
    def __init__(self):
        ...


    async def create_user(
        self, email: str, password: str, retype_password: str, name: str, session: Session
    ):
        result = session.query(User).filter(User.email == email)
        is_exist = result.first()
        if is_exist:
            raise DuplicateEmailException

        if password != retype_password:
            raise PasswordDoesNotMatchException
        
        if not PasswordHelper.validate_password(password):
            raise PasswordNotValidException
        
        encrypted_password = PasswordHelper.bcrypt(password)
        
        
        user = User(email=email, password=encrypted_password, name=name)
        session.add(user)
        session.commit()
        session.refresh(user)
        return ReadUserSchema.from_orm(user)


    async def is_admin(self, user_id: int) -> bool:
        result = session.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if not user:
            return False

        if user.is_admin is False:
            return False

        return True

    async def login(self, email: str, password: str,  session: Session) -> LoginResponseSchema:
        result = session.execute(
            select(User).where(and_(User.email == email, password == password))
        )
        user = result.scalars().first()
        if not user:
            raise UserNotFoundException
        
        tokens = TokenHelper().generate_token_response(user_email=user.email)
        response = LoginResponseSchema(**tokens)
        return response
