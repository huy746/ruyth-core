class Context:
    def __init__(self, bot, raw_event):
        self.bot = bot
        self.raw = raw_event
        self.channel_id = raw_event["channel_id"]
        self.author = raw_event["author"]["username"]

    async def reply(self, content: str):
        await self.bot.http.send_message(self.channel_id, content)
      
