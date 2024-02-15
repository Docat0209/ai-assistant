"""Discord bot settings"""

__all__ = ("Bot",)

import os
import sys
from logging import getLogger

import discord
from discord.ext import commands
from discord import WebhookMessage

from .embed import Embed

log = getLogger("Bot")


class Bot(commands.AutoShardedBot):
    """Bot settings"""

    def __init__(self):
        super().__init__(
            command_prefix="&",
            intents=discord.Intents.all(),
        )

    async def setup_hook(self) -> None:
        """Loading cogs"""
        for file in os.listdir("src/cogs"):
            if not file.startswith("_"):
                await self.load_extension(f"cogs.{file[:-3]}")

    async def on_ready(self) -> None:
        """When bot ready"""
        log.info("Logged in as %s (ID:%d)", self.user, self.user.id)

    async def on_connect(self) -> None:
        """Sync when bot connect"""
        if "-sync" in sys.argv:
            synced_commands = await self.tree.sync()
            log.info("Successfully synced %d commands.", len(synced_commands))

    async def success(
        self,
        message: str,
        interaction: discord.Interaction,
        ephemeral: bool | None = False,
        embed: bool | None = True,
    ) -> WebhookMessage | None:
        """Success message"""
        if embed:
            if interaction.response.is_done():
                return await interaction.followup.send(
                    embed=Embed(description=message, color=discord.Colour.green()),
                    ephemeral=ephemeral,
                )

            return await interaction.response.send_message(
                embed=Embed(description=message, color=discord.Colour.green()),
                ephemeral=ephemeral,
            )
        else:
            if interaction.response.is_done():
                return await interaction.followup.send(
                    content=f"✅ | {message}", ephemeral=ephemeral
                )
            return await interaction.response.send_message(
                content=f"✅ | {message}", ephemeral=ephemeral
            )

    async def error(
        self,
        message: str,
        interaction: discord.Interaction,
        ephemeral: bool | None = False,
        embed: bool | None = True,
    ) -> WebhookMessage | None:
        """Error message"""
        if embed:
            if interaction.response.is_done():
                return await interaction.followup.send(
                    embed=Embed(description=message, color=discord.Colour.red()),
                    ephemeral=ephemeral,
                )

            return await interaction.response.send_message(
                embed=Embed(description=message, color=discord.Colour.red()),
                ephemeral=ephemeral,
            )
        if interaction.response.is_done():
            return await interaction.followup.send(
                content=f"❌ | {message}", ephemeral=ephemeral
            )
        return await interaction.response.send_message(
            content=f"❌ | {message}", ephemeral=ephemeral
        )
