import asyncio
from ruythcore.client import Client

def test_imports():
    asyncio.set_event_loop(asyncio.new_event_loop())  # <-- thêm dòng này
    c = Client("fake-token")
    assert hasattr(c, "http")
    assert hasattr(c, "slash")
    assert hasattr(c, "voice")

if __name__ == "__main__":
    test_imports()
    print(">>> Test import Client thành công!")
    
