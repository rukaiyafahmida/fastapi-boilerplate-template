from sqlalchemy import Column, Unicode, BigInteger, Boolean
from core.db import Base, TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(Unicode(255), nullable=False, unique=True)
    password = Column(Unicode(255), nullable=False)
    name = Column(Unicode(255), nullable=False)
    is_admin = Column(Boolean, nullable = True)
