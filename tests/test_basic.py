import ruythcore

def test_imports():
    c = ruythcore.Client("fake-token")
    assert hasattr(c, "http")
    assert hasattr(c, "slash")
    assert hasattr(c, "voice")
    
