from typing import NamedTuple, Optional, Callable, Any
from BaseClasses import Location, CollectionState


class SlayThePrincessLocation(Location):
    game = "Slay The Princess"


class SlayThePrincessLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    rule: Optional[Callable[[CollectionState, Any], bool]] = None