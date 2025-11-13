import asyncio

def ensure_task(coro):
    """
    Helper to ensure an async coroutine is scheduled.
    """
    loop = asyncio.get_event_loop()
    return loop.create_task(coro)
    
