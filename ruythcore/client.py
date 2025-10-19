import asyncio
from .http import HTTPClient
from .gateway import Gateway
from .command import PrefixCommandManager
from .slash import SlashManager
from .constants import DEFAULT_INTENTS

class RuythBot:
    def __init__(self, token, prefix="!", intents=None):
        self.token = token
        self.prefix = prefix
        self.intents = intents or DEFAULT_INTENTS

        self.http = HTTPClient(token)
        self.gateway = Gateway(token, self.intents, self._dispatch)
        self.prefix_manager = PrefixCommandManager(self)
        self.slash = SlashManager(self)
        self._events = {}

    def command(self, name):
        return self.prefix_manager.command(name)

    def slash(self, name, description=""):
        return self.slash.slash(name, description)

    def event(self, fn):
        self._events[fn.__name__] = fn
        return fn

    async def _dispatch(self, ev_name, data):
        if ev_name == "on_ready":
            await self.slash.register_global_commands()
        if ev_name == "on_message":
            await self.prefix_manager.handle_message(data)
        if ev_name == "on_interaction":
            name = data.get("data", {}).get("name")
            if name in self.slash.commands:
                await self.slash.commands[name](data)
        if ev_name in self._events:
            await self._events[ev_name](data)

    async def start(self):
        await self.gateway.connect()

    def launch(self):
        asyncio.run(self.start())

    run = launch
            
