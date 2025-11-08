import os
import sys

# Thêm path chính xác đến package ruythcore
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ruythcore")))

import ruythcore

print(">>> DEBUG:", getattr(ruythcore, "__file__", "Không có __file__"))

def test_imports():
    c = ruythcore.Client("fake-token")
    assert hasattr(c, "http")
    assert hasattr(c, "slash")
    assert hasattr(c, "voice")
