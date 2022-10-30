from datetime import datetime
from fastapi import Body, APIRouter

router = APIRouter()

@router.put("/", tags=["echo"])
@router.post("/", tags=["echo"])
@router.patch("/", tags=["echo"])
async def echo(data: dict = Body()):
    return {"input": data, "timestamp": str(datetime.now())}
