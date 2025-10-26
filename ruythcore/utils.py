# ruythcore/utils.py
import asyncio

def ensure_task(coro):
    """Run coroutine as background task"""
    return asyncio.create_task(coro)
    
