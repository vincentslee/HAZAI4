#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading
from discordApi.bot import bot_construct
from dotenv import load_dotenv

load_dotenv("AUTH.env")

DISCORD_GUILD = int(os.environ.get("DISCORD_GUILD"))
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
BASE_URL = os.environ.get("BASE_URL") # TODO: Find a better configuration method for this variable


def main():
    # discord_bot = bot_construct(BASE_URL, DISCORD_GUILD, DISCORD_TOKEN)
    # thread = threading.Thread(target=lambda: discord_bot.start())
    # thread.start()

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
