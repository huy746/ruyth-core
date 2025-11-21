import asyncio
from .gateway import Gateway
from .http import HTTPClient
from .commands import CommandManager
from .slash import SlashCommandManager
from .events import EventHandler
from .context import Context
from .models import Message, User

class Client:
    def __init__(self, token, intents=0):
        self.token = token
        self.intents = intents
        self.http = HTTPClient(token)
        self.cmd = CommandManager()
        self.slash = SlashCommandManager()
        self.events = EventHandler()
        self.gateway = Gateway(token, intents, self._dispatch)
        self.prefix = "!"

    def create_context(self, msg):
        return Context(self, msg)

    def command(self, name=None):
        return self.cmd.command(name)

    def slash_command(self, name=None, description=None):
        return self.slash.slash(name, description)

    def event(self, name=None):
        return self.events.on(name or "ready")

    def start(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.gateway.connect())
        loop.run_forever()

    async def _dispatch(self, event, data):
        if event=="MESSAGE_CREATE":
            author = User(id=data['author']['id'], username=data['author'].get('username',''))
            msg = Message(id=data['id'], channel_id=data['channel_id'], content=data.get('content',''), author=author, raw=data)
            await self.cmd.run(self, msg)
            await self.events.emit("message", msg)
