"""Base interface for Feature Engine calculators."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Mapping

from atlas.features.metadata import FeatureMetadata


class FeatureCalculator(ABC):
    """Abstract contract for incremental feature calculators.

    Calculators consume clean Data Pipeline events and maintain only the state
    needed to update their feature incrementally. Concrete calculators are not
    responsible for trading, persistence, raw market data, or engine runtime.
    """

    @property
    @abstractmethod
    def metadata(self) -> FeatureMetadata:
        """Return immutable metadata describing this calculator."""

    @abstractmethod
    def initialize(self, context: Mapping[str, Any]) -> None:
        """Prepare the calculator with runtime context before updates begin."""

    @abstractmethod
    def update(self, event: Any) -> Any:
        """Process a clean pipeline event and return an implementation value."""

    @abstractmethod
    def reset(self) -> None:
        """Clear calculator state so it can be reused deterministically."""

    @abstractmethod
    def is_ready(self) -> bool:
        """Return whether the calculator has enough state to produce output."""
