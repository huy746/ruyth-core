class EventHandler:
    def __init__(self):
        self.listeners = {}

    def on(self, name):
        def decorator(func):
            self.listeners.setdefault(name, []).append(func)
            return func
        return decorator

    async def emit(self, name, *args, **kwargs):
        for func in self.listeners.get(name, []):
            await func(*args, **kwargs)
