import asyncio
import pytest

# Import Client từ file client.py
from ruythcore.client import Client

@pytest.mark.asyncio
def test_client_init():
    """
    Test cơ bản: kiểm tra class Client có thể khởi tạo
    mà không cần thật sự kết nối Gateway hoặc HTTPClient.
    """
    # Mock event loop để tránh lỗi "no running event loop"
    asyncio.set_event_loop(asyncio.new_event_loop())

    # Fake token (để không gọi API)
    c = Client("fake-token")

    # Kiểm tra các thuộc tính chính tồn tại
    assert hasattr(c, "http")
    assert hasattr(c, "slash")
    assert hasattr(c, "voice")
    assert c.prefix == "!"
    assert c.token == "fake-token"

    print(">>> Client khởi tạo thành công!")
