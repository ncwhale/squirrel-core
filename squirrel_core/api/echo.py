from datetime import datetime
from fastapi import Body, APIRouter

router = APIRouter()

@router.put("/")
@router.post("/")
@router.patch("/")
async def echo(data: dict = Body()):
    return {"input": data, "timestamp": str(datetime.now())}
