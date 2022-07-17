__version__ = '0.1.0'

from quart import Quart, request, jsonify, render_template
from datetime import datetime

app = Quart(__name__)

def run() -> None:
    app.run()

@app.post("/echo")
async def echo():
    data = await request.get_json()
    return {"input": data, "timestamp": str(datetime.now())}