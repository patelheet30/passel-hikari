import hikari
import lightbulb
from utils.blfuncs import add_ids, remove_ids

blacklist = lightbulb.Plugin("blacklist", "Implements a command group to modify the blacklisted channels.")


@blacklist.command()
@lightbulb.command("blacklist", "The command group for modifying blacklist channels")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def on_blacklist(ctx: lightbulb.Context) -> None:
    return

@on_blacklist.child()
@lightbulb.option("channel", "The channel you want to add", type=hikari.OptionType.CHANNEL, channel_types=[hikari.ChannelType.GUILD_TEXT])
@lightbulb.command("add", "Adds a channel to the blacklist", auto_defer=True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def on_blacklist_add(ctx: lightbulb.Context) -> None:
    channel_obj: hikari.PartialChannel = ctx.options.channel
    channel_id = channel_obj.id
    duplicate = add_ids(str(channel_id))
    if duplicate == True:
        await ctx.respond(f"<#{channel_id}> already in blacklist")
    else:
        await ctx.respond(f"<#{channel_id}> added to blacklist")
    
@on_blacklist.child()
@lightbulb.option("channel", "The channel you want to remove", type=hikari.OptionType.CHANNEL, channel_types=[hikari.ChannelType.GUILD_TEXT])
@lightbulb.command("remove", "Removes a channel from the blacklist", auto_defer=True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def on_blacklist_remove(ctx: lightbulb.Context) -> None:
    channel_obj: hikari.PartialChannel = ctx.options.channel
    channel_id = channel_obj.id
    removed = remove_ids(str(channel_id))
    if removed == True:
        await ctx.respond(f"<#{channel_id}> removed from blacklist")
    else:
        await ctx.respond(f"<#{channel_id}> was never in the blacklist")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(blacklist)
    
def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(blacklist)