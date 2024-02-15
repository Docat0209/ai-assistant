"""Discord cogs"""

from logging import getLogger

from discord.ext.commands import Cog

log = getLogger(__name__)

__all__ = ("Plugin",)


class Plugin(Cog):
    """Cog template"""

    async def cog_load(self) -> None:
        log.info("Loaded %s cog.", self.qualified_name)
