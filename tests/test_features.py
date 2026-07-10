from dataclasses import dataclass
from datetime import datetime
from typing import Any, Mapping

import pytest

from atlas.features import (
    FeatureCalculator,
    FeatureCategory,
    FeatureMetadata,
    FeatureRegistry,
)
from atlas.pipeline.normalizer import NormalizedPrice


@dataclass
class DummyCalculator(FeatureCalculator):
    _metadata: FeatureMetadata
    updates: int = 0
    initialized: bool = False

    @property
    def metadata(self) -> FeatureMetadata:
        return self._metadata

    def initialize(self, context: Mapping[str, Any]) -> None:
        self.initialized = True

    def update(self, event: NormalizedPrice) -> float:
        self.updates += 1
        return event.price

    def reset(self) -> None:
        self.updates = 0
        self.initialized = False

    def is_ready(self) -> bool:
        return self.updates >= self.metadata.warmup_period


def make_metadata(feature_id: str = "trend.test.1m") -> FeatureMetadata:
    return FeatureMetadata(
        feature_id=feature_id,
        name="Test Feature",
        category=FeatureCategory.TREND,
        timeframe="1m",
        dependencies=("source.close",),
        warmup_period=1,
        version="1.0.0",
        description="Test-only feature metadata.",
    )


def test_feature_calculator_interface_lifecycle():
    calculator = DummyCalculator(_metadata=make_metadata())
    event = NormalizedPrice(symbol="NIFTY", price=100.0, timestamp=datetime.utcnow())

    assert not calculator.is_ready()

    calculator.initialize({})
    value = calculator.update(100.0)

    assert calculator.initialized
    assert value == 100.0
    assert calculator.is_ready()

    calculator.reset()

    assert not calculator.initialized
    assert not calculator.is_ready()


def test_feature_metadata_creation():
    metadata = make_metadata()

    assert metadata.feature_id == "trend.test.1m"
    assert metadata.category == FeatureCategory.TREND
    assert metadata.timeframe == "1m"
    assert metadata.dependencies == ("source.close",)
    assert metadata.warmup_period == 1


def test_feature_registry_registers_and_lists_calculators():
    registry = FeatureRegistry()
    calculator = DummyCalculator(_metadata=make_metadata())

    registry.register(calculator)

    assert registry.contains("trend.test.1m")
    assert registry.list_registered() == (calculator,)


def test_feature_registry_rejects_duplicate_feature_ids():
    registry = FeatureRegistry()
    first = DummyCalculator(_metadata=make_metadata())
    second = DummyCalculator(_metadata=make_metadata())

    registry.register(first)

    with pytest.raises(ValueError, match="already registered"):
        registry.register(second)


def test_feature_registry_lookup_returns_calculator():
    registry = FeatureRegistry()
    calculator = DummyCalculator(_metadata=make_metadata())
    registry.register(calculator)

    assert registry.get("trend.test.1m") is calculator

    with pytest.raises(KeyError, match="not registered"):
        registry.get("missing.feature")


