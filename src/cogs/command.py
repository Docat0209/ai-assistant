"""This is Command Cog
ping: show the bot't latency
"""

import discord

from discord import app_commands
from bot import Bot, Embed

from . import Plugin


class Command(Plugin):
    """Simple Command"""

    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot

    @app_commands.command(name="ping", description="show the bot's latency.")
    async def ping(self, interaction: discord.Interaction):
        """show the bot't latency"""
        embed = Embed(description=f"My ping is {round(self.bot.latency*1000)}ms")
        await interaction.response.send_message(embed=embed)


async def setup(bot: Bot) -> None:
    """Cog setup"""
    await bot.add_cog(Command(bot))
