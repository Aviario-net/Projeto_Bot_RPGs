# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2025 Aviario

"""Comandos de dados no Discord. Tem que mexer muito aqui"""
import discord
from discord.ext import commands

from rpgbot.rules import dice


class DiceCog(commands.Cog):
    """Rolagem de dados de RPG."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(
        name="roll",
        description="Rola dados (ex: 2d6+3, 1d20, d20)",
    )
    async def roll(self, ctx: commands.Context, expressao: str = "1d20") -> None:
        try:
            result = dice.roll(expressao)
        except ValueError as e:
            await ctx.send(f"❌ {e}", ephemeral=True)
            return

        embed = discord.Embed(
            title="🎲 Rolagem",
            description=f"**{dice.format_result(result)}**",
            color=discord.Color.blue(),
        )
        embed.set_footer(text=f"Rolado por {ctx.author.display_name}")
        await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="sorte",
        description="Mostra as probabilidades de uma expressão de dados",
    )
    # Vou verificar a Calculadora de sorte ainda, ou tu faz mesmo já que deves tá pesquisando
    async def sorte(self, ctx: commands.Context, expressao: str = "1d20") -> None:
        try:
            qty, faces, mod = dice.parse(expressao)
        except ValueError as e:
            await ctx.send(f"❌ {e}", ephemeral=True)
            return

        min_total = qty * 1 + mod
        max_total = qty * faces + mod
        media = qty * (faces + 1) / 2 + mod

        embed = discord.Embed(
            title="🍀 Calculadora de Sorte",
            color=discord.Color.green(),
        )
        embed.add_field(name="Expressão", value=f"`{expressao}`", inline=False)
        embed.add_field(name="Mínimo", value=str(min_total))
        embed.add_field(name="Máximo", value=str(max_total))
        embed.add_field(name="Média", value=f"{media:.2f}")
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DiceCog(bot))