"""Feature value models for ATLAS."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any

from atlas.features.metadata import FeatureMetadata


class FeatureValueStatus(str, Enum):
    """Quality status for one computed feature value."""

    READY = "ready"
    WARMING_UP = "warming_up"
    INVALID = "invalid"
    STALE = "stale"


@dataclass(frozen=True)
class FeatureValue:
    """Represents one computed feature at a specific timestamp."""

    feature_id: str
    value: Any
    timestamp: datetime
    status: FeatureValueStatus
    metadata: FeatureMetadata | None = None

    def __post_init__(self) -> None:
        """Validate core feature value fields."""

        if not self.feature_id.strip():
            raise ValueError("feature_id is required")
