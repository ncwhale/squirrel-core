from ..hooks import hookspec
from .schema import GrabRequest

class CollectorHookspec:
    @hookspec
    def RequestParse(self, request: GrabRequest) -> dict:
        pass