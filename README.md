# ruythcore
[![discord](https://img.shields.io/badge/join_us-on_discord-5865F2?)](https://discord.gg/MZVrynFHFE)
[![Python](https://img.shields.io/pypi/pyversions/discord.py.svg)](https://pypi.org/project/ruythcore)

## Install

```bash
pip install ruythcore
```

### Bot Example
```bash
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

bot.start()
```
##### Note: Replace YOUR_BOT_TOKEN with your TOKEN . Do not share TOKEN.

### Run
```bash
python <namefile>.py
```
###### When showing "RuythCore Ready ✅ is successful.


## Link
[Docs](https://docsruythcore.blogspot.com)

[Server](https://discord.gg/MZVrynFHFE)

[Discord API](https://discord.gg/discord-api)
