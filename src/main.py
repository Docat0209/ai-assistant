"""AI Assistant"""

import os
import asyncio

import discord

from bot import Bot

TOKEN = os.getenv("DISCORD_TOKEN")


async def main():
    """Run discord bot"""
    discord.utils.setup_logging()
    async with Bot() as bot:
        await bot.start(TOKEN, reconnect=True)


if __name__ == "__main__":
    asyncio.run(main())
