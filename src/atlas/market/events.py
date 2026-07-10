"""Internal market event types and publisher for ATLAS."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Callable, TypeAlias

from atlas.providers.base import Candle


class ConnectionStatus(str, Enum):
    """Supported provider connection states."""

    CONNECTED = "connected"
    DISCONNECTED = "disconnected"


@dataclass(frozen=True)
class PriceUpdate:
    """Event emitted when the latest price for a symbol changes."""

    symbol: str
    price: float
    timestamp: datetime


@dataclass(frozen=True)
class CandleUpdate:
    """Event emitted when candle data is received for a symbol."""

    symbol: str
    candle: Candle
    timestamp: datetime


@dataclass(frozen=True)
class ConnectionStatusUpdate:
    """Event emitted when provider connection status changes."""

    status: ConnectionStatus
    timestamp: datetime


MarketEvent: TypeAlias = PriceUpdate | CandleUpdate | ConnectionStatusUpdate
EventHandler: TypeAlias = Callable[[MarketEvent], None]


@dataclass
class MarketEventBus:
    """Lightweight in-process publisher for market engine events."""

    _handlers: list[EventHandler] = field(default_factory=list)

    def subscribe(self, handler: EventHandler) -> None:
        """Register a handler for future market events."""

        self._handlers.append(handler)

    def publish(self, event: MarketEvent) -> None:
        """Publish an event to all registered handlers."""

        for handler in tuple(self._handlers):
            handler(event)

    def clear(self) -> None:
        """Remove all event handlers."""

        self._handlers.clear()
