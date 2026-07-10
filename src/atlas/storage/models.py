"""Minimal SQLAlchemy models for ATLAS storage."""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for all ATLAS ORM models."""


class MarketTick(Base):
    """Placeholder market tick table for future data ingestion."""

    __tablename__ = "market_ticks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


class Candle(Base):
    """Placeholder candle table for future OHLC data."""

    __tablename__ = "candles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


class Prediction(Base):
    """Placeholder prediction table for future model outputs."""

    __tablename__ = "predictions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


class TradeJournal(Base):
    """Placeholder trade journal table for future notes."""

    __tablename__ = "trade_journals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
