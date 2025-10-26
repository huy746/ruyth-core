import aiohttp
import json
from .constants import API_BASE

class HTTPClient:
    def __init__(self, token: str):
        self.token = token
        self.base = API_BASE
        self._headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json"
        }
        self.session = aiohttp.ClientSession(headers=self._headers)

    async def request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base}{endpoint}"
        async with self.session.request(method, url, **kwargs) as resp:
            text = await resp.text()
            try:
                return json.loads(text) if text else None
            except Exception:
                return text

    async def send_message(self, channel_id: int, content: str):
        payload = {"content": content}
        return await self.request("POST", f"/channels/{channel_id}/messages", json=payload)

    async def close(self):
        await self.session.close()
                 
