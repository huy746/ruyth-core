import asyncio
from unittest.mock import patch

from ruythcore.client import Client

def test_client_init():
    """
    Test khởi tạo Client mà không cần thật sự khởi tạo HTTPClient hoặc Gateway.
    """
    # Tạo loop giả để tránh lỗi RuntimeError
    asyncio.set_event_loop(asyncio.new_event_loop())

    # Patch (mock) toàn bộ lớp HTTPClient và Gateway để không chạy code bên trong
    with patch("ruythcore.client.HTTPClient", autospec=True) as mock_http, \
         patch("ruythcore.client.Gateway", autospec=True) as mock_gateway:

        c = Client("fake-token")

        # Kiểm tra các thuộc tính chính có tồn tại
        assert hasattr(c, "http")
        assert hasattr(c, "slash")
        assert hasattr(c, "voice")
        assert c.token == "fake-token"
        assert c.prefix == "!"

        # Kiểm tra mock được gọi đúng
        mock_http.assert_called_once_with("fake-token")
        mock_gateway.assert_called_once()

    print(">>> Client init test: PASSED ✅")
             
