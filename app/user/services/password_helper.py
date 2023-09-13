from passlib.context import CryptContext
import secrets
from password_validator import PasswordValidator




pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordHelper:
    @staticmethod
    def bcrypt(password: str):
        "changes simple passwords to some hashed value to be stored in the database"
        return pwd_cxt.hash(password)
    
    @staticmethod
    def verify(hashed, normal):
        "verifies that the user-given password matches with password stored in the databse"
        "returns a boolean"
        return pwd_cxt.verify(normal, hashed)
    @staticmethod
    def generate_random_hash():
        return secrets.token_urlsafe(16)
    
    @staticmethod
    def validate_password(password):
        schema = PasswordValidator()

        schema.min(8).max(
            30
        ).has().uppercase().has().lowercase().has().digits().has().symbols().has().no().spaces()

        return schema.validate(password)

