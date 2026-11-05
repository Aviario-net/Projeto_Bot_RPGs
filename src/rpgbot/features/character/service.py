# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2025 Aviario

"""Regras de negócio da ficha."""
from rpgbot.features.character.models import Character
from rpgbot.features.character.repository import CharacterRepository


class CharacterService:
    """Orquestra operações sobre fichas."""

    def __init__(self, repo: CharacterRepository) -> None:
        self.repo = repo

    def criar(self, user_id: int) -> Character:
        """Cria uma ficha padrão se ainda não existir; devolve a existente se já houver."""
        existente = self.repo.carregar(user_id)
        if existente:
            return existente
        nova = Character()
        self.repo.salvar(user_id, nova)
        return nova

    def obter(self, user_id: int) -> Character | None:
        return self.repo.carregar(user_id)

    def salvar(self, user_id: int, character: Character) -> None:
        self.repo.salvar(user_id, character)

    def deletar(self, user_id: int) -> bool:
        return self.repo.deletar(user_id)