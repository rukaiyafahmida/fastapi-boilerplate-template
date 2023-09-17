from typing import List
from fastapi import APIRouter, Depends, Query
from api.user.v1.request.user import LoginRequest
from api.user.v1.response.user import LoginResponse
from app.user.schemas import (
    ExceptionResponseSchema,
    CreateUserRequestSchema,
    CreateUserResponseSchema,
)
from app.user.services import UserService
from core.fastapi.dependencies import (
    PermissionDependency,
    IsAdmin,
)
from core.db import get_db
from sqlalchemy.orm import Session


user_router = APIRouter()



@user_router.post(
    "/register",
    response_model=CreateUserResponseSchema,
    responses={"404": {"model": ExceptionResponseSchema}}
)
async def create_user(request: CreateUserRequestSchema, session : Session = Depends(get_db)):
    await UserService().create_user(**request.dict(), session=session)
    return {"email": request.email, "name": request.name}


@user_router.post(
    "/login",
    response_model=LoginResponse,
    responses={"404": {"model": ExceptionResponseSchema}},
)
async def login(request: LoginRequest, session : Session = Depends(get_db)):
    token = await UserService().login(email=request.email, password=request.password, session= session)
    return {"token": token.token, "refresh_token": token.refresh_token}
