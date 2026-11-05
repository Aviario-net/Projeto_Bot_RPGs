# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2025 Aviario

"""Persistência da ficha em JSON."""
import json
from pathlib import Path

from rpgbot.features.character.models import Character


class CharacterRepository:
    """Salva/carrega fichas em arquivos JSON."""

    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _path(self, user_id: int) -> Path:
        return self.base_dir / f"{user_id}.json"

    def existe(self, user_id: int) -> bool:
        return self._path(user_id).exists()

    def carregar(self, user_id: int) -> Character | None:
        path = self._path(user_id)
        if not path.exists():
            return None
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return Character.model_validate(data)

    def salvar(self, user_id: int, character: Character) -> None:
        path = self._path(user_id)
        with path.open("w", encoding="utf-8") as f:
            json.dump(
                character.model_dump(mode="json"),
                f,
                ensure_ascii=False,
                indent=2,
            )

    def deletar(self, user_id: int) -> bool:
        path = self._path(user_id)
        if path.exists():
            path.unlink()
            return True
        return False