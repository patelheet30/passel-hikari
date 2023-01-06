import hikari
import lightbulb
import random
from utils.info import sendall, mode, pin_message_id
from utils.blfuncs import get_ids

pin_event = lightbulb.Plugin("pin_event", "Contains listeners for pinning events")

blacklist_ids = get_ids()

if sendall:
    @pin_event.listener(hikari.MessageUpdateEvent)
    async def on_pin(event: hikari.MessageUpdateEvent) -> None:
        if str(event.channel_id) in blacklist_ids:
            return None
        else:
            is_pinned = event.message.is_pinned
            channel_obj = await event.app.rest.fetch_channel(event.channel_id)
            channel_name = channel_obj.name
            message_timestamp = event.message.timestamp

            embed = hikari.Embed(
                title=f"Sent by {event.message.author}",
                description=f"{event.content}",
                colour=hikari.Colour.of((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))),
            )
            embed.add_field(name="Jump", value=f"https://discord.com/channels/{event.message.guild_id}/{event.channel_id}/{event.message_id}")
            embed.set_footer(f"Sent in: {channel_name} at: {(message_timestamp.strftime('%d/%m/%Y, %H:%M:%S'))}")

            if not is_pinned:
                return None
            else:
                await event.app.rest.unpin_message(channel=event.channel_id, message=event.message_id)
                await event.app.rest.create_message(channel=pin_message_id, content=embed)

else:
    if mode == 1:
        @pin_event.listener(hikari.MessageUpdateEvent)
        async def on_pin(event: hikari.MessageUpdateEvent) -> None:
            if str(event.channel_id) in blacklist_ids:
                return None
            else:
                is_pinned = event.message.is_pinned
                latest_pin = await event.app.rest.fetch_pins(event.channel_id)

                channel_obj = await event.app.rest.fetch_channel(event.channel_id)
                channel_name = channel_obj.name
                message_timestamp = event.message.timestamp

                embed = hikari.Embed(
                    title=f"Sent by {event.message.author}",
                    description=f"{event.content}",
                    colour=hikari.Colour.of((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))),
                )
                embed.add_field(name="Jump", value=f"https://discord.com/channels/{event.message.guild_id}/{event.channel_id}/{event.message_id}")
                embed.set_footer(f"Sent in: {channel_name} at: {(message_timestamp.strftime('%d/%m/%Y, %H:%M:%S'))}")

                if not is_pinned:
                    return
                else:
                    if len(latest_pin) <= 49:
                        return None
                    else:
                        await event.app.rest.unpin_message(channel=event.channel_id, message=event.message_id)
                        await event.app.rest.create_message(channel=pin_message_id, content=embed)

    elif mode == 2:
        @pin_event.listener(hikari.MessageUpdateEvent)
        async def on_pin(event: hikari.MessageUpdateEvent) -> None:
            if str(event.channel_id) in blacklist_ids:
                return None
            else:
                is_pinned = event.message.is_pinned

                if not is_pinned:
                    return
                else:
                    latest_pin = await event.app.rest.fetch_pins(event.channel_id)
                    message_timestamp = latest_pin[-1].timestamp
                    channel_obj = await event.app.rest.fetch_channel(event.channel_id)
                    channel_name = channel_obj.name

                    embed = hikari.Embed(
                        title=f"Sent by {latest_pin[-1].author}",
                        description=f"{latest_pin[-1].content}",
                        colour=hikari.Colour.of((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))),
                    )
                    embed.add_field(name="Jump",
                                    value=f"https://discord.com/channels/{event.message.guild_id}/{event.channel_id}/{latest_pin[-1].id}")
                    embed.set_footer(f"Sent in: {channel_name} at: {(message_timestamp.strftime('%d/%m/%Y, %H:%M:%S'))}")
                    if len(latest_pin) <= 49:
                        return None
                    else:
                        await event.app.rest.create_message(channel=pin_message_id, content=embed)
                        await event.app.rest.unpin_message(channel=event.channel_id, message=latest_pin[-1].id)

    else:
        print("Mode must be either 1 or 2")
        exit()


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(pin_event)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(pin_event)
