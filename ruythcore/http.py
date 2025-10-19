import aiohttp
import asyncio
import json

class HTTPClient:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://discord.com/api/v10"
        self.session = aiohttp.ClientSession()

    async def send_message(self, channel_id, content):
        url = f"{self.base_url}/channels/{channel_id}/messages"
        headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json"
        }
        async with self.session.post(url, headers=headers, json={"content": content}) as resp:
            return await resp.text()

    async def close(self):
        await self.session.close()
      
