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

    def event(self, name=None):
        return self.events.on(name or "ready")

    def start(self):
        # create and run main event loop safely
        asyncio.run(self.gateway.connect())

    async def _dispatch(self, event, data):
        if event == "MESSAGE_CREATE":
            # safe extraction
            author = User(id=str(data.get("author",{}).get("id","")), username=data.get("author",{}).get("username",""))
            msg = Message(id=str(data.get("id","")), channel_id=str(data.get("channel_id","")), content=data.get("content",""), author=author, raw=data)
            await self.cmd.run(self, msg)
            await self.events.emit("message", msg)
        elif event == "INTERACTION_CREATE":
            # Discord interaction event for slash commands
            await self.slash.handle(self, data)
        elif event == "READY":
            await self.events.emit("ready", data)
