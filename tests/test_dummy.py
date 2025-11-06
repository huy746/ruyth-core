import os
import sys

# ép sys.path lấy code trong repo này
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import ruythcore
print(">>> DEBUG: ruythcore được import từ:", getattr(ruythcore, "__file__", "Không có __file__"))

def test_imports():
    c = ruythcore.Client("fake-token")
    assert hasattr(c, "http")
    assert hasattr(c, "slash")
    assert hasattr(c, "voice")
