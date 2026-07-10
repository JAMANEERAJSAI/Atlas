"""Rolling in-memory buffers for cleaned market data."""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Deque, Generic, TypeVar

T = TypeVar("T")


@dataclass
class RollingBuffer(Generic[T]):
    """Symbol-partitioned fixed-size buffer for recent market data."""

    maxlen: int = 500
    _items: dict[str, Deque[T]] = field(default_factory=lambda: defaultdict(deque))

    def append(self, symbol: str, item: T) -> None:
        """Append an item to a symbol buffer, discarding older items as needed."""

        buffer = self._items[symbol]
        if buffer.maxlen != self.maxlen:
            self._items[symbol] = deque(buffer, maxlen=self.maxlen)
            buffer = self._items[symbol]
        buffer.append(item)

    def get(self, symbol: str) -> list[T]:
        """Return buffered items for a symbol in insertion order."""

        return list(self._items.get(symbol, ()))

    def latest(self, symbol: str) -> T | None:
        """Return the latest buffered item for a symbol, if present."""

        items = self._items.get(symbol)
        if not items:
            return None
        return items[-1]

    def clear(self) -> None:
        """Remove all buffered data."""

        self._items.clear()
