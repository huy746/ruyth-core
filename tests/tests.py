import ruythcore

bot = ruythcore.RuythBot("TOKEN")

@bot.event
async def on_ready(data):
    print("✅ Bot sẵn sàng!")

@bot.command("ping")
async def ping(data):
    ctx = ruythcore.Context(bot, data["d"])
    await ctx.reply("Pong!")

bot.launch()

