# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2025 Aviario

"""Modelos de personagem (ficha de D&D 5e)."""
from pydantic import BaseModel, ConfigDict, Field


class Attributes(BaseModel):
    """Os 6 atributos padrão do D&D."""

    forca: int = Field(default=10, ge=1, le=30)
    destreza: int = Field(default=10, ge=1, le=30)
    constituicao: int = Field(default=10, ge=1, le=30)
    inteligencia: int = Field(default=10, ge=1, le=30)
    sabedoria: int = Field(default=10, ge=1, le=30)
    carisma: int = Field(default=10, ge=1, le=30)

# por enquanto eu fiz ser funcional
class HitPoints(BaseModel):
    """Pontos de vida."""

    atual: int = Field(default=10, ge=0)
    maximo: int = Field(default=10, ge=1)


class Character(BaseModel):
    """Ficha de personagem."""

    model_config = ConfigDict(extra="allow")  
    # Fazer os campos extras

    nome: str = "Aventureiro"
    raca: str = "Humano"
    classe: str = "Guerreiro"
    nivel: int = Field(default=1, ge=1, le=20)
    atributos: Attributes = Field(default_factory=Attributes)
    pontos_de_vida: HitPoints = Field(default_factory=HitPoints)
    pericias: list[str] = Field(default_factory=list)
    equipamento: list[str] = Field(default_factory=list)