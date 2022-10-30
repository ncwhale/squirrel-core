# from imp import _FileLike
from pydantic import BaseModel
from typing import Optional

class GrabRequest(BaseModel):
    url: str
    method: str = "GET"
    headers: Optional[dict] = None
    body: Optional[dict] = None
    cookies: Optional[dict] = None
    metadata: Optional[dict] = None

class Resource(BaseModel):
    metadata: Optional[dict] = None
    blob: Optional[bytes] = None