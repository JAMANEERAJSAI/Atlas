from dataclasses import FrozenInstanceError
from datetime import datetime

import pytest

from atlas.features import (
    FeatureCategory,
    FeatureMetadata,
    FeatureSnapshot,
    FeatureValue,
    FeatureValueStatus,
)


def make_metadata(feature_id: str = "trend.test.1m") -> FeatureMetadata:
    return FeatureMetadata(
        feature_id=feature_id,
        name="Test Feature",
        category=FeatureCategory.TREND,
        timeframe="1m",
        warmup_period=1,
        description="Test metadata.",
    )


def test_feature_value_creation():
    timestamp = datetime.utcnow()
    metadata = make_metadata()

    feature_value = FeatureValue(
        feature_id="trend.test.1m",
        value=101.25,
        timestamp=timestamp,
        status=FeatureValueStatus.READY,
        metadata=metadata,
    )

    assert feature_value.feature_id == "trend.test.1m"
    assert feature_value.value == 101.25
    assert feature_value.timestamp == timestamp
    assert feature_value.status == FeatureValueStatus.READY
    assert feature_value.metadata is metadata


def test_feature_snapshot_creation():
    timestamp = datetime.utcnow()
    feature_value = FeatureValue(
        feature_id="trend.test.1m",
        value=101.25,
        timestamp=timestamp,
        status=FeatureValueStatus.READY,
        metadata=make_metadata(),
    )

    snapshot = FeatureSnapshot(
        symbol="NIFTY",
        timeframe="1m",
        timestamp=timestamp,
        values=(feature_value,),
        engine_version="1.0.0",
    )

    assert snapshot.symbol == "NIFTY"
    assert snapshot.timeframe == "1m"
    assert snapshot.timestamp == timestamp
    assert snapshot.values == (feature_value,)
    assert snapshot.get_value("trend.test.1m") is feature_value


def test_feature_snapshot_is_immutable():
    snapshot = FeatureSnapshot(
        symbol="NIFTY",
        timeframe="1m",
        timestamp=datetime.utcnow(),
    )

    with pytest.raises(FrozenInstanceError):
        snapshot.symbol = "BANKNIFTY"


def test_feature_snapshot_supports_multiple_feature_values():
    timestamp = datetime.utcnow()
    first = FeatureValue(
        feature_id="trend.test.1m",
        value=101.25,
        timestamp=timestamp,
        status=FeatureValueStatus.READY,
        metadata=make_metadata("trend.test.1m"),
    )
    second = FeatureValue(
        feature_id="momentum.test.1m",
        value=55.0,
        timestamp=timestamp,
        status=FeatureValueStatus.READY,
        metadata=FeatureMetadata(
            feature_id="momentum.test.1m",
            name="Momentum Test Feature",
            category=FeatureCategory.MOMENTUM,
            timeframe="1m",
        ),
    )

    snapshot = FeatureSnapshot(
        symbol="NIFTY",
        timeframe="1m",
        timestamp=timestamp,
        values=(first, second),
    )

    assert len(snapshot.values) == 2
    assert snapshot.get_value("trend.test.1m") is first
    assert snapshot.get_value("momentum.test.1m") is second


def test_feature_snapshot_warmup_flag():
    snapshot = FeatureSnapshot(
        symbol="NIFTY",
        timeframe="1m",
        timestamp=datetime.utcnow(),
        is_warmup=True,
    )

    assert snapshot.is_warmup
