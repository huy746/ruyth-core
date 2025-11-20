import asyncio

def ensure_task(coro):
    """
    Helper to ensure an async coroutine is scheduled safely.
    """
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # Nếu chưa có loop, tạo mới
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    return loop.create_task(coro)
    
