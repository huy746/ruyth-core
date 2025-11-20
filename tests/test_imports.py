def test_import_main():
    import ruythcore

def test_client_init():
    import ruythcore
    bot = ruythcore.Client("FAKE_TOKEN", prefix="!")
    assert bot.prefix == "!"
    assert bot.token == "FAKE_TOKEN"
    
