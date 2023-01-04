import hikari
import os
import lightbulb
from dotenv import load_dotenv

load_dotenv()

bot = lightbulb.BotApp(
    token="",
    default_enabled_guilds=INSERT_HERE,
    intents=hikari.Intents.ALL
)


@bot.listen(hikari.StartedEvent)
async def on_start(event: hikari.StartedEvent) -> None:
    print("Bot has started")


bot.load_extensions_from("extensions", recursive=True)


bot.run()
