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

if __name__ == "__main__":
    bot.run()

