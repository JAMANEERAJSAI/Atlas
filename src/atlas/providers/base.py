"""Abstract market data provider interface for ATLAS."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


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
    def get_historical_data(self, symbol: str) -> list[dict[str, Any]]:
        """Return historical candle data for a symbol."""

    @abstractmethod
    def subscribe(self, symbols: list[str]) -> None:
        """Subscribe to updates for the provided symbols."""

    @abstractmethod
    def unsubscribe(self, symbols: list[str]) -> None:
        """Unsubscribe from updates for the provided symbols."""
