import sys
import os

# Thêm đường dẫn gốc của project vào sys.path
# để pytest có thể import ruythcore khi chạy trên GitHub Actions
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



def test_imports():
    """Kiểm tra xem Client và các thuộc tính chính có tồn tại không"""
    c = ruythcore.Client("fake-token")
    assert hasattr(c, "http"), "Client không có thuộc tính http"
    assert hasattr(c, "slash"), "Client không có thuộc tính slash"
    assert hasattr(c, "voice"), "Client không có thuộc tính voice"
    
