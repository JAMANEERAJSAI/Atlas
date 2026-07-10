from datetime import datetime, timedelta

from atlas.market.events import CandleUpdate, PriceUpdate
from atlas.pipeline import (
    DataPipeline,
    MarketDataNormalizer,
    MarketDataValidator,
    NormalizedCandle,
    RollingBuffer,
    Timeframe,
    TimeframeAggregator,
)
from atlas.providers.base import Candle
from atlas.providers.mock_provider import MockMarketProvider
from atlas.market import MarketEngine


def test_validator_rejects_invalid_price():
    validator = MarketDataValidator()
    event = PriceUpdate(symbol="NIFTY", price=0.0, timestamp=datetime.utcnow())

    result = validator.validate(event)

    assert not result.is_valid
    assert result.reason == "price must be positive"


def test_buffer_keeps_latest_items_with_max_length():
    buffer = RollingBuffer[int](maxlen=2)

    buffer.append("NIFTY", 1)
    buffer.append("NIFTY", 2)
    buffer.append("NIFTY", 3)

    assert buffer.get("NIFTY") == [2, 3]
    assert buffer.latest("NIFTY") == 3


def test_normalizer_canonicalizes_price_symbol():
    normalizer = MarketDataNormalizer()
    event = PriceUpdate(symbol=" nifty ", price=101.5, timestamp=datetime.utcnow())

    normalized = normalizer.normalize(event)

    assert normalized is not None
    assert normalized.symbol == "NIFTY"
    assert normalized.price == 101.5


def test_timeframe_aggregator_builds_higher_timeframe_candle():
    start = datetime(2026, 7, 10, 9, 15)
    aggregator = TimeframeAggregator(timeframe=Timeframe(minutes=5))
    first = NormalizedCandle("NIFTY", start, 100.0, 102.0, 99.0, 101.0, 100)
    second = NormalizedCandle("NIFTY", start + timedelta(minutes=1), 101.0, 103.0, 100.0, 102.0, 150)
    next_bucket = NormalizedCandle("NIFTY", start + timedelta(minutes=5), 102.0, 104.0, 101.0, 103.0, 200)

    assert aggregator.add_candle(first) is None
    assert aggregator.add_candle(second) is None
    aggregate = aggregator.add_candle(next_bucket)

    assert aggregate is not None
    assert aggregate.open == 100.0
    assert aggregate.high == 103.0
    assert aggregate.low == 99.0
    assert aggregate.close == 102.0
    assert aggregate.volume == 250


def test_pipeline_accepts_market_engine_events_and_publishes_clean_data():
    engine = MarketEngine(provider=MockMarketProvider())
    pipeline = DataPipeline(market_engine=engine)
    cleaned_events = []
    pipeline.subscribe_clean_data(cleaned_events.append)
    pipeline.start()
    engine.start()

    price = engine.get_latest_price("nifty")

    latest = pipeline.latest_price("NIFTY")
    assert latest is not None
    assert latest.symbol == "NIFTY"
    assert latest.price == price
    assert isinstance(cleaned_events[-1], PriceUpdate)


def test_pipeline_buffers_normalized_candles():
    engine = MarketEngine(provider=MockMarketProvider())
    pipeline = DataPipeline(market_engine=engine)
    timestamp = datetime.utcnow()
    candle = Candle(
        symbol=" banknifty ",
        timestamp=timestamp,
        open=100.0,
        high=101.0,
        low=99.0,
        close=100.5,
        volume=1000,
    )

    normalized = pipeline.process_event(
        CandleUpdate(symbol="banknifty", candle=candle, timestamp=timestamp)
    )

    latest = pipeline.latest_candle("BANKNIFTY")
    assert normalized is not None
    assert latest is not None
    assert latest.symbol == "BANKNIFTY"
    assert latest.close == 100.5
