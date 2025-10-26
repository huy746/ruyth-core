class Context:
    def __init__(self, client, raw_event):
        self.client = client
        self.raw = raw_event
        self.channel_id = raw_event.get("channel_id")
        self.author = raw_event.get("author", {}).get("username")

    async def reply(self, content: str):
        """Send a message to the channel where event came from."""
        await self.client.http.send_message(self.channel_id, content)
        
