# client.py

import asyncio
from .http import HTTPClient
from .gateway import Gateway
from .command import PrefixCommandManager
from .slash import SlashManager
from .voice import VoiceManager
from .utils import ensure_task
from .constants import DEFAULT_INTENTS

class Client:
    def __init__(self, token: str, prefix: str = "!"):
        self.token = token
        self.prefix = prefix
        self.http = HTTPClient(token)
        self.gateway = Gateway(token, DEFAULT_INTENTS, self._dispatch)
        self.commands = PrefixCommandManager(self)
        self.slash = SlashManager(self)
        self.voice = VoiceManager(self)
        self._events = {}
        self.user = None

    # decorators
    def command(self, name: str = None):
        return self.commands.command(name)

    def slash_command(self, name: str, description: str = ""):
        return self.slash.command(name, description)

    def event(self, fn):
        self._events[fn.__name__] = fn
        return fn

    async def _dispatch(self, ev_name, data):
        if ev_name == "on_ready":
            try:
                self.user = data.get("user") or data.get("user", {})
            except Exception:
                pass
            try:
                await self.slash.register_global_commands()
            except Exception:
                pass

        if ev_name == "on_message":
            await self.commands.handle_message(data)

        if ev_name == "on_interaction":
            await self.slash.handle_interaction(data)

        if ev_name in self._events:
            await self._events[ev_name](data)

    async def start(self):
        await self.gateway.connect()

    def run(self):
        """An toàn cho mọi môi trường asyncio"""
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            # Nếu đang có loop, tạo task
            asyncio.ensure_future(self.start())
        else:
            # Nếu không có loop, chạy bình thường
            asyncio.run(self.start())


class RuythCore(Client):
    """Alias class name for branding"""
    pass
