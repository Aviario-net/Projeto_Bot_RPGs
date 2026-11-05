# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2025 Aviario

"""Comandos de ficha no Discord."""
import discord
from discord.ext import commands

from rpgbot.config import settings
from rpgbot.features.character.models import Character
from rpgbot.features.character.repository import CharacterRepository
from rpgbot.features.character.service import CharacterService


class EditarFichaModal(discord.ui.Modal, title="Editar Ficha"):
    """Modal com 5 campos (limite do Discord). Fazer mais Modais, não sei se dá certo 👍"""

    nome = discord.ui.TextInput(label="Nome", max_length=60)
    raca = discord.ui.TextInput(label="Raça", max_length=40)
    classe = discord.ui.TextInput(label="Classe", max_length=40)
    nivel = discord.ui.TextInput(label="Nível (1-20)", max_length=2)
    hp_atual = discord.ui.TextInput(label="HP Atual", max_length=4)

    def __init__(
        self,
        character: Character,
        service: CharacterService,
        user_id: int,
    ) -> None:
        super().__init__()
        self.character = character
        self.service = service
        self.user_id = user_id
        self.nome.default = character.nome
        self.raca.default = character.raca
        self.classe.default = character.classe
        self.nivel.default = str(character.nivel)
        self.hp_atual.default = str(character.pontos_de_vida.atual)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        try:
            self.character.nome = self.nome.value
            self.character.raca = self.raca.value
            self.character.classe = self.classe.value
            self.character.nivel = int(self.nivel.value)
            self.character.pontos_de_vida.atual = int(self.hp_atual.value)
        except ValueError:
            await interaction.response.send_message(
                "❌ Nível e HP devem ser números inteiros.",
                ephemeral=True,
            )
            return

        self.service.salvar(self.user_id, self.character)
        await interaction.response.send_message(
            "✅ Ficha atualizada! Use `/ficha` para ver.",
            ephemeral=True,
        )


class CharacterCog(commands.Cog):
    """Fichas de personagem."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.service = CharacterService(
            CharacterRepository(settings.data_dir / "characters")
        )

    @commands.hybrid_command(name="criarficha", description="Cria sua ficha")
    async def criar(self, ctx: commands.Context) -> None:
        if self.service.obter(ctx.author.id):
            await ctx.send(
                "⚠️ Você já tem uma ficha. Use `/ficha` para ver.",
                ephemeral=True,
            )
            return
        self.service.criar(ctx.author.id)
        await ctx.send(f"✅ Ficha criada para {ctx.author.mention}!")

    @commands.hybrid_command(name="ficha", description="Mostra sua ficha")
    async def ver(self, ctx: commands.Context) -> None:
        character = self.service.obter(ctx.author.id)
        if not character:
            await ctx.send(
                "❌ Você não tem ficha. Use `/criarficha`.",
                ephemeral=True,
            )
            return
        await ctx.send(embed=self._build_embed(character))

    @commands.hybrid_command(name="editarficha", description="Edita sua ficha")
    async def editar(self, ctx: commands.Context) -> None:
        character = self.service.obter(ctx.author.id)
        if not character:
            await ctx.send("❌ Crie uma ficha primeiro.", ephemeral=True)
            return

        modal = EditarFichaModal(character, self.service, ctx.author.id)
        if ctx.interaction:
            await ctx.interaction.response.send_modal(modal)
        else:
            await ctx.send_modal(modal)

    def _build_embed(self, c: Character) -> discord.Embed:
        embed = discord.Embed(
            title=f"📜 {c.nome}",
            description=f"{c.raca} • {c.classe} • Nível {c.nivel}",
            color=discord.Color.gold(),
        )
        embed.add_field(
            name="❤️ Pontos de Vida",
            value=f"{c.pontos_de_vida.atual}/{c.pontos_de_vida.maximo}",
            inline=False,
        )
        attrs = c.atributos
        embed.add_field(
            name="Atributos",
            value=(
                f"FOR {attrs.forca} • DES {attrs.destreza} • CON {attrs.constituicao}\n"
                f"INT {attrs.inteligencia} • SAB {attrs.sabedoria} • CAR {attrs.carisma}"
            ),
            inline=False,
        )
        return embed

    @commands.hybrid_command(
        name="hp",
        description="Ajusta os pontos de vida (atual e máximo)",
    )
    async def ajustar_hp(
        self,
        ctx: commands.Context,
        atual: int,
        maximo: int,
    ) -> None:
        character = self.service.obter(ctx.author.id)
        if not character:
            await ctx.send("❌ Crie uma ficha primeiro.", ephemeral=True)
            return
        if maximo < 1 or atual < 0 or atual > maximo:
            await ctx.send(
                "❌ Valores inválidos. `atual` entre 0 e `maximo`, `maximo` ≥ 1.",
                ephemeral=True,
            )
            return

        character.pontos_de_vida.atual = atual
        character.pontos_de_vida.maximo = maximo
        self.service.salvar(ctx.author.id, character)
        await ctx.send(f"❤️ HP ajustado para **{atual}/{maximo}**.")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CharacterCog(bot))