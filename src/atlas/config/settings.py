"""Configuration loading for ATLAS."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

from dotenv import load_dotenv

REQUIRED_ENV_VARS = (
    "ANGEL_API_KEY",
    "ANGEL_CLIENT_ID",
    "DATABASE_PATH",
    "LOG_LEVEL",
)


@dataclass(frozen=True)
class Settings:
    """Validated application settings loaded from the environment."""

    angel_api_key: str
    angel_client_id: str
    database_path: str
    log_level: str


def load_settings(env: Mapping[str, str] | None = None) -> Settings:
    """Load and validate settings from environment variables and a .env file."""

    if env is None:
        env_path = Path(__file__).resolve().parents[3] / ".env"
        load_dotenv(dotenv_path=env_path, override=False)
        env = os.environ

    missing = [name for name in REQUIRED_ENV_VARS if not str(env.get(name, "")).strip()]
    if missing:
        missing_names = ", ".join(missing)
        raise ValueError(
            f"Missing required environment variables: {missing_names}. "
            "Set them in your environment or in the project .env file."
        )

    return Settings(
        angel_api_key=str(env["ANGEL_API_KEY"]).strip(),
        angel_client_id=str(env["ANGEL_CLIENT_ID"]).strip(),
        database_path=str(env["DATABASE_PATH"]).strip(),
        log_level=str(env["LOG_LEVEL"]).strip(),
    )


def get_settings() -> Settings:
    """Return the validated ATLAS settings."""

    return load_settings()


__all__ = ["Settings", "get_settings", "load_settings"]
