from fastapi import APIRouter
from ..hooks import hookspec
from ..schema import GrabRequest


class CollectorHookspec:
    @hookspec
    def CollectorRouterInit(self, router: APIRouter):
        '''
        This hook is called when collector router is initialized.

        plugins can add routes to the router.
        '''

    @hookspec
    def RequestParse(self, request: GrabRequest) -> dict:
        '''
        Parse a request and return a dict.
        '''
