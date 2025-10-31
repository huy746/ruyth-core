<div align="center">
	<br />
	<p>
		<a href="https://github.com"><img src="https://github.com/huy746/ruyth-core/blob/main/tests/template/Ruyth%20Core.png" width="546" alt="discord.js" /></a>
	</p>
	<br />
	<p>
		<a href="https://discord.gg/MZVrynFHFE"><img src="https://img.shields.io/badge/join_us-on_discord-5865F2?logo=discord&logoColor=white" alt="Discord server" /></a>
	
</div>

# Install
Install

```bash
pip install .
```
Example
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
