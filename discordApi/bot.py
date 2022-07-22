import interactions
import requests


def bot_construct(base_url, guild, token):
    bot = interactions.Client(token=token)

    @bot.command(
        name="ping",
        description="ping server",
        scope=guild
    )
    async def ping(ctx: interactions.CommandContext):
        response = requests.get(f"{base_url}/discordApi/ping")
        await ctx.send(response.text)

    @bot.command(
        name="chatlog_data_backfill",
        description="Backfills chat data to database",
        scope=guild
    )
    async def chatlog_data_backfill(ctx: interactions.CommandContext):
        channel_id = ctx.channel_id

        headers = {
            "channel-id": str(channel_id)
        }

        response = requests.get(f"{base_url}/discordApi/download_channel_message_history", headers=headers)

        await ctx.send(response.text)

    return bot
