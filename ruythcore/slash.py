import aiohttp
import json
from .constants import API_BASE

class SlashManager:
    def __init__(self, client):
        self.client = client
        self.commands = {}

    def command(self, name: str, description: str = "Command"):
        def decorator(func):
            self.commands[name] = {"func": func, "description": description}
            return func
        return decorator

    async def register_global_commands(self):
        """
        Register commands globally for the application.
        Note: this calls Discord REST API - requires application id.
        """
        app_id = await self.client.get_application_id()
        if not app_id:
            return
        endpoint = f"/applications/{app_id}/commands"
        payload = []
        for name, info in self.commands.items():
            payload.append({
                "name": name,
                "type": 1,
                "description": info.get("description", "Command")
            })
        if not payload:
            return
        async with aiohttp.ClientSession(headers={
            "Authorization": f"Bot {self.client.token}",
            "Content-Type": "application/json"
        }) as s:
            async with s.put(f"{API_BASE}{endpoint}", data=json.dumps(payload)) as r:
                if r.status >= 400:
                    text = await r.text()
                    raise RuntimeError(f"Register slash failed: {r.status} {text}")
                return await r.json()

    async def handle_interaction(self, data):
        name = data.get("data", {}).get("name")
        if name in self.commands:
            ctx = self.client.get_context(data)
            await self.commands[name]["func"](ctx)
