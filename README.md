# emoji-bot
A discord bot that sends specific emojis to a group of users and other to everybody else

# Installtion

run `pip install -r requirements.txt`

If pip was unable to find discord then run `python -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip`

# Usage

Create a discord bot and get the key from [here](https://discordapp.com/developers/applications/me).

Then enter you key in the `constants.py` file along with users good and bad emojis. Good emojis are considered emojis that we want to send to the set of users, bad to everybody else.

If everything was fine so far run `python main.py` and invite the bot to your server.
