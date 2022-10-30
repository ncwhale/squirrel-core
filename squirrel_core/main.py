import trio
from hypercorn.config import Config
from hypercorn.trio import serve

from .app import app

# Event for shutdown serivce.
trigger_shutdown = trio.Event()


async def async_run():
    config = Config()
    config.bind = ["localhost:8080"]

    await serve(app, config=config, shutdown_trigger=trigger_shutdown.wait)


def run():
    trio.run(async_run)


if __name__ == '__main__':
    run()
