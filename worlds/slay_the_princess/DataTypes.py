from typing import NamedTuple, Optional, Callable, Any
from BaseClasses import Location, CollectionState
from enum import Enum

class MemoryGroup(Enum):
    WOOD = "Wood"
    CABIN = "Cabin"
    BASEMENT = "Basement"
    FIND = "Find"

    BEFORE = "Before"
    HEART = "Heart"
    EYES = "Eyes"

    DESTROY = "Destroy"

    OTHER = "Other"
all_memory_group_name = [group.value for group in MemoryGroup]

class SlayThePrincessLocation(Location):
    game = "Slay The Princess"


class SlayThePrincessLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    rule: Optional[Callable[[CollectionState, Any], bool]] = None
    group: MemoryGroup = MemoryGroup.OTHER