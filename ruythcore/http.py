import asyncio
import importlib.util

from .constants import HTTP_BASE, USER_AGENT


class HTTPException(Exception):
    def __init__(self, status, message):
        super().__init__(f"HTTP {status}: {message}")
        self.status = status
        self.message = message


class MissingDependencyError(RuntimeError):
    """Raised when an optional runtime dependency is required but missing."""

    def __init__(self, package, feature):
        super().__init__(
            f"{package!r} is required to use {feature}. "
            f"Install runtime dependencies with: pip install {package} "
            "or pip install -r requirements.txt"
        )
        self.package = package
        self.feature = feature


class HTTPClient:
    def __init__(self, token):
        self.token = token
        self._session = None

    async def _ensure(self):
        if self._session is None or self._session.closed:
            if importlib.util.find_spec("aiohttp") is None:
                raise MissingDependencyError("aiohttp", "HTTP requests")
            import aiohttp

            self._session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=15)
            )

    async def request(self, method, path, retry=2, **kwargs):
        await self._ensure()

        default_headers = {
            "Authorization": f"Bot {self.token}",
            "User-Agent": USER_AGENT,
            "Content-Type": "application/json",
        }

        headers = {**default_headers, **kwargs.pop("headers", {})}
        url = HTTP_BASE + path

        for _ in range(retry + 1):
            async with self._session.request(
                method,
                url,
                headers=headers,
                **kwargs
            ) as resp:
                text = await resp.text()

                if resp.status == 429:
                    try:
                        data = await resp.json()
                        retry_after = data.get("retry_after", 1)
                    except Exception:
                        retry_after = 1

                    await asyncio.sleep(retry_after)
                    continue

                if resp.status >= 400:
                    raise HTTPException(resp.status, text)

                if resp.headers.get("Content-Type", "").startswith("application/json"):
                    return await resp.json()

                return text

        raise HTTPException(429, "Too many retries")

    async def send_message(self, channel_id, content):
        return await self.request(
            "POST",
            f"/channels/{channel_id}/messages",
            json={"content": content},
        )

    async def send_embed(self, channel_id, embed: dict):
        return await self.request(
            "POST",
            f"/channels/{channel_id}/messages",
            json={"embeds": [embed]},
        )

    async def delete_message(self, channel_id, message_id):
        return await self.request(
            "DELETE",
            f"/channels/{channel_id}/messages/{message_id}",
        )

    async def edit_message(self, channel_id, message_id, content):
        return await self.request(
            "PATCH",
            f"/channels/{channel_id}/messages/{message_id}",
            json={"content": content},
        )

    async def send_interaction_response(self, interaction_id, token, content):
        return await self.request(
            "POST",
            f"/interactions/{interaction_id}/{token}/callback",
            json={
                "type": 4,
                "data": {"content": content}
            },
        )

    async def followup_message(self, application_id, token, content):
        return await self.request(
            "POST",
            f"/webhooks/{application_id}/{token}",
            json={"content": content},
        )

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()

    async def __aenter__(self):
        await self._ensure()
        return self

    async def __aexit__(self, *args):
        await self.close()
