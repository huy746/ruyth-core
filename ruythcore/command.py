class PrefixCommandManager:
    def __init__(self, client):
        self.client = client
        self._commands = {}

    def command(self, name=None):
        def decorator(fn):
            self._commands[name or fn.__name__] = fn
            return fn
        return decorator

    async def handle_message(self, message):
        # Fake xử lý
        pass
        
