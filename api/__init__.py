from fastapi import APIRouter

from api.auth.auth import auth_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["Auth"])


__all__ = ["router"]
