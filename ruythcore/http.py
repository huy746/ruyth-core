import aiohttp
import asyncio
from .constants import HTTP_BASE, USER_AGENT

class HTTPClient:
    def __init__(self, token):
        self.token = token
        self._session = None

    async def _ensure(self):
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()

    async def request(self, method, path, **kwargs):
        await self._ensure()
        headers = kwargs.pop("headers", {})
        headers.update({
            "Authorization": f"Bot {self.token}",
            "User-Agent": USER_AGENT,
        })
        async with self._session.request(method, HTTP_BASE + path, headers=headers, **kwargs) as resp:
            text = await resp.text()
            if resp.status >= 400:
                raise Exception(f"HTTP {resp.status}: {text}")
            try:
                return await resp.json()
            except Exception:
                return text

    # convenience helpers
    async def send_message(self, channel_id, content):
        return await self.request("POST", f"/channels/{channel_id}/messages", json={"content": content})

    async def send_interaction_response(self, interaction_id, token, content):
        # simple immediate response (type 4 = CHANNEL_MESSAGE_WITH_SOURCE)
        await self._ensure()
        url = f"{HTTP_BASE}/interactions/{interaction_id}/{token}/callback"
        data = {"type": 4, "data": {"content": content}}
        async with self._session.post(url, json=data, headers={
            "Authorization": f"Bot {self.token}",
            "User-Agent": USER_AGENT
        }) as resp:
            if resp.status >= 400:
                raise Exception(await resp.text())
            try:
                return await resp.json()
            except:
                return await resp.text()

    async def close(self):
        if self._session:
            await self._session.close()
    
