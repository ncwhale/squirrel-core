from fastapi import FastAPI
from .api import router as api_router
from .collector import router as collector_router

app = FastAPI()

app.include_router(api_router, prefix="/api")
app.include_router(collector_router, prefix="/collector")