from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, Any
from pydantic import BaseModel

class AllMessageFormat(BaseModel):
    message: str
    data: Any = None

def format_response(data, message: str, code: Optional[int] = 200):
    return JSONResponse(status_code=code, content=jsonable_encoder(AllMessageFormat(message=message, data=data)))
