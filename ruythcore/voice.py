class VoiceClient:
    def __init__(self):
        self.ready = False

    async def connect(self):
        self.ready = True
