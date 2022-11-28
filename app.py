import utils
import asyncio
from fastapi import FastAPI

from routers import google, imagemanip


class RandomAPI(FastAPI):
    def __init__(self, *, loop: asyncio.AbstractEventLoop | None = None):
        self.loop: asyncio.AbstractEventLoop = loop or asyncio.get_event_loop_policy().get_event_loop()
        super().__init__(
            title="RandomAPI",
            version="0.0.1",
            description="Some random API",
            loop=self.loop,
            redoc_url="/docs",
            docs_url=None,
            on_startup=[utils.on_start_up],
            on_shutdown=[utils.on_shutdown],
        )

app = RandomAPI()
app.include_router(google.router)
app.include_router(imagemanip.router)
