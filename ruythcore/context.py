class Context:
    def __init__(self, client, msg):
        self.client = client
        self.message = msg
        self.channel_id = getattr(msg, "channel_id", None)

    async def reply(self, content: str):
        if self.channel_id:
            return await self.client.http.request(
                "POST",
                f"/channels/{self.channel_id}/messages",
                json={"content": content},
            )
                
