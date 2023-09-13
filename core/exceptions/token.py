from core.exceptions import CustomException


class DecodeTokenException(CustomException):
    code = 400
    error_code = "TOKEN__DECODE_ERROR"
    message = "token decode error"


class ExpiredTokenException(CustomException):
    code = 401
    error_code = "TOKEN__EXPIRE_TOKEN"
    message = "Token expired"

class InvalidAuthException(CustomException):
    code = 400
    error_code = "INVALID_AUTHENTICATION_SCHEME"
    message = "Invalid authentication scheme"


class TokenValidationException(CustomException):
    code = 401
    error_code = "COULD_NOT_VALIDATE"
    message = "Could not validate credentials"
