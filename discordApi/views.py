from django.shortcuts import render
from django.http import HttpResponse
import requests
from dotenv import load_dotenv
import json
import os
import time

from . import utils

load_dotenv("../AUTH.env")

app_utils = utils.Main(**{
    "discord_base_url": "https://discord.com/api",
    "DISCORD_TOKEN": os.environ.get("DISCORD_TOKEN")
})


def ping(request) -> HttpResponse:
    return HttpResponse('pong')


def download_channel_message_history(request) -> HttpResponse:
    channel_id = request.headers["channel-id"]

    app_utils.download_channel_message_history(channel_id)

    return HttpResponse("Chatlogs downloaded successfully")


def download_guild_member_data(request) -> HttpResponse:
    guild_id = request.headers["guild-id"]

    app_utils.download_guild_member_data(guild_id)

    return HttpResponse("User data downloaded successfully")
