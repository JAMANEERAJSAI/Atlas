"""Normalize market events into ATLAS internal models."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from atlas.market.events import CandleUpdate, MarketEvent, PriceUpdate
from atlas.providers.base import Candle


@dataclass(frozen=True)
class NormalizedPrice:
    """Canonical latest price model used inside ATLAS."""

    symbol: str
    price: float
    timestamp: datetime


@dataclass(frozen=True)
class NormalizedCandle:
    """Canonical OHLCV candle model used inside ATLAS."""

    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

    def to_candle(self) -> Candle:
        """Convert the normalized candle to the existing provider candle model."""

        return Candle(
            symbol=self.symbol,
            timestamp=self.timestamp,
            open=self.open,
            high=self.high,
            low=self.low,
            close=self.close,
            volume=self.volume,
        )


NormalizedMarketData = NormalizedPrice | NormalizedCandle


class MarketDataNormalizer:
    """Convert supported market events into canonical ATLAS models."""

    def normalize(self, event: MarketEvent) -> NormalizedMarketData | None:
        """Normalize a supported market event, or ignore unsupported events."""

        if isinstance(event, PriceUpdate):
            return NormalizedPrice(
                symbol=event.symbol.strip().upper(),
                price=float(event.price),
                timestamp=event.timestamp,
            )
        if isinstance(event, CandleUpdate):
            candle = event.candle
            return NormalizedCandle(
                symbol=candle.symbol.strip().upper(),
                timestamp=candle.timestamp,
                open=float(candle.open),
                high=float(candle.high),
                low=float(candle.low),
                close=float(candle.close),
                volume=int(candle.volume),
            )
        return None
