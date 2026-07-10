"""Feature metadata models for ATLAS."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class FeatureCategory(str, Enum):
    """Supported mathematical and market-structure feature categories."""

    TREND = "trend"
    MOMENTUM = "momentum"
    VOLATILITY = "volatility"
    VOLUME = "volume"
    PATTERN = "pattern"
    STRUCTURE = "structure"


@dataclass(frozen=True)
class FeatureMetadata:
    """Describes a feature calculator and its output contract."""

    feature_id: str
    name: str
    category: FeatureCategory
    timeframe: str
    dependencies: tuple[str, ...] = field(default_factory=tuple)
    warmup_period: int = 0
    version: str = "1.0.0"
    description: str = ""

    def __post_init__(self) -> None:
        """Validate core metadata fields."""

        if not self.feature_id.strip():
            raise ValueError("feature_id is required")
        if not self.name.strip():
            raise ValueError("name is required")
        if not self.timeframe.strip():
            raise ValueError("timeframe is required")
        if self.warmup_period < 0:
            raise ValueError("warmup_period cannot be negative")
