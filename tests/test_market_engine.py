from atlas.market import ConnectionStatus, ConnectionStatusUpdate, MarketEngine, PriceUpdate
from atlas.market.events import CandleUpdate
from atlas.providers.mock_provider import MockMarketProvider


def test_market_engine_start_and_stop_updates_connection_state():
    provider = MockMarketProvider()
    engine = MarketEngine(provider=provider)
    events = []
    engine.subscribe_events(events.append)

    engine.start()

    assert engine.state.connection_status == ConnectionStatus.CONNECTED
    assert isinstance(events[-1], ConnectionStatusUpdate)
    assert events[-1].status == ConnectionStatus.CONNECTED

    engine.stop()

    assert engine.state.connection_status == ConnectionStatus.DISCONNECTED
    assert isinstance(events[-1], ConnectionStatusUpdate)
    assert events[-1].status == ConnectionStatus.DISCONNECTED


def test_market_engine_retrieves_and_caches_latest_price():
    provider = MockMarketProvider()
    engine = MarketEngine(provider=provider)
    events = []
    engine.subscribe_events(events.append)
    engine.start()

    price = engine.get_latest_price("NIFTY")
    cached_price = engine.get_cached_price("NIFTY")

    assert price == provider.get_ltp("NIFTY")
    assert cached_price is not None
    assert cached_price.symbol == "NIFTY"
    assert cached_price.price == price
    assert isinstance(events[-1], PriceUpdate)
    assert events[-1].symbol == "NIFTY"
    assert events[-1].price == price


def test_market_engine_publishes_candle_updates():
    provider = MockMarketProvider()
    engine = MarketEngine(provider=provider)
    events = []
    engine.subscribe_events(events.append)
    engine.start()

    historical_data = engine.get_historical_data("BANKNIFTY")
    candle_events = [event for event in events if isinstance(event, CandleUpdate)]

    assert len(historical_data) == 5
    assert len(candle_events) == len(historical_data)
    assert all(event.symbol == "BANKNIFTY" for event in candle_events)
