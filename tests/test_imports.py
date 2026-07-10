import asyncio

import ruythcore
from ruythcore.models import Message, User


def test_import_main():
    assert ruythcore.Client is not None


def test_client_init():
    bot = ruythcore.Client("FAKE_TOKEN", prefix="!")
    assert bot.prefix == "!"
    assert bot.token == "FAKE_TOKEN"


def test_event_decorator_infers_on_prefix_name():
    bot = ruythcore.Client("FAKE_TOKEN")

    @bot.event
    async def on_ready(data):
        return data

    assert bot.events.listeners["ready"] == [on_ready]


def test_context_accepts_message_model():
    bot = ruythcore.Client("FAKE_TOKEN")
    msg = Message(
        id="1",
        channel_id="2",
        content="!ping",
        author=User(id="3", username="tester"),
    )

    ctx = bot.create_context(msg)

    assert ctx.channel_id == "2"
    assert ctx.content == "!ping"
    assert ctx.author.id == "3"
    assert ctx.author.username == "tester"


def test_command_dispatch_builds_context_from_message_model():
    bot = ruythcore.Client("FAKE_TOKEN", prefix="!")
    seen = []

    @bot.command("ping")
    async def ping(ctx, *args):
        seen.append((ctx.channel_id, ctx.author.username, args))

    msg = Message(
        id="1",
        channel_id="2",
        content="!ping a b",
        author=User(id="3", username="tester"),
    )

    asyncio.run(bot.cmd.run(bot, msg))

    assert seen == [("2", "tester", ("a", "b"))]
