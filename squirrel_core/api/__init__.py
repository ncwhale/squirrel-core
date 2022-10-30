__version__ = '0.1.0'

from fastapi import APIRouter

router = APIRouter()

from .echo import router as echo_router

router.include_router(echo_router, prefix="/echo")