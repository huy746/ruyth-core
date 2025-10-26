import asyncio
import subprocess

class VoiceManager:
    def __init__(self, client):
        self.client = client
        self.connected_channel = None

    async def connect(self, channel_id):
        self.connected_channel = channel_id
        print(f"[Voice] (sim) connected to {channel_id}")

    async def play(self, source_url):
        if not self.connected_channel:
            raise RuntimeError("Not connected to voice channel")
        print(f"[Voice] (sim) playing {source_url} in {self.connected_channel}")
        # simulate playback (optionally spawn a subprocess or stream)
        await asyncio.sleep(1)
        # subprocess.run(["echo", f"simulate play {source_url}"])

    async def disconnect(self):
        print(f"[Voice] (sim) disconnected from {self.connected_channel}")
        self.connected_channel = None
