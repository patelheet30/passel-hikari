import hikari
import lightbulb
import random
from utils.info import mode, sendall, pin_message_id
from utils.blfuncs import get_ids

commands = lightbulb.Plugin("commands", "List of commands for the bot")


@commands.command()
@lightbulb.command("settings", "View the settings of the bot")
@lightbulb.implements(lightbulb.SlashCommand)
async def on_settings_view(ctx: lightbulb.SlashContext) -> None:
    blacklist_ids = get_ids()
    edited_blacklist = [f"<#{i}>" for i in blacklist_ids]

    embed = hikari.Embed(
        title=f"View settings",
        colour=hikari.Colour.of((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))),
    )

    embed.add_field(name="Mode", value=f"{mode}", inline=True)
    embed.add_field(name="Send all?", value=f"{sendall}", inline=True)
    embed.add_field(name="Pins archive channel", value=f"<#{pin_message_id}>", inline=True)
    embed.add_field(name="Blacklist channels", value=" ".join(edited_blacklist) if edited_blacklist else "No blacklisted channels")

    await ctx.respond(embed)


@commands.command()
@lightbulb.command("pins", "View the amount of pins in this channel")
@lightbulb.implements(lightbulb.SlashCommand)
async def on_pins_count(ctx: lightbulb.SlashContext) -> None:
    channel_pins = await ctx.app.rest.fetch_pins(ctx.channel_id)
    count = len(channel_pins)

    await ctx.respond(f"Channel has {count} pin(s)")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(commands)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(commands)
