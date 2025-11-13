import aiohttp

class HTTPClient:
    def __init__(self, token: str):
        self.token = token
        self.session = aiohttp.ClientSession(headers={
            "Authorization": f"Bot {token}"
        })

    async def request(self, method: str, url: str, **kwargs):
        async with self.session.request(method, url, **kwargs) as r:
            return await r.json()
            
