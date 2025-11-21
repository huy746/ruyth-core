import aiohttp
from .constants import HTTP_BASE, USER_AGENT

class HTTPClient:
    def __init__(self, token):
        self.token = token
        self.session = aiohttp.ClientSession()

    async def request(self, method, path, **kwargs):
        headers = kwargs.pop("headers", {})
        headers.update({
            "Authorization": f"Bot {self.token}",
            "User-Agent": USER_AGENT
        })
        async with self.session.request(method, HTTP_BASE + path, headers=headers, **kwargs) as resp:
            if resp.status >= 400:
                raise Exception(await resp.text())
            try:
                return await resp.json()
            except:
                return await resp.text()

    async def close(self):
        await self.session.close()
