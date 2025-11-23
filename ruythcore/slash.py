from functools import wraps

class SlashCommandManager:
    def __init__(self):
        self.slashes = {}

    def slash(self, name=None, description=None):
        def decorator(func):
            cmd_name = name or func.__name__
            self.slashes[cmd_name] = func
            @wraps(func)
            async def wrapper(ctx, *args, **kwargs):
                return await func(ctx, *args, **kwargs)
            return wrapper
        return decorator

    async def handle(self, client, interaction):
        data = interaction.get("data", {})
        name = data.get("name")
        if not name:
            return
        handler = self.slashes.get(name)
        if handler:
            ctx = client.create_context(interaction, slash=True)
            try:
                await handler(ctx)
            except Exception as e:
                await client.events.emit("error", e)
