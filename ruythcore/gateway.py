
import asyncio
import websockets
from .constants import GATEWAY_URL

class Gateway:
    def __init__(self, token, intents, dispatch):
        self.token = token
        self.intents = intents
        self._dispatch = dispatch
        self.ws = None

    async def connect(self):
        async with websockets.connect(GATEWAY_URL) as ws:
            self.ws = ws
            await self._run()

    async def _run(self):
        async for message in self.ws:
            # Fake dispatch
            await self._dispatch("on_ready", {"user": {"username": "RuythBot"}})
    
