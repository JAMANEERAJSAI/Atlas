"""Provider-agnostic Market Engine for ATLAS."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from atlas.market.events import (
    CandleUpdate,
    ConnectionStatus,
    ConnectionStatusUpdate,
    EventHandler,
    MarketEventBus,
    PriceUpdate,
)
from atlas.market.state import MarketState, PriceSnapshot
from atlas.providers.base import HistoricalData, MarketDataProvider


@dataclass
class MarketEngine:
    """Single entry point for market data access inside ATLAS.

    The engine owns one market data provider, manages connection lifecycle,
    caches latest prices, and emits internal market events without exposing
    provider-specific details to downstream modules.
    """

    provider: MarketDataProvider
    state: MarketState = field(default_factory=MarketState)
    _event_bus: MarketEventBus = field(default_factory=MarketEventBus)

    def start(self) -> None:
        """Connect to the provider and mark the engine as connected."""

        self.provider.connect()
        self.state.set_connection_status(ConnectionStatus.CONNECTED)
        self._event_bus.publish(
            ConnectionStatusUpdate(
                status=ConnectionStatus.CONNECTED,
                timestamp=datetime.utcnow(),
            )
        )

    def stop(self) -> None:
        """Disconnect from the provider and mark the engine as disconnected."""

        self.provider.disconnect()
        self.state.set_connection_status(ConnectionStatus.DISCONNECTED)
        self._event_bus.publish(
            ConnectionStatusUpdate(
                status=ConnectionStatus.DISCONNECTED,
                timestamp=datetime.utcnow(),
            )
        )

    def get_latest_price(self, symbol: str) -> float:
        """Return the latest price for a symbol and refresh the in-memory cache."""

        price = self.provider.get_ltp(symbol)
        timestamp = datetime.utcnow()
        self.state.update_price(symbol=symbol, price=price, timestamp=timestamp)
        self._event_bus.publish(
            PriceUpdate(symbol=symbol, price=price, timestamp=timestamp)
        )
        return price

    def get_cached_price(self, symbol: str) -> PriceSnapshot | None:
        """Return the cached price snapshot for a symbol without provider access."""

        return self.state.get_price(symbol)

    def get_historical_data(self, symbol: str) -> HistoricalData:
        """Return historical candles and publish candle update events internally."""

        historical_data = self.provider.get_historical_data(symbol)
        timestamp = datetime.utcnow()
        for candle in historical_data.candles:
            self._event_bus.publish(
                CandleUpdate(symbol=symbol, candle=candle, timestamp=timestamp)
            )
        return historical_data

    def subscribe_events(self, handler: EventHandler) -> None:
        """Subscribe an internal handler to Market Engine events."""

        self._event_bus.subscribe(handler)
