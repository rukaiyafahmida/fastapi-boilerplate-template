from fastapi import APIRouter

from api.home.home import home_router
from api.user.v1.user import user_router
from api.auth.auth import auth_router

router = APIRouter()
router.include_router(home_router, prefix="/home", tags=["Home"])
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(user_router, prefix="/user", tags=["User"])


__all__ = ["router"]
