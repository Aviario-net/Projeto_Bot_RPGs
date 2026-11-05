# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2025 Aviario

"""Configuração central do bot. Único ponto que lê variáveis de ambiente."""
from pathlib import Path
from typing import Literal

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuração tipada, validada no boot.

    Se faltar alguma variável obrigatória, o processo NÃO inicia.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    discord_token: SecretStr
    discord_owner_id: int
    dev_guild_id: int | None = None

    env: Literal["development", "staging", "production"] = "development"
    log_level: str = "INFO"

    database_url: str = "sqlite+aiosqlite:///data/db.sqlite"

    data_dir: Path = Field(default=Path("data"))


settings = Settings()