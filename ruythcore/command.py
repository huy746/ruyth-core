from .context import Context

class PrefixCommandManager:
    def __init__(self, bot):
        self.bot = bot
        self.commands = {}

    def command(self, name):
        def decorator(func):
            self.commands[name] = func
            return func
        return decorator

    async def handle_message(self, raw_event):
        content = raw_event.get("content", "")
        if content.startswith(self.bot.prefix):
            body = content[len(self.bot.prefix):].strip()
            if not body: return
            parts = body.split()
            cmd = parts[0]
            args = parts[1:]
            if cmd in self.commands:
                ctx = Context(self.bot, raw_event)
                await self.commands[cmd](ctx, *args)
            
