from fastapi import APIRouter, Response, Depends
from app.auth.services.jwt import JwtService
from fastapi.security import HTTPAuthorizationCredentials

auth_router = APIRouter()


@auth_router.post("/refresh")
async def refresh_token(
    response: HTTPAuthorizationCredentials = 
    Depends(JwtService().generate_refresh_token)
):
    return response


@auth_router.post("/verify")
async def verify_token(response: HTTPAuthorizationCredentials = 
    Depends(JwtService().verify_token)):
    return Response(status_code=200)





# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ1OTk2NTMsInN1YiI6ImVtYWlscyJ9.lIXo9IdNlqIPWEht2uCQBGAXo1qODRvucvOamzn-xpg