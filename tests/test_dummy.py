import os
import sys

# Thêm đường dẫn thư mục gốc (chứa thư mục "ruythcore")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    import ruythcore
except ImportError as e:
    raise ImportError(f"Lỗi import ruythcore: {e}")

def test_imports():
    """Kiểm tra module ruythcore có import được và class Client hoạt động"""
    c = ruythcore.Client("fake-token")
    assert hasattr(c, "http"), "Client thiếu thuộc tính http"
    assert hasattr(c, "slash"), "Client thiếu thuộc tính slash"
    assert hasattr(c, "voice"), "Client thiếu thuộc tính voice"
