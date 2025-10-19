class SlashManager:
    def __init__(self, bot):
        self.bot = bot
        self.commands = {}

    def slash(self, name, description=""):
        def decorator(func):
            self.commands[name] = func
            return func
        return decorator

    async def register_global_commands(self):
        pass
                                       
