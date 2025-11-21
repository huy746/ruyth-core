import asyncio, json, websockets
from .constants import GATEWAY_URL, OP_HEARTBEAT, OP_IDENTIFY

class Gateway:
    def __init__(self, token, intents, dispatch):
        self.token = token
        self.intents = intents
        self.dispatch = dispatch
        self.ws = None
        self.heartbeat_interval = 0
        self.seq = None

    async def connect(self):
        self.ws = await websockets.connect(GATEWAY_URL)
        hello = json.loads(await self.ws.recv())
        self.heartbeat_interval = hello['d']['heartbeat_interval'] / 1000
        await self.identify()
        asyncio.create_task(self.heartbeat())
        asyncio.create_task(self.listen())

    async def identify(self):
        await self.ws.send(json.dumps({
            'op': OP_IDENTIFY,
            'd': {
                'token': self.token,
                'intents': self.intents,
                'properties': {'$os':'linux','$browser':'ruythcore','$device':'ruythcore'}
            }
        }))

    async def heartbeat(self):
        while True:
            await asyncio.sleep(self.heartbeat_interval)
            await self.ws.send(json.dumps({'op': OP_HEARTBEAT,'d':self.seq}))

    async def listen(self):
        async for msg in self.ws:
            data = json.loads(msg)
            if data.get('s'):
                self.seq = data['s']
            if data.get('t'):
                await self.dispatch(data['t'], data['d'])
