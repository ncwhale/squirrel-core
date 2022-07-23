from datetime import datetime
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from ..hooks import pm
from ..templates import templates
from .schema import GrabRequest
from .flow import AddGrabRequest

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def input_view(request: Request):
    # It's a simple form for manual input grab request.
    # TODO: Add a form for manual input grab request.
    return templates.TemplateResponse("collector/input.html", {"request": request})

@router.post("/")
async def add_task(task: GrabRequest):
    result = await AddGrabRequest(task)
    return {"result": result, "timestamp": datetime.now()}

pm.hook.CollectorRouterInit(router=router)