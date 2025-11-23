# ruythcore
[![discord](https://img.shields.io/badge/join_us-on_discord-5865F2?)](https://discord.gg/MZVrynFHFE)
[![pypi](https://img.shields.io/pypi/v/ruythcore.svg)](https://pypi.org/project/ruythcore)
[![Python](https://img.shields.io/pypi/pyversions/ruythcore.svg)](https://pypi.org/project/ruythcore)

## Install

```bash
pip install ruythcore
```

### Bot Example
```bash
import ruythcore

bot = ruythcore.Client("YOUR_TOKEN_HERE", prefix="!")

@bot.command("ping")
async def ping(ctx):
    await ctx.reply("🏓 Pong from RuythCore!")

@bot.slash_command("hello")
async def hello(ctx):
    await ctx.reply("Hello from RuythCore!")

@bot.events.on("ready")
async def on_ready(data):
    print("Ready ✅")

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
