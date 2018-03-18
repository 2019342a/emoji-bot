"""
A simple discord bot.
"""

import random

import discord

from .constants import BAD_EMOJIS
from .constants import GOOD_EMOJIS
from .constants import USERS

class BotClient(discord.Client):
    """
    Contains the methods that the bot can execute.
    """

    async def on_ready(self):
        """
        Displays to the console.
        """
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        """
        Prints the message to the console.
        """
        if str(message.author) in USERS:
            await message.add_reaction(random.choice(GOOD_EMOJIS))
        else:
            await message.add_reaction(random.choice(BAD_EMOJIS))
