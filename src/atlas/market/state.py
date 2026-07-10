"""In-memory market state managed by the Market Engine."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from atlas.market.events import ConnectionStatus


@dataclass(frozen=True)
class PriceSnapshot:
    """Latest known price for a market symbol."""

    symbol: str
    price: float
    timestamp: datetime


@dataclass
class MarketState:
    """Mutable in-memory cache of current market data."""

    connection_status: ConnectionStatus = ConnectionStatus.DISCONNECTED
    latest_prices: dict[str, PriceSnapshot] = field(default_factory=dict)

    def set_connection_status(self, status: ConnectionStatus) -> None:
        """Update the current provider connection status."""

        self.connection_status = status

    def update_price(self, symbol: str, price: float, timestamp: datetime) -> PriceSnapshot:
        """Store and return the latest price snapshot for a symbol."""

        snapshot = PriceSnapshot(symbol=symbol, price=price, timestamp=timestamp)
        self.latest_prices[symbol] = snapshot
        return snapshot

    def get_price(self, symbol: str) -> PriceSnapshot | None:
        """Return the cached latest price snapshot for a symbol, if available."""

        return self.latest_prices.get(symbol)
