from typing import Any
from pydantic import BaseModel

class AllMessageFormat(BaseModel):
    message: str
    data: Any = None