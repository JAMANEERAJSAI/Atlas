"""Timeframe aggregation utilities for market candles."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta

from atlas.pipeline.normalizer import NormalizedCandle


@dataclass(frozen=True)
class Timeframe:
    """Fixed candle aggregation interval."""

    minutes: int

    def __post_init__(self) -> None:
        """Ensure the timeframe can aggregate at least one minute."""

        if self.minutes <= 0:
            raise ValueError("timeframe minutes must be positive")

    @property
    def duration(self) -> timedelta:
        """Return the timeframe as a timedelta."""

        return timedelta(minutes=self.minutes)


@dataclass
class TimeframeAggregator:
    """Build higher timeframe candles from lower timeframe candles."""

    timeframe: Timeframe
    _pending: dict[str, list[NormalizedCandle]] = field(default_factory=dict)

    def add_candle(self, candle: NormalizedCandle) -> NormalizedCandle | None:
        """Add a candle and return an aggregate when the bucket is complete."""

        bucket = self._pending.setdefault(candle.symbol, [])
        if not bucket:
            bucket.append(candle)
            return None

        bucket_start = bucket[0].timestamp
        if candle.timestamp < bucket_start + self.timeframe.duration:
            bucket.append(candle)
            return None

        aggregate = self._build(candle.symbol, bucket_start, bucket)
        self._pending[candle.symbol] = [candle]
        return aggregate

    def flush(self, symbol: str) -> NormalizedCandle | None:
        """Return and clear the current incomplete aggregate for a symbol."""

        bucket = self._pending.pop(symbol, [])
        if not bucket:
            return None
        return self._build(symbol, bucket[0].timestamp, bucket)

    def _build(
        self,
        symbol: str,
        timestamp: datetime,
        candles: list[NormalizedCandle],
    ) -> NormalizedCandle:
        return NormalizedCandle(
            symbol=symbol,
            timestamp=timestamp,
            open=candles[0].open,
            high=max(candle.high for candle in candles),
            low=min(candle.low for candle in candles),
            close=candles[-1].close,
            volume=sum(candle.volume for candle in candles),
        )
