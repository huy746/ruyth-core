# test/test_dummy.py
import os
import sys

# Thêm thư mục root repo vào sys.path để Python tìm thấy ruythcore
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import ruythcore

print(">>> DEBUG:", getattr(ruythcore, "__file__", "Không có __file__"))

def test_imports():
    c = ruythcore.Client("fake-token")
    assert hasattr(c, "http"), "Client thiếu thuộc tính http"
    assert hasattr(c, "slash"), "Client thiếu thuộc tính slash"
    assert hasattr(c, "voice"), "Client thiếu thuộc tính voice"

if __name__ == "__main__":
    test_imports()
    print(">>> Test import Client thành công!")
