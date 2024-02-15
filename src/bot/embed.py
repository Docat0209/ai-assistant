"""Discord embed"""

__all__ = ("Embed",)

from typing_extensions import Self
from discord import Colour, Embed as OriginalEmbed


class Embed(OriginalEmbed):
    """Embed template"""

    def __init__(self, color: int | Colour | None = Colour.blurple(), **kwargs):
        super().__init__(color=color, **kwargs)

    def credits(self) -> Self:
        """Credits footer"""
        super().set_footer(text="Powered by gpt-3.5-turbo-0125")
        return self
