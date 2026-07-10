"""Feature Engine foundation package for ATLAS."""

from atlas.features.base import FeatureCalculator
from atlas.features.metadata import FeatureCategory, FeatureMetadata
from atlas.features.registry import FeatureRegistry

__all__ = [
    "FeatureCalculator",
    "FeatureCategory",
    "FeatureMetadata",
    "FeatureRegistry",
]
