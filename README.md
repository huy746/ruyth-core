# ruythcore
[![discord](https://img.shields.io/badge/join_us-on_discord-5865F2?)](http://discord.com)
[![Python](https://img.shields.io/pypi/pyversions/discord.py.svg)](http://makeapullrequest.com)

## Install

```bash
pip install ruythcore
```

### Bot Example
```bash
import asyncio
import ruythcore

bot = ruythcore.Client("YOUR_BOT_TOKEN", prefix="!")

@bot.command("ping")
async def ping(ctx):
    await ctx.reply("🏓 Pong from RuythCore!")

@bot.slash_command("hello", description="Say hello")
async def hello(ctx):
    await ctx.reply(f"Hello from RuythCore!")

@bot.event
async def on_ready(data):
    print("RuythCore Ready ✅")

bot.run()
```
##### Note: Replace YOUR_BOT_TOKEN with your TOKEN . Do not share TOKEN.

### Run
```bash
python <namefile>.py
```
###### When showing "RuythCore Ready ✅ is successful.

Link

[Sever]()

[Discord API](https://discord.gg/discord-api)
