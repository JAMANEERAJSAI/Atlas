from atlas.providers.mock_provider import MockMarketProvider


def test_mock_provider_returns_deterministic_values():
    provider = MockMarketProvider()
    provider.connect()

    ltp = provider.get_ltp("RELIANCE")
    historical = provider.get_historical_data("RELIANCE")

    assert isinstance(ltp, float)
    assert len(historical) == 5
    assert historical[0]["symbol"] == "RELIANCE"
    assert historical[0]["close"] >= historical[0]["low"]


def test_mock_provider_subscription_tracking():
    provider = MockMarketProvider()
    provider.subscribe(["RELIANCE", "TCS"])

    assert "RELIANCE" in provider.subscribed_symbols
    assert "TCS" in provider.subscribed_symbols

    provider.unsubscribe(["RELIANCE"])

    assert "RELIANCE" not in provider.subscribed_symbols
    assert "TCS" in provider.subscribed_symbols
