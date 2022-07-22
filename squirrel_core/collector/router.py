from datetime import datetime
from fastapi import APIRouter
from ..hooks import pm
from .schema import GrabRequest
from .flow import AddGrabRequest

router = APIRouter()

@router.get("/")
async def input_view():
    # It's a simple form for manual input grab request.
    # TODO: Add a form for manual input grab request.
    return "Hello World!"

@router.post("/")
async def add_task(task: GrabRequest):
    result = await AddGrabRequest(task)
    return {"result": result, "timestamp": datetime.now()}

pm.hook.CollectorRouterInit(router=router)