class Context:
    def __init__(self, message=None, interaction=None):
        self.message = message
        self.interaction = interaction

    async def send(self, content):
        print(f"[BOT SEND]: {content}")
