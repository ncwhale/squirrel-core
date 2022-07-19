from pydantic import BaseModel

class GrabRequest(BaseModel):
    url: str
    method: str
    headers: dict
    cookies: dict
    metadata: dict
