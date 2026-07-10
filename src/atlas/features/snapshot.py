"""Feature snapshot models for ATLAS."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from atlas.features.value import FeatureValue


@dataclass(frozen=True)
class FeatureSnapshot:
    """Immutable collection of feature values for one symbol and timeframe."""

    symbol: str
    timeframe: str
    timestamp: datetime
    values: tuple[FeatureValue, ...] = field(default_factory=tuple)
    engine_version: str = "1.0.0"
    is_warmup: bool = False

    def __post_init__(self) -> None:
        """Validate snapshot identity fields."""

        if not self.symbol.strip():
            raise ValueError("symbol is required")
        if not self.timeframe.strip():
            raise ValueError("timeframe is required")
        if not self.engine_version.strip():
            raise ValueError("engine_version is required")

    def get_value(self, feature_id: str) -> FeatureValue | None:
        """Return a feature value by ID, if present in the snapshot."""

        for feature_value in self.values:
            if feature_value.feature_id == feature_id:
                return feature_value
        return None
