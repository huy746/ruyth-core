import asyncio
import json
import importlib.util

from .constants import (
    GATEWAY_URL,
    OP_HEARTBEAT,
    OP_IDENTIFY,
    OP_HEARTBEAT_ACK,
    OP_RECONNECT,
    OP_INVALID_SESSION,
)
from .http import MissingDependencyError


class Gateway:
    def __init__(self, token, intents, dispatch):
        self.token = token
        self.intents = intents
        self.dispatch = dispatch
        self.ws = None
        self.heartbeat_interval = None
        self.seq = None
        self.session_id = None
        self._closing = False

    async def connect(self):
        if importlib.util.find_spec("websockets") is None:
            raise MissingDependencyError("websockets", "Discord gateway connections")
        import websockets

        backoff = 1
        while not self._closing:
            hb = None
            listen = None
            try:
                self.ws = await websockets.connect(GATEWAY_URL)
                hello = json.loads(await self.ws.recv())
                self.heartbeat_interval = hello["d"]["heartbeat_interval"] / 1000.0
                await self.identify()
                hb = asyncio.create_task(self._heartbeat_loop())
                listen = asyncio.create_task(self._listen_loop())
                done, pending = await asyncio.wait(
                    [hb, listen], return_when=asyncio.FIRST_EXCEPTION
                )
                for task in pending:
                    task.cancel()
                for task in done:
                    exc = task.exception()
                    if exc:
                        raise exc
            except asyncio.CancelledError:
                self._closing = True
                raise
            except Exception as e:
                print("[Gateway] connection error:", e)
                await asyncio.sleep(backoff)
                backoff = min(backoff * 2, 60)
            finally:
                for task in (hb, listen):
                    if task and not task.done():
                        task.cancel()
                if self.ws:
                    await self.ws.close()
                await asyncio.sleep(1)

    async def identify(self):
        if self.ws is None:
            raise RuntimeError("Gateway websocket is not connected")
        payload = {
            "op": OP_IDENTIFY,
            "d": {
                "token": self.token,
                "intents": self.intents,
                "properties": {
                    "$os": "linux",
                    "$browser": "ruythcore",
                    "$device": "ruythcore",
                },
            },
        }
        await self.ws.send(json.dumps(payload))

    async def close(self):
        self._closing = True
        if self.ws:
            await self.ws.close()

    async def _heartbeat_loop(self):
        while not self._closing:
            await asyncio.sleep(self.heartbeat_interval)
            await self.ws.send(json.dumps({"op": OP_HEARTBEAT, "d": self.seq}))

    async def _listen_loop(self):
        async for raw in self.ws:
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                continue
            op = data.get("op")
            t = data.get("t")
            d = data.get("d")
            if data.get("s") is not None:
                self.seq = data["s"]
            if op == OP_HEARTBEAT_ACK:
                continue
            if op == OP_RECONNECT:
                raise RuntimeError("Gateway requested reconnect")
            if op == OP_INVALID_SESSION:
                await asyncio.sleep(2)
                await self.identify()
                continue
            if t:
                await self.dispatch(t, d)
