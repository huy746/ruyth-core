import asyncio
import websockets
import json

class Gateway:
    def __init__(self, token, intents, event_dispatcher):
        self.token = token
        self.intents = intents
        self.event_dispatcher = event_dispatcher
        self.url = "wss://gateway.discord.gg/?v=10&encoding=json"

    async def connect(self):
        async with websockets.connect(self.url) as ws:
            await self._identify(ws)
            await self._listen(ws)

    async def _identify(self, ws):
        payload = {
            "op": 2,
            "d": {
                "token": self.token,
                "intents": self.intents,
                "properties": {
                    "$os": "linux",
                    "$browser": "python",
                    "$device": "python"
                }
            }
        }
        await ws.send(json.dumps(payload))

    async def _listen(self, ws):
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            op = data.get("op")
            if op == 0:
                event_name = data.get("t")
                await self.event_dispatcher(event_name, data)
          
