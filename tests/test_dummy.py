import os
import sys

# Đảm bảo pytest tìm thấy package cục bộ
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import ruythcore


def test_imports():
    """Kiểm tra import thành công và có các thuộc tính chính"""
    c = ruythcore.Client("fake-token")
    assert hasattr(c, "http")
    assert hasattr(c, "slash")
    assert hasattr(c, "voice")
