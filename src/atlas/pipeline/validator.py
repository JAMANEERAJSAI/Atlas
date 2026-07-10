"""Validation rules for incoming market data."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from atlas.market.events import CandleUpdate, MarketEvent, PriceUpdate
from atlas.providers.base import Candle


@dataclass(frozen=True)
class ValidationResult:
    """Result of validating one market data event."""

    is_valid: bool
    reason: str | None = None


class MarketDataValidator:
    """Validate raw market events before normalization."""

    def validate(self, event: MarketEvent) -> ValidationResult:
        """Validate a supported market event."""

        if isinstance(event, PriceUpdate):
            return self._validate_price(event)
        if isinstance(event, CandleUpdate):
            return self._validate_candle(event.candle)
        return ValidationResult(is_valid=True)

    def _validate_price(self, event: PriceUpdate) -> ValidationResult:
        if not event.symbol.strip():
            return ValidationResult(False, "symbol is required")
        if event.price <= 0:
            return ValidationResult(False, "price must be positive")
        if not isinstance(event.timestamp, datetime):
            return ValidationResult(False, "timestamp must be a datetime")
        return ValidationResult(True)

    def _validate_candle(self, candle: Candle) -> ValidationResult:
        if not candle.symbol.strip():
            return ValidationResult(False, "symbol is required")
        if min(candle.open, candle.high, candle.low, candle.close) <= 0:
            return ValidationResult(False, "candle prices must be positive")
        if candle.low > min(candle.open, candle.close):
            return ValidationResult(False, "low exceeds candle body")
        if candle.high < max(candle.open, candle.close):
            return ValidationResult(False, "high is below candle body")
        if candle.volume < 0:
            return ValidationResult(False, "volume cannot be negative")
        return ValidationResult(True)
