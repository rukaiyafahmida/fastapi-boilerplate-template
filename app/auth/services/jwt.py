from app.auth.schemas.jwt import RefreshTokenSchema
from core.exceptions.token import DecodeTokenException
from core.utils.token_helper import TokenHelper
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from core.exceptions import InvalidAuthException, UserNotFoundException, DecodeTokenException
from fastapi import Depends


security = HTTPBearer()


class JwtService:
    def verify_token(self, 
    authorization: HTTPAuthorizationCredentials = Depends(security)) -> None:
        TokenHelper().validate_refresh_token(token=authorization.credentials)

    def generate_refresh_token(self,
    authorization: HTTPAuthorizationCredentials = Depends(security)
    ):
        token = TokenHelper.decode(token=authorization.credentials)
        user_email = token.get("sub")
        token_response = TokenHelper().generate_token_response(user_email)
        return token_response
