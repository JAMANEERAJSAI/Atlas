"""SQLite database setup for ATLAS."""

from __future__ import annotations

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from atlas.config.settings import get_settings
from atlas.storage.models import Base


def get_engine() -> Engine:
    """Create and return the SQLAlchemy engine for the configured SQLite database."""

    settings = get_settings()
    db_path = Path(settings.database_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    database_url = f"sqlite:///{db_path.resolve()}"
    return create_engine(database_url, future=True)


def get_session_factory() -> sessionmaker[Session]:
    """Return a configured session factory for the ATLAS database."""

    return sessionmaker(bind=get_engine(), expire_on_commit=False, future=True)


def init_db() -> None:
    """Create the SQLite database and all ATLAS tables."""

    Base.metadata.create_all(bind=get_engine())


__all__ = ["get_engine", "get_session_factory", "init_db"]
