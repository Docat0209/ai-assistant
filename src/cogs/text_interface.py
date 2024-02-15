"""Text Interface"""

from discord.ext import commands
from core import LLM


class TextInterface(commands.Cog):
    """Text Interface"""

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        """Response when user send message on specific channel"""
        if "&" in msg.content:
            return
        if msg.channel.id not in [1201781543169970228, 1206648134097313852]:
            return
        if msg.author.bot:
            return
        await msg.channel.send(LLM().chat(msg.content))


async def setup(client) -> None:
    """Cog setup"""
    await client.add_cog(TextInterface(client))
