"""Canonical Data Pipeline between Market Engine and downstream systems."""

from __future__ import annotations

from dataclasses import dataclass, field

from atlas.market.engine import MarketEngine
from atlas.market.events import CandleUpdate, EventHandler, MarketEvent, MarketEventBus, PriceUpdate
from atlas.pipeline.buffer import RollingBuffer
from atlas.pipeline.normalizer import (
    MarketDataNormalizer,
    NormalizedCandle,
    NormalizedMarketData,
    NormalizedPrice,
)
from atlas.pipeline.timeframe import TimeframeAggregator
from atlas.pipeline.validator import MarketDataValidator
from atlas.utils.logger import get_logger

logger = get_logger(__name__)


@dataclass
class DataPipeline:
    """Prepare market data for downstream ATLAS systems.

    The pipeline subscribes to Market Engine events, validates and normalizes
    incoming data, maintains rolling buffers, builds optional higher timeframe
    candles, and publishes cleaned events for consumers such as future feature
    engines or backtesters.
    """

    market_engine: MarketEngine
    validator: MarketDataValidator = field(default_factory=MarketDataValidator)
    normalizer: MarketDataNormalizer = field(default_factory=MarketDataNormalizer)
    price_buffer: RollingBuffer[NormalizedPrice] = field(default_factory=RollingBuffer)
    candle_buffer: RollingBuffer[NormalizedCandle] = field(default_factory=RollingBuffer)
    timeframe_aggregator: TimeframeAggregator | None = None
    _event_bus: MarketEventBus = field(default_factory=MarketEventBus)
    _started: bool = False

    def start(self) -> None:
        """Subscribe the pipeline to the Market Engine event stream."""

        if self._started:
            return
        self.market_engine.subscribe_events(self.process_event)
        self._started = True
        logger.info("Data Pipeline started")

    def process_event(self, event: MarketEvent) -> NormalizedMarketData | None:
        """Validate, normalize, buffer, and publish a Market Engine event."""

        validation = self.validator.validate(event)
        if not validation.is_valid:
            logger.warning(f"Rejected market data: {validation.reason}")
            return None

        normalized = self.normalizer.normalize(event)
        if normalized is None:
            return None

        if isinstance(normalized, NormalizedPrice):
            self.price_buffer.append(normalized.symbol, normalized)
            self._event_bus.publish(
                PriceUpdate(
                    symbol=normalized.symbol,
                    price=normalized.price,
                    timestamp=normalized.timestamp,
                )
            )
            return normalized

        self.candle_buffer.append(normalized.symbol, normalized)
        self._event_bus.publish(
            CandleUpdate(
                symbol=normalized.symbol,
                candle=normalized.to_candle(),
                timestamp=normalized.timestamp,
            )
        )

        if self.timeframe_aggregator is not None:
            aggregate = self.timeframe_aggregator.add_candle(normalized)
            if aggregate is not None:
                self.candle_buffer.append(aggregate.symbol, aggregate)
                self._event_bus.publish(
                    CandleUpdate(
                        symbol=aggregate.symbol,
                        candle=aggregate.to_candle(),
                        timestamp=aggregate.timestamp,
                    )
                )

        return normalized

    def subscribe_clean_data(self, handler: EventHandler) -> None:
        """Subscribe a downstream consumer to cleaned pipeline events."""

        self._event_bus.subscribe(handler)

    def latest_price(self, symbol: str) -> NormalizedPrice | None:
        """Return the latest normalized price for a symbol."""

        return self.price_buffer.latest(symbol.strip().upper())

    def latest_candle(self, symbol: str) -> NormalizedCandle | None:
        """Return the latest normalized candle for a symbol."""

        return self.candle_buffer.latest(symbol.strip().upper())

