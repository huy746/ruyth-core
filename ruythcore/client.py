import asyncio

from .gateway import Gateway
from .http import HTTPClient
from .commands import CommandManager
from .slash import SlashCommandManager
from .events import EventHandler
from .context import Context
from .models import Message, User


class Client:
    def __init__(self, token, intents=0, prefix="!"):
        self.token = token
        self.intents = intents
        self.prefix = prefix
        self.http = HTTPClient(token)
        self.cmd = CommandManager()
        self.slash = SlashCommandManager()
        self.events = EventHandler()
        self.gateway = Gateway(token, intents, self._dispatch)

    def create_context(self, raw, slash=False):
        return Context(self, raw, slash)

    def command(self, name=None):
        return self.cmd.command(name)

    def slash_command(self, name=None, description=None):
        return self.slash.slash(name, description)

    def event(self, func=None, name=None):
        def decorator(handler):
            event_name = name or self._event_name_from_handler(handler)
            return self.events.on(event_name)(handler)

        if callable(func):
            return decorator(func)
        return decorator

    def run(self):
        self.start()

    def start(self):
        asyncio.run(self.gateway.connect())

    async def close(self):
        await self.gateway.close()
        await self.http.close()

    @staticmethod
    def _event_name_from_handler(handler):
        name = getattr(handler, "__name__", "ready")
        return name[3:] if name.startswith("on_") else name

    async def _dispatch(self, event, data):
        if event == "MESSAGE_CREATE":
            author_data = data.get("author", {})
            author = User(
                id=str(author_data.get("id", "")),
                username=author_data.get("username", ""),
                discriminator=author_data.get("discriminator", "0000"),
                bot=author_data.get("bot", False),
            )
            msg = Message(
                id=str(data.get("id", "")),
                channel_id=str(data.get("channel_id", "")),
                content=data.get("content", ""),
                author=author,
                raw=data,
            )
            await self.cmd.run(self, msg)
            await self.events.emit("message", msg)
        elif event == "INTERACTION_CREATE":
            await self.slash.handle(self, data)
        elif event == "READY":
            await self.events.emit("ready", data)
