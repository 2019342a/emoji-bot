"""
Main entry point of the bot.
"""

from src.bot import BotClient
from src.constants import KEY

def main():
    """
    Runs the bot.
    """
    client = BotClient()
    client.run(KEY)

if __name__ == "__main__":
    main()
