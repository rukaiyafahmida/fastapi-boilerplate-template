from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from core.db import create_tables
from core.fastapi.logger import logger
from api import router
from core.exceptions import CustomException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from typing import List

load_dotenv()



def init_listeners(app_: FastAPI) -> None:
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )

def init_routers(app_: FastAPI) -> None:
    # app_.include_router(home_router)
    app_.include_router(router)

def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
    return middleware
def create_app() -> FastAPI:
    app_ = FastAPI(
        title="FastAPI Template",
        description="FastAPI Template API",
        version="1.0.0",
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    init_listeners(app_=app_)
    return app_


app = create_app()

try:
    create_tables()
except Exception as e:
    logger.error(f"Error creatinig tables. Error: {e}")

# app.add_exception_handler(JWTCustomError, jwt_custom_exception_handler)