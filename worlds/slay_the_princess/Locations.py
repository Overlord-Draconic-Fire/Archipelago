from typing import Dict, NamedTuple, Optional, Callable, Any

from BaseClasses import Location, CollectionState
from .Names import ItemName, LocationName, RegionName
from .Rules import max_reachable_vessels

offset: int = 63900000
specials: int = 10
mirror: int = 20
princess: int = 100
heart: int = 200
memories: int = 10000
entry = " ENTRY"


class SlayThePrincessLocation(Location):
    game = "Slay The Princess"


class SlayThePrincessLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    rule: Optional[Callable[[CollectionState, Any], bool]] = None


others_location_data_table: Dict[str, SlayThePrincessLocationData] = {
    LocationName.win: SlayThePrincessLocationData(RegionName.win),
}

mirror_location_data_table: Dict[str, SlayThePrincessLocationData] = {
    LocationName.mirror1: SlayThePrincessLocationData(
        RegionName.space_between, offset + mirror + 0,
        rule=lambda state, world: max_reachable_vessels(state, world) > 0),
    LocationName.mirror2: SlayThePrincessLocationData(
        RegionName.space_between, offset + mirror + 1,
        rule=lambda state, world: (max_reachable_vessels(state, world) > 1) and state.has(ItemName.goddess, world.player)),
    LocationName.mirror3: SlayThePrincessLocationData(
        RegionName.space_between, offset + mirror + 2,
        rule=lambda state, world: (max_reachable_vessels(state, world) > 2) and state.has(ItemName.goddess, world.player)),
    LocationName.mirror4: SlayThePrincessLocationData(
        RegionName.space_between, offset + mirror + 3,
        rule=lambda state, world: (max_reachable_vessels(state, world) > 3) and state.has(ItemName.goddess, world.player)),
    LocationName.mirror5: SlayThePrincessLocationData(
        RegionName.space_between, offset + mirror + 4,
        rule=lambda state, world: (max_reachable_vessels(state, world) > 4) and state.has(ItemName.goddess, world.player)),
}

princess_location_data_table: Dict[str, SlayThePrincessLocationData] = {
    LocationName.adversary: SlayThePrincessLocationData(RegionName.adversary + entry, offset + princess + 0),
    LocationName.tower: SlayThePrincessLocationData(RegionName.tower + entry, offset + princess + 1),
    LocationName.spectre: SlayThePrincessLocationData(RegionName.spectre + entry, offset + princess + 2),
    LocationName.nightmare: SlayThePrincessLocationData(RegionName.nightmare + entry, offset + princess + 3),
    LocationName.razor: SlayThePrincessLocationData(RegionName.razor + entry, offset + princess + 4),
    LocationName.beast: SlayThePrincessLocationData(RegionName.beast + entry, offset + princess + 5),
    LocationName.witch: SlayThePrincessLocationData(RegionName.witch + entry, offset + princess + 6),
    LocationName.stranger: SlayThePrincessLocationData(RegionName.stranger + entry, offset + princess + 7),
    LocationName.prisoner: SlayThePrincessLocationData(RegionName.prisoner + entry, offset + princess + 8),
    LocationName.damsel: SlayThePrincessLocationData(RegionName.damsel + entry, offset + princess + 9),

    LocationName.needle: SlayThePrincessLocationData(RegionName.needle + entry, offset + princess + 10),
    LocationName.fury: SlayThePrincessLocationData(RegionName.fury + entry, offset + princess + 11),
    LocationName.apotheosis: SlayThePrincessLocationData(RegionName.apotheosis + entry, offset + princess + 12),
    LocationName.dragon: SlayThePrincessLocationData(RegionName.dragon + entry, offset + princess + 13),
    LocationName.wraith: SlayThePrincessLocationData(RegionName.wraith + entry, offset + princess + 14),
    LocationName.clarity: SlayThePrincessLocationData(RegionName.clarity + entry, offset + princess + 15),
    LocationName.den: SlayThePrincessLocationData(RegionName.den + entry, offset + princess + 16),
    LocationName.wild: SlayThePrincessLocationData(RegionName.wild + entry, offset + princess + 17),
    LocationName.thorn: SlayThePrincessLocationData(RegionName.thorn + entry, offset + princess + 18),
    LocationName.cage: SlayThePrincessLocationData(RegionName.cage + entry, offset + princess + 19),
    LocationName.grey: SlayThePrincessLocationData(RegionName.grey + entry, offset + princess + 20),
    LocationName.happily: SlayThePrincessLocationData(RegionName.happily + entry, offset + princess + 21),

    LocationName.goddess: SlayThePrincessLocationData(RegionName.goddess + entry, offset + princess + 22)
}

global_chapter_location_data_table: Dict[str, SlayThePrincessLocationData] = {
    LocationName.chap2: SlayThePrincessLocationData(RegionName.chap2, offset + princess + 23),
    LocationName.chap3: SlayThePrincessLocationData(RegionName.chap3, offset + princess + 24)
}

heart_location_data_table: Dict[str, SlayThePrincessLocationData] = {
    LocationName.adversary_heart: SlayThePrincessLocationData(RegionName.adversary_blade, offset + heart + 0),
    LocationName.tower_heart: SlayThePrincessLocationData(RegionName.tower, offset + heart + 1),
    LocationName.spectre_heart: SlayThePrincessLocationData(RegionName.spectre, offset + heart + 2),
    LocationName.nightmare_heart: SlayThePrincessLocationData(RegionName.nightmare, offset + heart + 3),
    LocationName.beast_heart: SlayThePrincessLocationData(RegionName.beast, offset + heart + 4),
    LocationName.witch_heart: SlayThePrincessLocationData(RegionName.witch, offset + heart + 5),
    LocationName.stranger_heart: SlayThePrincessLocationData(RegionName.stranger_blade, offset + heart + 6),
    LocationName.prisoner_heart_patient: SlayThePrincessLocationData(RegionName.prisoner, offset + heart + 7),
    LocationName.prisoner_heart_clever: SlayThePrincessLocationData(RegionName.prisoner, offset + heart + 8),
    LocationName.damsel_heart_gentle: SlayThePrincessLocationData(RegionName.damsel, offset + heart + 9),
    LocationName.damsel_heart_pliable: SlayThePrincessLocationData(RegionName.damsel, offset + heart + 10),

    LocationName.needle_heart: SlayThePrincessLocationData(RegionName.needle, offset + heart + 11),
    LocationName.fury_heart_weathered: SlayThePrincessLocationData(RegionName.fury_weathered_heart, offset + heart + 12),
    LocationName.fury_heart_unwound: SlayThePrincessLocationData(RegionName.fury, offset + heart + 13),
    LocationName.apotheosis_heart: SlayThePrincessLocationData(RegionName.apotheosis, offset + heart + 14),
    LocationName.dragon_heart_main: SlayThePrincessLocationData(RegionName.dragon, offset + heart + 15),
    LocationName.dragon_heart_stencil: SlayThePrincessLocationData(RegionName.dragon, offset + heart + 16),
    LocationName.wraith_heart: SlayThePrincessLocationData(RegionName.wraith, offset + heart + 17),
    LocationName.clarity_heart: SlayThePrincessLocationData(RegionName.clarity_blade, offset + heart + 18),
    LocationName.den_heart: SlayThePrincessLocationData(RegionName.den, offset + heart + 19),
    LocationName.wild_heart_curious: SlayThePrincessLocationData(RegionName.wild, offset + heart + 20),
    LocationName.wild_heart_scarred: SlayThePrincessLocationData(RegionName.wild_blade, offset + heart + 21),
    LocationName.thorn_heart: SlayThePrincessLocationData(RegionName.thorn, offset + heart + 22),
    LocationName.cage_heart_open: SlayThePrincessLocationData(RegionName.cage, offset + heart + 23),
    LocationName.grey_heart_bright: SlayThePrincessLocationData(RegionName.grey_burned, offset + heart + 24),
    LocationName.grey_heart_deep: SlayThePrincessLocationData(RegionName.grey_drowned, offset + heart + 25),
    LocationName.happily_heart: SlayThePrincessLocationData(RegionName.happily, offset + heart + 26),

    LocationName.razor_heart_iron: SlayThePrincessLocationData(RegionName.razor_destruction, offset + heart + 27),
    LocationName.razor_heart_free: SlayThePrincessLocationData(RegionName.razor_empty, offset + heart + 28),
}


location_data_table: Dict[str, SlayThePrincessLocationData] = {**others_location_data_table,
                                                               **mirror_location_data_table,
                                                               **princess_location_data_table,
                                                               **global_chapter_location_data_table,
                                                               **heart_location_data_table}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
