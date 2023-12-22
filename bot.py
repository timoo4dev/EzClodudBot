import discord

import ezcloud
import logging
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

ezcloud.set_log(
    log_level=logging.DEBUG, 
    file=True
)

bot = ezcloud.Bot(
    intents=discord.Intents.all(), 
    language="de",
)

bot.add_help_command(
    style=ezcloud.HelpStyle.codeblocks
)

if __name__ == "__main__":
    bot.load_cogs("cogs")

    bot.run(TOKEN)
