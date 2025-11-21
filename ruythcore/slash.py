from functools import wraps

class SlashCommandManager:
    def __init__(self):
        self.slashes = {}

    def slash(self, name=None, description=None):
        def decorator(func):
            cmd_name = name or func.__name__
            self.slashes[cmd_name] = func
            @wraps(func)
            async def wrapper(*args, **kwargs):
                return await func(*args, **kwargs)
            return wrapper
        return decorator

    async def handle(self, client, data):
        name = data.get("data", {}).get("name")
        if name in self.slashes:
            await self.slashes[name](client.create_context(data))
