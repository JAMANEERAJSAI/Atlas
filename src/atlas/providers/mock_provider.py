"""Offline mock market data provider for ATLAS."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta

from atlas.providers.base import Candle, HistoricalData, MarketDataProvider, Quote


@dataclass
class MockMarketProvider(MarketDataProvider):
    """Deterministic offline provider that mimics simple market data."""

    base_price: float = 100.0
    drift: float = 0.25
    subscribed_symbols: set[str] = field(default_factory=set)
    _connected: bool = False

    def connect(self) -> None:
        """Mark the provider as connected."""

        self._connected = True

    def disconnect(self) -> None:
        """Mark the provider as disconnected."""

        self._connected = False

    def get_ltp(self, symbol: str) -> float:
        """Return a deterministic latest price for the symbol."""

        if not self._connected:
            raise RuntimeError("Provider is not connected")

        seed = sum(ord(ch) for ch in symbol)
        movement = ((seed % 7) - 3) * self.drift
        return round(self.base_price + movement, 2)

    def get_historical_data(self, symbol: str) -> HistoricalData:
        """Return realistic-looking OHLC candles for the symbol."""

        if not self._connected:
            raise RuntimeError("Provider is not connected")

        candles: list[Candle] = []
        base = self.get_ltp(symbol)
        start_time = datetime.utcnow().replace(hour=9, minute=15, second=0, microsecond=0)

        for index in range(5):
            candle_time = start_time + timedelta(minutes=index * 15)
            open_price = round(base + index * 0.15, 2)
            close_price = round(open_price + ((index % 3) - 1) * 0.1, 2)
            high_price = round(max(open_price, close_price) + 0.2, 2)
            low_price = round(min(open_price, close_price) - 0.2, 2)
            candles.append(
                Candle(
                    symbol=symbol,
                    timestamp=candle_time,
                    open=open_price,
                    high=high_price,
                    low=low_price,
                    close=close_price,
                    volume=1000 + index * 100,
                )
            )

        return HistoricalData(symbol=symbol, candles=candles)

    def subscribe(self, symbols: list[str]) -> None:
        """Subscribe to a list of symbols."""

        self.subscribed_symbols.update(symbols)

    def unsubscribe(self, symbols: list[str]) -> None:
        """Unsubscribe from a list of symbols."""

        for symbol in symbols:
            self.subscribed_symbols.discard(symbol)
