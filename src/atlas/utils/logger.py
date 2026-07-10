"""Centralized logging helpers for ATLAS."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from loguru import logger as loguru_logger

LOG_DIR = Path(__file__).resolve().parents[3] / "data" / "logs"
LOG_PATH = LOG_DIR / "atlas_{time:YYYY-MM-DD}.log"
_CONFIGURED = False


def _ensure_log_dir() -> None:
    """Create the log directory if it does not already exist."""

    LOG_DIR.mkdir(parents=True, exist_ok=True)


def _configure_logger() -> None:
    """Configure the shared Loguru logger once."""

    global _CONFIGURED
    if _CONFIGURED:
        return

    _ensure_log_dir()
    loguru_logger.remove()
    loguru_logger.add(
        sys.stdout,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} | {message}",
        level="INFO",
    )
    loguru_logger.add(
        str(LOG_PATH),
        rotation="1 day",
        retention="30 days",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} | {message}",
        level="INFO",
    )
    _CONFIGURED = True


def get_logger(name: str) -> Any:
    """Return a Loguru logger bound to the provided module name."""

    _configure_logger()
    return loguru_logger.bind(name=name)


__all__ = ["get_logger"]
