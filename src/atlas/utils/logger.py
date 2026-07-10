"""Centralized logging helpers for ATLAS."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

from loguru import logger as loguru_logger

LOG_DIR = Path(__file__).resolve().parents[3] / "data" / "logs"
LOG_PATH = LOG_DIR / "atlas_{time:YYYY-MM-DD}.log"


def _ensure_log_dir() -> None:
    """Create the log directory if it does not already exist."""

    LOG_DIR.mkdir(parents=True, exist_ok=True)


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


def get_logger(name: str) -> object:
    """Return a Loguru logger bound to the provided module name."""

    return loguru_logger.bind(name=name)


__all__ = ["get_logger"]
