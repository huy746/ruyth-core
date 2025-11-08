import os
import sys

# ép sys.path trỏ đến thư mục chứa mã nguồn thật
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

# In debug xem import từ đâu
import Client from ruythcore
print(">>> DEBUG: ruythcore được import từ:", getattr(ruythcore, "__file__", "Không có __file__"))

# Nếu không có attribute Client -> ép reload từ đúng file __init__.py
if not hasattr(ruythcore, "Client"):
    import importlib
    print(">>> Cảnh báo: ruythcore không có Client, đang ép reload...")
    importlib.reload(ruythcore)

def test_imports():
    from ruythcore import Client
    c = Client("fake-token")
    assert hasattr(c, "http")
    assert hasattr(c, "slash")
    assert hasattr(c, "voice")
    
