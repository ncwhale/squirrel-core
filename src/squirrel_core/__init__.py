__version__ = '0.1.0'

from api import app as api_app

def run() -> None:
    api_app.run()