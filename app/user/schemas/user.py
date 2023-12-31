from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    name : str

    

class CreateUserRequestSchema(UserBase):
    password : str
    retype_password : str


class ReadUserWEmailSchema(BaseModel):
    email: str


class ReadUserWIdSchema(BaseModel):
    id: int


class ReadUserSchema(UserBase):
    id : int
    class Config:
        orm_mode = True

class LoginResponseSchema(BaseModel):
    token : str
    refresh_token : str



class CreateUserResponseSchema(BaseModel):
    email: str
    name: str 

    class Config:
        orm_mode = True

