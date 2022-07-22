from ..hooks import pm
from .schema import GrabRequest


async def AddGrabRequest(req: GrabRequest) -> list | dict | None:
    results = pm.hook.RequestParse(request=req)
    # TODO: Send results to Despatcher
    return results
