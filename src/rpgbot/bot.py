# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2025 Aviario

"""Classe principal do bot e carregamento de cogs."""
import logging

import discord
from discord.ext import commands

from rpgbot.config import settings

logger = logging.getLogger(__name__)


class RPGbot(commands.Bot):
    """Wolframium."""

    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None,
        )

    async def setup_hook(self) -> None:
        await self.load_extension("rpgbot.interface.cogs.dice_cog")
        await self.load_extension("rpgbot.interface.cogs.character_cog")

        if settings.env == "development" and settings.dev_guild_id:
            guild = discord.Object(id=settings.dev_guild_id)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            logger.info(
                "Slash commands sincronizados no guild de dev %s",
                settings.dev_guild_id,
            )
        else:
            await self.tree.sync()
            logger.info("Slash commands sincronizados globalmente")

    async def on_ready(self) -> None:
        logger.info("Online como %s (id=%s)", self.user, self.user.id)
        logger.info("Em %d guild(s)", len(self.guilds))