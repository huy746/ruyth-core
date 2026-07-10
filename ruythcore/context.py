class Context:
    def __init__(self, client, raw, slash=False):
        self.client = client
        self.raw = raw
        self.is_slash = slash
        if slash:
            self.interaction_id = raw.get("id")
            self.token = raw.get("token")
            self.channel_id = (raw.get("channel", {}) or {}).get("id") or raw.get("channel_id")
            member = raw.get("member") or {}
            user = member.get("user") or raw.get("user") or {}
            self.author = type(
                "U",
                (object,),
                {"id": user.get("id"), "username": user.get("username")},
            )
            self.content = None
        else:
            self.interaction_id = None
            self.token = None
            self.channel_id = self._get(raw, "channel_id")
            author = self._get(raw, "author", {}) or {}
            if isinstance(author, dict):
                author_id = author.get("id")
                username = author.get("username")
            else:
                author_id = getattr(author, "id", None)
                username = getattr(author, "username", None)
            self.author = type("U", (object,), {"id": author_id, "username": username})
            self.content = self._get(raw, "content", "")

    @staticmethod
    def _get(raw, key, default=None):
        if isinstance(raw, dict):
            return raw.get(key, default)
        return getattr(raw, key, default)

    async def reply(self, content: str):
        if self.is_slash:
            return await self.client.http.send_interaction_response(
                self.interaction_id, self.token, content
            )
        return await self.client.http.send_message(self.channel_id, content)
