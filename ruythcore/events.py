import inspect

class EventHandler:
    def __init__(self):
        self.listeners = {}

    def on(self, name):
        def decorator(func):
            self.listeners.setdefault(name, []).append(func)
            return func
        return decorator

    async def emit(self, name, *args, **kwargs):
        for func in list(self.listeners.get(name, [])):
            try:
                if inspect.iscoroutinefunction(func):
                    await func(*args, **kwargs)
                else:
                    func(*args, **kwargs)
            except Exception as e:
                # prevent event handler crash
                print(f"[EventHandler] error in handler for {name}: {e}")
