import os
import sys
import importlib

# Đảm bảo pytest có thể tìm đúng package ruythcore/
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

print("DEBUG: sys.path[0] =", sys.path[0])

# Import lại module sạch đ
ể chắc chắn lấy đúng file __init__.py
ruythcore = importlib.import_module("ruythcore")

def test_imports():
    """Kiểm tra Client và các thuộc tính chính"""
    assert hasattr(ruythcore, "Client"), "Module ruythcore không có class Client"
    c = ruythcore.Client("fake-token")
    assert hasattr(c, "http"), "Client thiếu thuộc tính http"
    assert hasattr(c, "slash"), "Client thiếu thuộc tính slash"
    assert hasattr(c, "voice"), "Client thiếu thuộc tính voice"
