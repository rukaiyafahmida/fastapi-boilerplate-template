from core.exceptions import CustomException


class PasswordDoesNotMatchException(CustomException):
    code = 401
    error_code = "USER_PASSWORD_DOES_NOT_MATCH"
    message = "password does not match"

class PasswordNotValidException(CustomException):
    code = 400
    error_code = "PASSWORD_DO_NOT_FOLLOW_CRITERIA"
    message = "Password does not follow our protocol.Make sure the password contains at least 8 characters, uppercase, lowercase, special characters, numbers and has no spaces."


class DuplicateEmailException(CustomException):
    code = 400
    error_code = "USER_DUPLICATE_EMAIL"
    message = "duplicate email"


class UserNotFoundException(CustomException):
    code = 404
    error_code = "USER_NOT_FOUND"
    message = "user not found"



class NotPermittedException(CustomException):
    code = 403
    error_code = "NOT_PERMITTED"
    message = "Do not have privilege to perform this action"

