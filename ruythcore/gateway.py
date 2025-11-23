import asyncio, json
import websockets
from .constants import GATEWAY_URL, OP_HEARTBEAT, OP_IDENTIFY, OP_HEARTBEAT_ACK, OP_RECONNECT, OP_INVALID_SESSION

class Gateway:
    def __init__(self, token, intents, dispatch):
        self.token = token
        self.intents = intents
        self.dispatch = dispatch
        self.ws = None
        self.heartbeat_interval = None
        self.seq = None
        self.session_id = None
        self._task = None
        self._closing = False

    async def connect(self):
        backoff = 1
        while not self._closing:
            try:
                self.ws = await websockets.connect(GATEWAY_URL)
                hello = json.loads(await self.ws.recv())
                self.heartbeat_interval = hello["d"]["heartbeat_interval"] / 1000.0
                await self.identify()
                # start heartbeat + listen
                hb = asyncio.create_task(self._heartbeat_loop())
                listen = asyncio.create_task(self._listen_loop())
                await asyncio.wait([hb, listen], return_when=asyncio.FIRST_EXCEPTION)
            except Exception as e:
                print("[Gateway] connection error:", e)
                await asyncio.sleep(backoff)
                backoff = min(backoff * 2, 60)
            finally:
                try:
                    if self.ws:
                        await self.ws.close()
                except:
                    pass
                await asyncio.sleep(1)

    async def identify(self):
        payload = {
            "op": OP_IDENTIFY,
            "d": {
                "token": self.token,
                "intents": self.intents,
                "properties": {"$os":"linux","$browser":"ruythcore","$device":"ruythcore"}
            }
        }
        await self.ws.send(json.dumps(payload))

    async def _heartbeat_loop(self):
        try:
            while True:
                await asyncio.sleep(self.heartbeat_interval)
                await self.ws.send(json.dumps({"op": OP_HEARTBEAT, "d": self.seq}))
        except Exception as e:
            # stop heartbeat on error
            pass

    async def _listen_loop(self):
        async for raw in self.ws:
            try:
                data = json.loads(raw)
            except:
                continue
            op = data.get("op")
            t = data.get("t")
            d = data.get("d")
            if data.get("s") is not None:
                self.seq = data["s"]
            if op == OP_HEARTBEAT_ACK:
                continue
            if op == OP_RECONNECT:
                raise Exception("Gateway requested reconnect")
            if op == OP_INVALID_SESSION:
                await asyncio.sleep(2)
                await self.identify()
                continue
            if t:
                # dispatch events to client
                await self.dispatch(t, d)
