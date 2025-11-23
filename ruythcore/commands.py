from functools import wraps

class CommandManager:
    def __init__(self):
        self.commands = {}

    def command(self, name=None):
        def decorator(func):
            cmd_name = name or func.__name__
            # store the coroutine function
            self.commands[cmd_name] = func
            @wraps(func)
            async def wrapper(ctx, *args, **kwargs):
                return await func(ctx, *args, **kwargs)
            return wrapper
        return decorator

    async def run(self, client, msg):
        prefix = getattr(client, "prefix", "!")
        content = getattr(msg, "content", "")
        if not content.startswith(prefix):
            return
        parts = content[len(prefix):].strip().split()
        if not parts:
            return
        name = parts[0]
        args = parts[1:]
        cmd = self.commands.get(name)
        if cmd:
            ctx = client.create_context(msg)
            try:
                await cmd(ctx, *args)
            except Exception as e:
                await client.events.emit("error", e)
                  
