"""Abstract market data provider interface for ATLAS."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class Quote:
    """Represents a single market quote."""

    symbol: str
    price: float
    timestamp: datetime


@dataclass(frozen=True)
class Candle:
    """Represents a single historical candle."""

    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

    def to_dict(self) -> dict[str, Any]:
        """Return the candle as a dictionary."""

        return asdict(self)


@dataclass(frozen=True)
class HistoricalData:
    """Represents a collection of historical candles."""

    symbol: str
    candles: list[Candle]

    def __len__(self) -> int:
        """Return the number of candles."""

        return len(self.candles)

    def __iter__(self):
        """Iterate over the candles as dictionaries."""

        return iter(self.to_dicts())

    def __getitem__(self, index: int) -> dict[str, Any]:
        """Return a candle as a dictionary at the given index."""

        return self.to_dicts()[index]

    def to_dicts(self) -> list[dict[str, Any]]:
        """Return the underlying candles as dictionaries."""

        return [candle.to_dict() for candle in self.candles]


class MarketDataProvider(ABC):
    """Common interface for market data providers."""

    @abstractmethod
    def connect(self) -> None:
        """Establish a connection to the data source."""

    @abstractmethod
    def disconnect(self) -> None:
        """Close the connection to the data source."""

    @abstractmethod
    def get_ltp(self, symbol: str) -> float:
        """Return the latest traded price for a symbol."""

    @abstractmethod
    def get_historical_data(self, symbol: str) -> HistoricalData:
        """Return historical candle data for a symbol."""

    @abstractmethod
    def subscribe(self, symbols: list[str]) -> None:
        """Subscribe to updates for the provided symbols."""

    @abstractmethod
    def unsubscribe(self, symbols: list[str]) -> None:
        """Unsubscribe from updates for the provided symbols."""
