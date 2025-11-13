class SlashManager:
    def __init__(self, client):
        self.client = client
        self._commands = {}

    def command(self, name, description=""):
        def decorator(fn):
            self._commands[name] = fn
            return fn
        return decorator

    async def register_global_commands(self):
        # Fake register
        pass

    async def handle_interaction(self, interaction):
        # Fake interaction
        pass
