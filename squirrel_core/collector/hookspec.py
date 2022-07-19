from ..hooks import hookspec

class CollectorHookspec:
    @hookspec
    def RequestParse(self, request: dict) -> dict:
        pass