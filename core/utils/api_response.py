from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from core.fastapi.schema.response import AllMessageFormat

def format_response(data, message: str, code: Optional[int] = 200):
    return JSONResponse(status_code=code, content=jsonable_encoder(AllMessageFormat(message=message, data=data)))
