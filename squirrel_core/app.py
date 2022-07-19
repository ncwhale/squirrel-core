from fastapi import FastAPI
from .api import router as api_routes

app = FastAPI()

app.include_router(api_routes, prefix="/api")