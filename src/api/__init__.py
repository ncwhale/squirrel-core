__version__ = '0.1.0'

# from quart import Quart, request, jsonify, render_template

from datetime import datetime

# app = Quart(__name__)
from fastapi import FastAPI, Request, Body

app = FastAPI()

@app.post("/echo")
async def echo(data: dict = Body()):
    return {"input": data, "timestamp": str(datetime.now())}