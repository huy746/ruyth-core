class Context:
    def __init__(self, client, raw, slash=False):
        self.client = client
        self.raw = raw
        self.is_slash = slash
        if slash:
            # minimal safe extraction
            self.interaction_id = raw.get("id")
            self.token = raw.get("token")
            # channel might be nested differently; try both
            self.channel_id = (raw.get("channel",{}) or {}).get("id") or raw.get("channel_id")
            member = raw.get("member") or {}
            user = member.get("user") or raw.get("user") or {}
            self.author = type("U",(object,),{"id": user.get("id"), "username": user.get("username")})
            self.content = None
        else:
            self.interaction_id = None
            self.token = None
            self.channel_id = raw.get("channel_id")
            author = raw.get("author", {})
            self.author = type("U",(object,),{"id": author.get("id"), "username": author.get("username")})
            self.content = raw.get("content", "")

    async def reply(self, content: str):
        if self.is_slash:
            # use interaction response
            return await self.client.http.send_interaction_response(self.interaction_id, self.token, content)
        else:
            return await self.client.http.send_message(self.channel_id, content)
        
