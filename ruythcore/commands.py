from functools import wraps

class CommandManager:
    def __init__(self):
        self.commands = {}

    def command(self, name=None):
        def decorator(func):
            cmd_name = name or func.__name__
            self.commands[cmd_name] = func
            @wraps(func)
            async def wrapper(*args, **kwargs):
                return await func(*args, **kwargs)
            return wrapper
        return decorator

    async def run(self, client, msg):
        if not getattr(msg, "content", "").startswith("!"):
            return
        parts = msg.content[1:].split()
        name = parts[0]
        args = parts[1:]
        if name in self.commands:
            ctx = client.create_context(msg)
            await self.commands[name](ctx)
            
