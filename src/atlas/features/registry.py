"""Feature calculator registration for ATLAS."""

from __future__ import annotations

from dataclasses import dataclass, field

from atlas.features.base import FeatureCalculator


@dataclass
class FeatureRegistry:
    """In-memory registry of feature calculators keyed by feature ID."""

    _calculators: dict[str, FeatureCalculator] = field(default_factory=dict)

    def register(self, calculator: FeatureCalculator) -> None:
        """Register a calculator and reject duplicate feature IDs."""

        feature_id = calculator.metadata.feature_id
        if feature_id in self._calculators:
            raise ValueError(f"Feature calculator already registered: {feature_id}")
        self._calculators[feature_id] = calculator

    def get(self, feature_id: str) -> FeatureCalculator:
        """Return a registered calculator by feature ID."""

        try:
            return self._calculators[feature_id]
        except KeyError as exc:
            raise KeyError(f"Feature calculator not registered: {feature_id}") from exc

    def list_registered(self) -> tuple[FeatureCalculator, ...]:
        """Return registered calculators in insertion order."""

        return tuple(self._calculators.values())

    def contains(self, feature_id: str) -> bool:
        """Return whether a feature ID is registered."""

        return feature_id in self._calculators
