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

    return bot
