import aiohttp
import asyncio
import json
from .constants import GATEWAY_URL

class Gateway:
    def __init__(self, token: str, intents: int, event_callback):
        self.token = token
        self.intents = intents
        self.event_callback = event_callback
        self.ws = None
        self.heartbeat_interval = None
        self.last_seq = None
        self.session = None

    async def connect(self):
        self.session = aiohttp.ClientSession()
        async with self.session.ws_connect(GATEWAY_URL) as ws:
            self.ws = ws
            async for msg in ws:
                if msg.type != aiohttp.WSMsgType.TEXT:
                    continue
                payload = json.loads(msg.data)
                op = payload.get("op")
                t = payload.get("t")
                d = payload.get("d")
                # handle Hello
                if op == 10:
                    self.heartbeat_interval = d.get("heartbeat_interval") / 1000.0
                    await self.identify()
                    asyncio.create_task(self._heartbeat_loop())
                # dispatch events
                if t == "READY":
                    await self.event_callback("on_ready", d)
                if t == "MESSAGE_CREATE":
                    await self.event_callback("on_message", d)
                if t == "INTERACTION_CREATE":
                    await self.event_callback("on_interaction", d)

    async def identify(self):
        payload = {
            "op": 2,
            "d": {
                "token": self.token,
                "intents": self.intents,
                "properties": {"$os": "linux", "$browser": "ruythcore", "$device": "ruythcore"}
            }
        }
        await self.ws.send_json(payload)

    async def _heartbeat_loop(self):
        while True:
            await asyncio.sleep(self.heartbeat_interval or 10)
            try:
                await self.ws.send_json({"op": 1, "d": self.last_seq})
            except Exception:
                break

    async def close(self):
        if self.session:
            await self.session.close()
        
