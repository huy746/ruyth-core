# test/test_dummy.py
from ruythcore.client import Client  # import trực tiếp file chứa class

def test_imports():
    c = Client("fake-token")
    assert hasattr(c, "http")
    assert hasattr(c, "slash")
    assert hasattr(c, "voice")

if __name__ == "__main__":
    test_imports()
    print(">>> Test import Client thành công!")
    
