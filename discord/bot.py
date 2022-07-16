import os
import discord
import dotenv
import threading


dotenv.load_dotenv()
GUILD = os.getenv("DISCORD_GUILD")
TOKEN = os.getenv("DISCORD_TOKEN")

class CustomClient(discord.client):
    pass

client = CustomClient()


