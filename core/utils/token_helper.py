from datetime import datetime, timedelta
import jwt
import os
from typing import Union, Any
from core.exceptions import DecodeTokenException, ExpiredTokenException, UserNotFoundException
from dotenv import load_dotenv

load_dotenv()



JWT_SECRET_KEY = os.getenv("jwt_secret_key")
JWT_ALGORITHM = os.getenv("algorithm")
ACCESS_TOKEN_EXPIRES_IN_MINUTES = int(os.getenv("access_token_expires_in_minutes"))
REFRESH_TOKEN_EXPIRES_IN_MINUTES = int(os.getenv("refresh_token_expires_in_minutes"))


class TokenHelper:
    @staticmethod
    def encode(payload: dict, expire_period: int = 3600) -> str:
        token = jwt.encode(
            payload={
                **payload,
                "exp": datetime.utcnow() + timedelta(seconds=expire_period),
            },
            key = JWT_SECRET_KEY,
            algorithm = JWT_ALGORITHM,
        ).decode("utf8")
        return token
    
    @staticmethod
    def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(
                minutes=ACCESS_TOKEN_EXPIRES_IN_MINUTES
            )
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, JWT_ALGORITHM)
        return encoded_jwt

    @staticmethod
    def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(
                minutes=REFRESH_TOKEN_EXPIRES_IN_MINUTES
            )
        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, JWT_ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def generate_token_response(user_email: Union[str, Any]):
        return {'token' : TokenHelper().create_access_token(user_email), "refresh_token" : TokenHelper().create_refresh_token(user_email)}

    @staticmethod
    def decode(token: str) -> dict:
        try:
            return jwt.decode(
                token,
                JWT_SECRET_KEY,
                JWT_ALGORITHM,
            )
        except jwt.exceptions.DecodeError:
            raise DecodeTokenException
        except jwt.exceptions.ExpiredSignatureError:
            raise ExpiredTokenException
    
    @staticmethod
    def validate_refresh_token(token):
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            user_email: str = payload.get("sub")
            if user_email is None:
                raise UserNotFoundException

            if datetime.fromtimestamp(payload.get("exp")) < datetime.now():
                raise ExpiredTokenException
            return user_email
        except Exception:
            raise DecodeTokenException

    @staticmethod
    def decode_expired_token(token: str) -> dict:
        try:
            return jwt.decode(
                token,
                JWT_SECRET_KEY,
                JWT_ALGORITHM,
                options={"verify_exp": False},
            )
        except jwt.exceptions.DecodeError:
            raise DecodeTokenException