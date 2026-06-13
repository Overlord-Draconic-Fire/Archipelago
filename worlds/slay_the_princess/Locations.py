from typing import Dict, NamedTuple, Optional, Callable, Any

from BaseClasses import Location, CollectionState
from .DataTypes import SlayThePrincessLocationData
from .Names import ItemName, LocationName, RegionName
from .Rules import has_blade
from .TokenSystem import max_reachable_vessels, can_reach_oblivion

offset: int = 63900000
specials: int = 10
mirror: int = 20
princess: int = 100
heart: int = 200
memories: int = 10000
entry = " ENTRY"


others_location_data_table: Dict[str, SlayThePrincessLocationData] = {
    LocationName.win: SlayThePrincessLocationData(RegionName.win),
}

mirror_location_data_table: Dict[str, SlayThePrincessLocationData] = {
    LocationName.mirror1: SlayThePrincessLocationData(
        RegionName.space_between, offset + mirror + 0,
        rule=lambda state, world: max_reachable_vessels(state, world, 1)),
    LocationName.mirror2: SlayThePrincessLocationData(
        RegionName.space_between, offset + mirror + 1,
        rule=lambda state, world: (max_reachable_vessels(state, world, 2) and state.has(ItemName.goddess, world.player))),
    LocationName.mirror3: SlayThePrincessLocationData(
        RegionName.space_between, offset + mirror + 2,
        rule=lambda state, world: (max_reachable_vessels(state, world, 3) and state.has(ItemName.goddess, world.player))),
    LocationName.mirror4: SlayThePrincessLocationData(
        RegionName.space_between, offset + mirror + 3,
        rule=lambda state, world: (max_reachable_vessels(state, world, 4) and state.has(ItemName.goddess, world.player))),
    LocationName.mirror5: SlayThePrincessLocationData(
        RegionName.space_between, offset + mirror + 4,
        rule=lambda state, world: (max_reachable_vessels(state, world, 5) and state.has(ItemName.goddess, world.player))),
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
    LocationName.dragon_heart_stencil: SlayThePrincessLocationData(RegionName.dragon_fuse, offset + heart + 16),
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

gallery_location_data_table: Dict[str, SlayThePrincessLocationData] = {
    LocationName.gallery_princess[1]: SlayThePrincessLocationData(RegionName.one, offset + memories + 1),
    LocationName.gallery_princess[2]: SlayThePrincessLocationData(RegionName.one, offset + memories + 2),
    LocationName.gallery_princess[3]: SlayThePrincessLocationData(RegionName.one, offset + memories + 3),
    LocationName.gallery_princess[4]: SlayThePrincessLocationData(RegionName.one, offset + memories + 4),
    LocationName.gallery_princess[5]: SlayThePrincessLocationData(RegionName.tower, offset + memories + 5),
    LocationName.gallery_princess[6]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 6),
    LocationName.gallery_princess[7]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 7),
    LocationName.gallery_princess[8]: SlayThePrincessLocationData(RegionName.prisoner, offset + memories + 8),
    LocationName.gallery_princess[9]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 9),
    LocationName.gallery_princess[10]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 10),
    LocationName.gallery_princess[11]: SlayThePrincessLocationData(RegionName.witch, offset + memories + 11),
    LocationName.gallery_princess[12]: SlayThePrincessLocationData(RegionName.beast, offset + memories + 12),
    LocationName.gallery_princess[13]: SlayThePrincessLocationData(RegionName.adversary, offset + memories + 13),
    LocationName.gallery_princess[14]: SlayThePrincessLocationData(RegionName.stranger, offset + memories + 14),
    LocationName.gallery_princess[15]: SlayThePrincessLocationData(RegionName.one_blade, offset + memories + 15),
    LocationName.gallery_princess[16]: SlayThePrincessLocationData(RegionName.one_blade, offset + memories + 16),
    LocationName.gallery_princess[17]: SlayThePrincessLocationData(RegionName.one_blade, offset + memories + 17),
    LocationName.gallery_princess[18]: SlayThePrincessLocationData(RegionName.one_blade, offset + memories + 18),

    LocationName.gallery_spaceBetween[1]: SlayThePrincessLocationData(RegionName.space_between, offset + memories + 101),
    LocationName.gallery_spaceBetween[2]: SlayThePrincessLocationData(RegionName.space_between, offset + memories + 102),
    LocationName.gallery_spaceBetween[3]: SlayThePrincessLocationData(RegionName.space_between, offset + memories + 103),
    LocationName.gallery_spaceBetween[4]: SlayThePrincessLocationData(
        RegionName.space_between, offset + memories + 104,
        rule=lambda state, world: max_reachable_vessels(state, world, 1)),
    LocationName.gallery_spaceBetween[5]: SlayThePrincessLocationData(
        RegionName.space_between, offset + memories + 105,
        rule=lambda state, world: (max_reachable_vessels(state, world, 2) and state.has(ItemName.goddess, world.player))),
    LocationName.gallery_spaceBetween[6]: SlayThePrincessLocationData(
        RegionName.space_between, offset + memories + 106,
        rule=lambda state, world: (max_reachable_vessels(state, world, 3) and state.has(ItemName.goddess, world.player))),
    LocationName.gallery_spaceBetween[7]: SlayThePrincessLocationData(
        RegionName.space_between, offset + memories + 107,
        rule=lambda state, world: (max_reachable_vessels(state, world, 4) and state.has(ItemName.goddess, world.player))),
    LocationName.gallery_spaceBetween[8]: SlayThePrincessLocationData(
        RegionName.space_between, offset + memories + 108,
        rule=lambda state, world: (max_reachable_vessels(state, world, 5) and state.has(ItemName.goddess, world.player))),
    LocationName.gallery_spaceBetween[9]: SlayThePrincessLocationData(
        RegionName.space_between, offset + memories + 109,
        rule=lambda state, world: can_reach_oblivion(state, world)),

    LocationName.gallery_finale[1]: SlayThePrincessLocationData(RegionName.goddess, offset + memories + 201),
    LocationName.gallery_finale[2]: SlayThePrincessLocationData(RegionName.goddess, offset + memories + 202),
    LocationName.gallery_finale[3]: SlayThePrincessLocationData(RegionName.goddess, offset + memories + 203),
    LocationName.gallery_finale[4]: SlayThePrincessLocationData(RegionName.goddess, offset + memories + 204),
    LocationName.gallery_finale[5]: SlayThePrincessLocationData(RegionName.goddess, offset + memories + 205),
    LocationName.gallery_finale[6]: SlayThePrincessLocationData(RegionName.goddess, offset + memories + 206),
    LocationName.gallery_finale[7]: SlayThePrincessLocationData(RegionName.goddess_blade, offset + memories + 207),
    LocationName.gallery_finale[8]: SlayThePrincessLocationData(RegionName.goddess_blade, offset + memories + 208),
    LocationName.gallery_finale[9]: SlayThePrincessLocationData(RegionName.goddess, offset + memories + 209),
    LocationName.gallery_finale[10]: SlayThePrincessLocationData(RegionName.goddess, offset + memories + 210),
    LocationName.gallery_finale[11]: SlayThePrincessLocationData(
        RegionName.goddess, offset + memories + 211,
        rule=lambda state, world: state.can_reach_region(RegionName.stranger_blade, world.player)),
    LocationName.gallery_finale[12]: SlayThePrincessLocationData(
        RegionName.goddess_blade, offset + memories + 212,
        rule=lambda state, world: state.can_reach_region(RegionName.stranger_blade, world.player)),
    LocationName.gallery_finale[13]: SlayThePrincessLocationData(
        RegionName.goddess, offset + memories + 213,
        rule=lambda state, world: state.can_reach_region(RegionName.stranger_blade, world.player)),
    LocationName.gallery_finale[14]: SlayThePrincessLocationData(
        RegionName.goddess_blade, offset + memories + 214,
        rule=lambda state, world: state.can_reach_region(RegionName.stranger_blade, world.player)),
    LocationName.gallery_finale[15]: SlayThePrincessLocationData(RegionName.goddess_blade, offset + memories + 215),
    LocationName.gallery_finale[16]: SlayThePrincessLocationData(RegionName.new_world, offset + memories + 216),
    LocationName.gallery_finale[17]: SlayThePrincessLocationData(RegionName.new_world, offset + memories + 217),
    LocationName.gallery_finale[18]: SlayThePrincessLocationData(RegionName.new_world, offset + memories + 218),
    LocationName.gallery_finale[19]: SlayThePrincessLocationData(RegionName.new_world, offset + memories + 219),
    LocationName.gallery_finale[20]: SlayThePrincessLocationData(RegionName.new_world, offset + memories + 220),

    LocationName.gallery_adversary[1]: SlayThePrincessLocationData(RegionName.adversary, offset + memories + 301),
    LocationName.gallery_adversary[2]: SlayThePrincessLocationData(RegionName.adversary, offset + memories + 302),
    LocationName.gallery_adversary[3]: SlayThePrincessLocationData(RegionName.adversary_blade, offset + memories + 303),
    LocationName.gallery_adversary[4]: SlayThePrincessLocationData(RegionName.adversary, offset + memories + 304),
    LocationName.gallery_adversary[5]: SlayThePrincessLocationData(RegionName.adversary_blade, offset + memories + 305),
    LocationName.gallery_adversary[6]: SlayThePrincessLocationData(RegionName.adversary, offset + memories + 306),
    LocationName.gallery_adversary[7]: SlayThePrincessLocationData(RegionName.adversary_blade, offset + memories + 307),
    LocationName.gallery_adversary[8]: SlayThePrincessLocationData(RegionName.adversary_blade, offset + memories + 308),
    LocationName.gallery_adversary[9]: SlayThePrincessLocationData(RegionName.adversary_blade, offset + memories + 309),
    LocationName.gallery_adversary[10]: SlayThePrincessLocationData(RegionName.adversary_blade, offset + memories + 310),
    LocationName.gallery_adversary[11]: SlayThePrincessLocationData(RegionName.adversary, offset + memories + 311),
    LocationName.gallery_adversary[12]: SlayThePrincessLocationData(RegionName.adversary, offset + memories + 312),
    LocationName.gallery_adversary[13]: SlayThePrincessLocationData(RegionName.adversary, offset + memories + 313),
    LocationName.gallery_adversary[14]: SlayThePrincessLocationData(RegionName.adversary_blade, offset + memories + 314),
    LocationName.gallery_adversary[15]: SlayThePrincessLocationData(RegionName.adversary_blade, offset + memories + 315),
    LocationName.gallery_adversary[16]: SlayThePrincessLocationData(RegionName.adversary_blade, offset + memories + 316),
    LocationName.gallery_adversary[17]: SlayThePrincessLocationData(RegionName.adversary_blade, offset + memories + 317),
    LocationName.gallery_adversary[18]: SlayThePrincessLocationData(
        RegionName.adversary_blade, offset + memories + 318,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_adversary[19]: SlayThePrincessLocationData(
        RegionName.adversary_blade, offset + memories + 319,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_adversary[20]: SlayThePrincessLocationData(
        RegionName.adversary_blade, offset + memories + 320,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_tower[1]: SlayThePrincessLocationData(RegionName.tower, offset + memories + 401),
    LocationName.gallery_tower[2]: SlayThePrincessLocationData(RegionName.tower, offset + memories + 402),
    LocationName.gallery_tower[3]: SlayThePrincessLocationData(RegionName.tower_blade, offset + memories + 403),
    LocationName.gallery_tower[4]: SlayThePrincessLocationData(RegionName.tower_blade, offset + memories + 404),
    LocationName.gallery_tower[5]: SlayThePrincessLocationData(RegionName.tower, offset + memories + 405),
    LocationName.gallery_tower[6]: SlayThePrincessLocationData(RegionName.tower, offset + memories + 406),
    LocationName.gallery_tower[7]: SlayThePrincessLocationData(RegionName.tower, offset + memories + 407),
    LocationName.gallery_tower[8]: SlayThePrincessLocationData(RegionName.tower_blade, offset + memories + 408),
    LocationName.gallery_tower[9]: SlayThePrincessLocationData(RegionName.tower_blade, offset + memories + 409),
    LocationName.gallery_tower[10]: SlayThePrincessLocationData(RegionName.tower_blade, offset + memories + 410),
    LocationName.gallery_tower[11]: SlayThePrincessLocationData(
        RegionName.tower, offset + memories + 411,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_tower[12]: SlayThePrincessLocationData(
        RegionName.tower, offset + memories + 412,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_tower[13]: SlayThePrincessLocationData(
        RegionName.tower, offset + memories + 413,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_spectre[1]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 501),
    LocationName.gallery_spectre[2]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 502),
    LocationName.gallery_spectre[3]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 503),
    LocationName.gallery_spectre[4]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 504),
    LocationName.gallery_spectre[5]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 505),
    LocationName.gallery_spectre[6]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 506),
    LocationName.gallery_spectre[7]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 507),
    LocationName.gallery_spectre[8]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 508),
    LocationName.gallery_spectre[9]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 509),
    LocationName.gallery_spectre[10]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 510),
    LocationName.gallery_spectre[11]: SlayThePrincessLocationData(RegionName.spectre_blade, offset + memories + 511),
    LocationName.gallery_spectre[12]: SlayThePrincessLocationData(RegionName.spectre_blade, offset + memories + 512),
    LocationName.gallery_spectre[13]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 513),
    LocationName.gallery_spectre[14]: SlayThePrincessLocationData(RegionName.spectre_blade, offset + memories + 514),
    LocationName.gallery_spectre[15]: SlayThePrincessLocationData(RegionName.spectre, offset + memories + 515),
    LocationName.gallery_spectre[16]: SlayThePrincessLocationData(
        RegionName.spectre, offset + memories + 516,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_spectre[17]: SlayThePrincessLocationData(
        RegionName.spectre, offset + memories + 517,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_spectre[18]: SlayThePrincessLocationData(
        RegionName.spectre, offset + memories + 518,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_nightmare[1]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 601),
    LocationName.gallery_nightmare[2]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 602),
    LocationName.gallery_nightmare[3]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 603),
    LocationName.gallery_nightmare[4]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 604),
    LocationName.gallery_nightmare[5]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 605),
    LocationName.gallery_nightmare[6]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 606),
    LocationName.gallery_nightmare[7]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 607),
    LocationName.gallery_nightmare[8]: SlayThePrincessLocationData(RegionName.nightmare_blade, offset + memories + 608),
    LocationName.gallery_nightmare[9]: SlayThePrincessLocationData(RegionName.nightmare_blade, offset + memories + 609),
    LocationName.gallery_nightmare[10]: SlayThePrincessLocationData(RegionName.nightmare_blade, offset + memories + 610),
    LocationName.gallery_nightmare[11]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 611),
    LocationName.gallery_nightmare[12]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 612),
    LocationName.gallery_nightmare[13]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 613),
    LocationName.gallery_nightmare[14]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 614),
    LocationName.gallery_nightmare[15]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 615),
    LocationName.gallery_nightmare[16]: SlayThePrincessLocationData(RegionName.nightmare, offset + memories + 616),
    LocationName.gallery_nightmare[17]: SlayThePrincessLocationData(
        RegionName.nightmare, offset + memories + 617,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_nightmare[18]: SlayThePrincessLocationData(
        RegionName.nightmare, offset + memories + 618,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_nightmare[19]: SlayThePrincessLocationData(
        RegionName.nightmare, offset + memories + 619,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_razor[1]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 701),
    LocationName.gallery_razor[2]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 702),
    LocationName.gallery_razor[3]: SlayThePrincessLocationData(RegionName.razor_blade, offset + memories + 703),
    LocationName.gallery_razor[4]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 704),
    LocationName.gallery_razor[5]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 705),
    LocationName.gallery_razor[6]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 706),
    LocationName.gallery_razor[7]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 707),
    LocationName.gallery_razor[8]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 708),
    LocationName.gallery_razor[9]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 709),
    LocationName.gallery_razor[10]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 710),
    LocationName.gallery_razor[11]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 711),
    LocationName.gallery_razor[12]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 712),
    LocationName.gallery_razor[13]: SlayThePrincessLocationData(RegionName.razor_blade, offset + memories + 713),
    LocationName.gallery_razor[14]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 714),
    LocationName.gallery_razor[15]: SlayThePrincessLocationData(RegionName.razor, offset + memories + 715),
    LocationName.gallery_razor[16]: SlayThePrincessLocationData(
        RegionName.razor_blade, offset + memories + 716,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_razor[17]: SlayThePrincessLocationData(
        RegionName.razor_blade, offset + memories + 717,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_razor[18]: SlayThePrincessLocationData(
        RegionName.razor, offset + memories + 718,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_razor[19]: SlayThePrincessLocationData(
        RegionName.razor, offset + memories + 719,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_razor[20]: SlayThePrincessLocationData(
        RegionName.razor, offset + memories + 720,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_beast[1]: SlayThePrincessLocationData(RegionName.beast, offset + memories + 801),
    LocationName.gallery_beast[2]: SlayThePrincessLocationData(RegionName.beast, offset + memories + 802),
    LocationName.gallery_beast[3]: SlayThePrincessLocationData(RegionName.beast, offset + memories + 803),
    LocationName.gallery_beast[4]: SlayThePrincessLocationData(RegionName.beast_blade, offset + memories + 804),
    LocationName.gallery_beast[5]: SlayThePrincessLocationData(RegionName.beast, offset + memories + 805),
    LocationName.gallery_beast[6]: SlayThePrincessLocationData(RegionName.beast_blade, offset + memories + 806),
    LocationName.gallery_beast[7]: SlayThePrincessLocationData(RegionName.beast_blade, offset + memories + 807),
    LocationName.gallery_beast[8]: SlayThePrincessLocationData(RegionName.beast_blade, offset + memories + 808),
    LocationName.gallery_beast[9]: SlayThePrincessLocationData(RegionName.beast, offset + memories + 809),
    LocationName.gallery_beast[10]: SlayThePrincessLocationData(RegionName.beast, offset + memories + 810),
    LocationName.gallery_beast[11]: SlayThePrincessLocationData(RegionName.beast, offset + memories + 811),
    LocationName.gallery_beast[12]: SlayThePrincessLocationData(RegionName.beast, offset + memories + 812),
    LocationName.gallery_beast[13]: SlayThePrincessLocationData(RegionName.beast_blade, offset + memories + 813),
    LocationName.gallery_beast[14]: SlayThePrincessLocationData(RegionName.beast, offset + memories + 814),
    LocationName.gallery_beast[15]: SlayThePrincessLocationData(
        RegionName.beast, offset + memories + 815,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_beast[16]: SlayThePrincessLocationData(
        RegionName.beast, offset + memories + 816,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_beast[17]: SlayThePrincessLocationData(
        RegionName.beast, offset + memories + 817,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_witch[1]: SlayThePrincessLocationData(RegionName.witch, offset + memories + 901),
    LocationName.gallery_witch[2]: SlayThePrincessLocationData(RegionName.witch, offset + memories + 902),
    LocationName.gallery_witch[3]: SlayThePrincessLocationData(RegionName.witch_blade, offset + memories + 903),
    LocationName.gallery_witch[4]: SlayThePrincessLocationData(RegionName.witch_blade, offset + memories + 904),
    LocationName.gallery_witch[5]: SlayThePrincessLocationData(RegionName.witch_blade, offset + memories + 905),
    LocationName.gallery_witch[6]: SlayThePrincessLocationData(RegionName.witch_blade, offset + memories + 906),
    LocationName.gallery_witch[7]: SlayThePrincessLocationData(RegionName.witch_blade, offset + memories + 907),
    LocationName.gallery_witch[8]: SlayThePrincessLocationData(RegionName.witch_blade, offset + memories + 908),
    LocationName.gallery_witch[9]: SlayThePrincessLocationData(RegionName.witch_blade, offset + memories + 909),
    LocationName.gallery_witch[10]: SlayThePrincessLocationData(RegionName.witch, offset + memories + 910),
    LocationName.gallery_witch[11]: SlayThePrincessLocationData(RegionName.witch, offset + memories + 911),
    LocationName.gallery_witch[12]: SlayThePrincessLocationData(RegionName.witch, offset + memories + 912),
    LocationName.gallery_witch[13]: SlayThePrincessLocationData(RegionName.witch, offset + memories + 913),
    LocationName.gallery_witch[14]: SlayThePrincessLocationData(RegionName.witch, offset + memories + 914),
    LocationName.gallery_witch[15]: SlayThePrincessLocationData(RegionName.witch, offset + memories + 915),
    LocationName.gallery_witch[16]: SlayThePrincessLocationData(RegionName.witch_blade, offset + memories + 916),
    LocationName.gallery_witch[17]: SlayThePrincessLocationData(
        RegionName.witch, offset + memories + 917,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_witch[18]: SlayThePrincessLocationData(
        RegionName.witch, offset + memories + 918,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_witch[19]: SlayThePrincessLocationData(
        RegionName.witch, offset + memories + 919,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),
    LocationName.gallery_witch[20]: SlayThePrincessLocationData(
        RegionName.witch, offset + memories + 920,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_stranger[1]: SlayThePrincessLocationData(RegionName.stranger, offset + memories + 1001),
    LocationName.gallery_stranger[2]: SlayThePrincessLocationData(RegionName.stranger, offset + memories + 1002),
    LocationName.gallery_stranger[3]: SlayThePrincessLocationData(RegionName.stranger, offset + memories + 1003),
    LocationName.gallery_stranger[4]: SlayThePrincessLocationData(RegionName.stranger, offset + memories + 1004),
    LocationName.gallery_stranger[5]: SlayThePrincessLocationData(RegionName.stranger, offset + memories + 1005),
    LocationName.gallery_stranger[6]: SlayThePrincessLocationData(RegionName.stranger_blade, offset + memories + 1006),
    LocationName.gallery_stranger[7]: SlayThePrincessLocationData(RegionName.stranger_blade, offset + memories + 1007),
    LocationName.gallery_stranger[8]: SlayThePrincessLocationData(RegionName.stranger_blade, offset + memories + 1008),
    LocationName.gallery_stranger[9]: SlayThePrincessLocationData(RegionName.stranger_blade, offset + memories + 1009),
    LocationName.gallery_stranger[10]: SlayThePrincessLocationData(
        RegionName.stranger_blade, offset + memories + 1010,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_stranger[11]: SlayThePrincessLocationData(
        RegionName.stranger_blade, offset + memories + 1011,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_stranger[12]: SlayThePrincessLocationData(
        RegionName.stranger_blade, offset + memories + 1012,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_prisoner[1]: SlayThePrincessLocationData(RegionName.prisoner, offset + memories + 1101),
    LocationName.gallery_prisoner[2]: SlayThePrincessLocationData(RegionName.prisoner, offset + memories + 1102),
    LocationName.gallery_prisoner[3]: SlayThePrincessLocationData(RegionName.prisoner, offset + memories + 1103),
    LocationName.gallery_prisoner[4]: SlayThePrincessLocationData(RegionName.prisoner, offset + memories + 1104),
    LocationName.gallery_prisoner[5]: SlayThePrincessLocationData(RegionName.prisoner, offset + memories + 1105),
    LocationName.gallery_prisoner[6]: SlayThePrincessLocationData(RegionName.prisoner, offset + memories + 1106),
    LocationName.gallery_prisoner[7]: SlayThePrincessLocationData(RegionName.prisoner, offset + memories + 1107),
    LocationName.gallery_prisoner[8]: SlayThePrincessLocationData(RegionName.prisoner, offset + memories + 1108),
    LocationName.gallery_prisoner[9]: SlayThePrincessLocationData(RegionName.prisoner_blade, offset + memories + 1109),
    LocationName.gallery_prisoner[10]: SlayThePrincessLocationData(RegionName.prisoner_blade, offset + memories + 1110),
    LocationName.gallery_prisoner[11]: SlayThePrincessLocationData(RegionName.prisoner_blade, offset + memories + 1111),
    LocationName.gallery_prisoner[12]: SlayThePrincessLocationData(RegionName.prisoner, offset + memories + 1112),
    LocationName.gallery_prisoner[13]: SlayThePrincessLocationData(
        RegionName.prisoner, offset + memories + 1113,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_prisoner[14]: SlayThePrincessLocationData(
        RegionName.prisoner, offset + memories + 1114,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_prisoner[15]: SlayThePrincessLocationData(
        RegionName.prisoner, offset + memories + 1115,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_prisoner[16]: SlayThePrincessLocationData(
        RegionName.prisoner, offset + memories + 1116,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_prisoner[17]: SlayThePrincessLocationData(
        RegionName.prisoner, offset + memories + 1117,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_damsel[1]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 1201),
    LocationName.gallery_damsel[2]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 1202),
    LocationName.gallery_damsel[3]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 1203),
    LocationName.gallery_damsel[4]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 1204),
    LocationName.gallery_damsel[5]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 1205),
    LocationName.gallery_damsel[6]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 1206),
    LocationName.gallery_damsel[7]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 1207),
    LocationName.gallery_damsel[8]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 1208),
    LocationName.gallery_damsel[9]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 1209),
    LocationName.gallery_damsel[10]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 1210),
    LocationName.gallery_damsel[11]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 1211),
    LocationName.gallery_damsel[12]: SlayThePrincessLocationData(RegionName.damsel_blade, offset + memories + 1212),
    LocationName.gallery_damsel[13]: SlayThePrincessLocationData(RegionName.damsel_blade, offset + memories + 1213),
    LocationName.gallery_damsel[14]: SlayThePrincessLocationData(RegionName.damsel_blade, offset + memories + 1214),
    LocationName.gallery_damsel[15]: SlayThePrincessLocationData(RegionName.damsel_blade, offset + memories + 1215),
    LocationName.gallery_damsel[16]: SlayThePrincessLocationData(RegionName.damsel, offset + memories + 1216),
    LocationName.gallery_damsel[17]: SlayThePrincessLocationData(
        RegionName.damsel, offset + memories + 1217,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_damsel[18]: SlayThePrincessLocationData(
        RegionName.damsel, offset + memories + 1218,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_damsel[19]: SlayThePrincessLocationData(
        RegionName.damsel, offset + memories + 1219,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_damsel[20]: SlayThePrincessLocationData(
        RegionName.damsel, offset + memories + 1220,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_needle[1]: SlayThePrincessLocationData(RegionName.needle, offset + memories + 1301),
    LocationName.gallery_needle[2]: SlayThePrincessLocationData(RegionName.needle, offset + memories + 1302),
    LocationName.gallery_needle[3]: SlayThePrincessLocationData(RegionName.needle, offset + memories + 1303),
    LocationName.gallery_needle[4]: SlayThePrincessLocationData(RegionName.needle, offset + memories + 1304),
    LocationName.gallery_needle[5]: SlayThePrincessLocationData(RegionName.needle_blade, offset + memories + 1305),
    LocationName.gallery_needle[6]: SlayThePrincessLocationData(RegionName.needle_blade, offset + memories + 1306),
    LocationName.gallery_needle[7]: SlayThePrincessLocationData(RegionName.needle, offset + memories + 1307),
    LocationName.gallery_needle[8]: SlayThePrincessLocationData(RegionName.needle, offset + memories + 1308),
    LocationName.gallery_needle[9]: SlayThePrincessLocationData(RegionName.needle_hunted_blade, offset + memories + 1309),
    LocationName.gallery_needle[10]: SlayThePrincessLocationData(RegionName.needle_hunted_blade, offset + memories + 1310),
    LocationName.gallery_needle[11]: SlayThePrincessLocationData(RegionName.needle_hunted_blade, offset + memories + 1311),
    LocationName.gallery_needle[12]: SlayThePrincessLocationData(RegionName.needle_hunted_blade, offset + memories + 1312),
    LocationName.gallery_needle[13]: SlayThePrincessLocationData(RegionName.needle_hunted_blade, offset + memories + 1313),
    LocationName.gallery_needle[14]: SlayThePrincessLocationData(RegionName.needle_skeptic, offset + memories + 1314),
    LocationName.gallery_needle[15]: SlayThePrincessLocationData(RegionName.needle, offset + memories + 1315),
    LocationName.gallery_needle[16]: SlayThePrincessLocationData(RegionName.needle, offset + memories + 1316),
    LocationName.gallery_needle[17]: SlayThePrincessLocationData(RegionName.needle, offset + memories + 1317),
    LocationName.gallery_needle[18]: SlayThePrincessLocationData(
        RegionName.needle, offset + memories + 1318,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_needle[19]: SlayThePrincessLocationData(
        RegionName.needle, offset + memories + 1319,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_needle[20]: SlayThePrincessLocationData(
        RegionName.needle, offset + memories + 1320,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_fury[1]: SlayThePrincessLocationData(RegionName.fury, offset + memories + 1401),
    LocationName.gallery_fury[2]: SlayThePrincessLocationData(RegionName.fury, offset + memories + 1402),
    LocationName.gallery_fury[3]: SlayThePrincessLocationData(RegionName.fury, offset + memories + 1403),
    LocationName.gallery_fury[4]: SlayThePrincessLocationData(RegionName.fury, offset + memories + 1404),
    LocationName.gallery_fury[5]: SlayThePrincessLocationData(
        RegionName.fury_broken_cold, offset + memories + 1405,
        rule=lambda state, world: has_blade(state, world, ItemName.blade_fury)),
    LocationName.gallery_fury[6]: SlayThePrincessLocationData(RegionName.fury_broken_cold, offset + memories + 1406),
    LocationName.gallery_fury[7]: SlayThePrincessLocationData(RegionName.fury_broken_cold, offset + memories + 1407),
    LocationName.gallery_fury[8]: SlayThePrincessLocationData(RegionName.fury_contrarian, offset + memories + 1408),
    LocationName.gallery_fury[9]: SlayThePrincessLocationData(RegionName.fury_tower, offset + memories + 1409),
    LocationName.gallery_fury[10]: SlayThePrincessLocationData(RegionName.fury_contrarian, offset + memories + 1410),
    LocationName.gallery_fury[11]: SlayThePrincessLocationData(RegionName.fury_contrarian, offset + memories + 1411),
    LocationName.gallery_fury[12]: SlayThePrincessLocationData(RegionName.fury_tower_blade, offset + memories + 1412),
    LocationName.gallery_fury[13]: SlayThePrincessLocationData(RegionName.fury_tower_blade, offset + memories + 1413),
    LocationName.gallery_fury[14]: SlayThePrincessLocationData(RegionName.fury_tower_blade, offset + memories + 1414),
    LocationName.gallery_fury[15]: SlayThePrincessLocationData(RegionName.fury, offset + memories + 1415),
    LocationName.gallery_fury[16]: SlayThePrincessLocationData(RegionName.fury, offset + memories + 1416),
    LocationName.gallery_fury[17]: SlayThePrincessLocationData(RegionName.fury_broken_cold, offset + memories + 1417),
    LocationName.gallery_fury[18]: SlayThePrincessLocationData(
        RegionName.fury, offset + memories + 1418,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_fury[19]: SlayThePrincessLocationData(
        RegionName.fury, offset + memories + 1419,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_fury[20]: SlayThePrincessLocationData(
        RegionName.fury, offset + memories + 1420,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_apotheosis[1]: SlayThePrincessLocationData(RegionName.apotheosis, offset + memories + 1501),
    LocationName.gallery_apotheosis[2]: SlayThePrincessLocationData(RegionName.apotheosis, offset + memories + 1502),
    LocationName.gallery_apotheosis[3]: SlayThePrincessLocationData(RegionName.apotheosis_blade, offset + memories + 1503),
    LocationName.gallery_apotheosis[4]: SlayThePrincessLocationData(RegionName.apotheosis_paranoid_blade, offset + memories + 1504),
    LocationName.gallery_apotheosis[5]: SlayThePrincessLocationData(RegionName.apotheosis_paranoid_blade, offset + memories + 1505),
    LocationName.gallery_apotheosis[6]: SlayThePrincessLocationData(RegionName.apotheosis_paranoid_blade, offset + memories + 1506),
    LocationName.gallery_apotheosis[7]: SlayThePrincessLocationData(RegionName.apotheosis_paranoid_blade, offset + memories + 1507),
    LocationName.gallery_apotheosis[8]: SlayThePrincessLocationData(RegionName.apotheosis, offset + memories + 1508),
    LocationName.gallery_apotheosis[9]: SlayThePrincessLocationData(RegionName.apotheosis_contrarian_blade, offset + memories + 1509),
    LocationName.gallery_apotheosis[10]: SlayThePrincessLocationData(RegionName.apotheosis_contrarian_blade, offset + memories + 1510),
    LocationName.gallery_apotheosis[11]: SlayThePrincessLocationData(RegionName.apotheosis_contrarian_blade, offset + memories + 1511),
    LocationName.gallery_apotheosis[12]: SlayThePrincessLocationData(RegionName.apotheosis, offset + memories + 1512),
    LocationName.gallery_apotheosis[13]: SlayThePrincessLocationData(RegionName.apotheosis, offset + memories + 1513),
    LocationName.gallery_apotheosis[14]: SlayThePrincessLocationData(RegionName.apotheosis, offset + memories + 1514),
    LocationName.gallery_apotheosis[15]: SlayThePrincessLocationData(RegionName.apotheosis, offset + memories + 1515),
    LocationName.gallery_apotheosis[16]: SlayThePrincessLocationData(RegionName.apotheosis, offset + memories + 1516),
    LocationName.gallery_apotheosis[17]: SlayThePrincessLocationData(RegionName.apotheosis, offset + memories + 1517),
    LocationName.gallery_apotheosis[18]: SlayThePrincessLocationData(
        RegionName.apotheosis, offset + memories + 1518,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_apotheosis[19]: SlayThePrincessLocationData(
        RegionName.apotheosis, offset + memories + 1519,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_apotheosis[20]: SlayThePrincessLocationData(
        RegionName.apotheosis, offset + memories + 1520,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_dragon[1]: SlayThePrincessLocationData(RegionName.dragon, offset + memories + 1601),
    LocationName.gallery_dragon[2]: SlayThePrincessLocationData(RegionName.dragon, offset + memories + 1602),
    LocationName.gallery_dragon[3]: SlayThePrincessLocationData(RegionName.dragon, offset + memories + 1603),
    LocationName.gallery_dragon[4]: SlayThePrincessLocationData(RegionName.dragon, offset + memories + 1604),
    LocationName.gallery_dragon[5]: SlayThePrincessLocationData(RegionName.dragon, offset + memories + 1605),
    LocationName.gallery_dragon[6]: SlayThePrincessLocationData(RegionName.dragon, offset + memories + 1606),
    LocationName.gallery_dragon[7]: SlayThePrincessLocationData(RegionName.dragon_kind, offset + memories + 1607),
    LocationName.gallery_dragon[8]: SlayThePrincessLocationData(RegionName.dragon, offset + memories + 1608),
    LocationName.gallery_dragon[9]: SlayThePrincessLocationData(RegionName.dragon, offset + memories + 1609),
    LocationName.gallery_dragon[10]: SlayThePrincessLocationData(RegionName.dragon_harsh, offset + memories + 1610),
    LocationName.gallery_dragon[11]: SlayThePrincessLocationData(RegionName.dragon_harsh, offset + memories + 1611),
    LocationName.gallery_dragon[12]: SlayThePrincessLocationData(RegionName.dragon_kind, offset + memories + 1612),
    LocationName.gallery_dragon[13]: SlayThePrincessLocationData(
        RegionName.dragon_kind, offset + memories + 1613,
        rule=lambda state, world: has_blade(state, world, ItemName.blade_dragon)),
    LocationName.gallery_dragon[14]: SlayThePrincessLocationData(RegionName.dragon_harsh, offset + memories + 1614),
    LocationName.gallery_dragon[15]: SlayThePrincessLocationData(RegionName.dragon_kind, offset + memories + 1615),
    LocationName.gallery_dragon[16]: SlayThePrincessLocationData(RegionName.dragon, offset + memories + 1616),
    LocationName.gallery_dragon[17]: SlayThePrincessLocationData(
        RegionName.dragon, offset + memories + 1617,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_dragon[18]: SlayThePrincessLocationData(
        RegionName.dragon, offset + memories + 1618,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_dragon[19]: SlayThePrincessLocationData(
        RegionName.dragon, offset + memories + 1619,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_dragon[20]: SlayThePrincessLocationData(
        RegionName.dragon, offset + memories + 1620,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_wraith[1]: SlayThePrincessLocationData(RegionName.wraith, offset + memories + 1701),
    LocationName.gallery_wraith[2]: SlayThePrincessLocationData(RegionName.wraith, offset + memories + 1702),
    LocationName.gallery_wraith[3]: SlayThePrincessLocationData(RegionName.wraith, offset + memories + 1703),
    LocationName.gallery_wraith[4]: SlayThePrincessLocationData(RegionName.wraith, offset + memories + 1704),
    LocationName.gallery_wraith[5]: SlayThePrincessLocationData(RegionName.wraith, offset + memories + 1705),
    LocationName.gallery_wraith[6]: SlayThePrincessLocationData(RegionName.wraith, offset + memories + 1706),
    LocationName.gallery_wraith[7]: SlayThePrincessLocationData(RegionName.wraith, offset + memories + 1707),
    LocationName.gallery_wraith[8]: SlayThePrincessLocationData(RegionName.wraith, offset + memories + 1708),
    LocationName.gallery_wraith[9]: SlayThePrincessLocationData(
        RegionName.wraith, offset + memories + 1709,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_wraith[10]: SlayThePrincessLocationData(
        RegionName.wraith, offset + memories + 1710,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_wraith[11]: SlayThePrincessLocationData(
        RegionName.wraith, offset + memories + 1711,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_clarity[1]: SlayThePrincessLocationData(RegionName.clarity, offset + memories + 1801),
    LocationName.gallery_clarity[2]: SlayThePrincessLocationData(RegionName.clarity, offset + memories + 1802),
    LocationName.gallery_clarity[3]: SlayThePrincessLocationData(RegionName.clarity, offset + memories + 1803),
    LocationName.gallery_clarity[4]: SlayThePrincessLocationData(RegionName.clarity_blade, offset + memories + 1804),
    LocationName.gallery_clarity[5]: SlayThePrincessLocationData(RegionName.clarity_blade, offset + memories + 1805),
    LocationName.gallery_clarity[6]: SlayThePrincessLocationData(RegionName.clarity_blade, offset + memories + 1806),
    LocationName.gallery_clarity[7]: SlayThePrincessLocationData(RegionName.clarity_blade, offset + memories + 1807),
    LocationName.gallery_clarity[8]: SlayThePrincessLocationData(RegionName.clarity_blade, offset + memories + 1808),
    LocationName.gallery_clarity[9]: SlayThePrincessLocationData(RegionName.clarity_blade, offset + memories + 1809),
    LocationName.gallery_clarity[10]: SlayThePrincessLocationData(RegionName.clarity_blade, offset + memories + 1810),
    LocationName.gallery_clarity[11]: SlayThePrincessLocationData(RegionName.clarity_blade, offset + memories + 1811),
    LocationName.gallery_clarity[12]: SlayThePrincessLocationData(
        RegionName.clarity_blade, offset + memories + 1812,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_clarity[13]: SlayThePrincessLocationData(
        RegionName.clarity_blade, offset + memories + 1813,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_clarity[14]: SlayThePrincessLocationData(
        RegionName.clarity_blade, offset + memories + 1814,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_den[1]: SlayThePrincessLocationData(RegionName.den, offset + memories + 1901),
    LocationName.gallery_den[2]: SlayThePrincessLocationData(RegionName.den, offset + memories + 1902),
    LocationName.gallery_den[3]: SlayThePrincessLocationData(RegionName.den, offset + memories + 1903),
    LocationName.gallery_den[4]: SlayThePrincessLocationData(RegionName.den_stubborn_blade, offset + memories + 1904),
    LocationName.gallery_den[5]: SlayThePrincessLocationData(RegionName.den_stubborn_blade, offset + memories + 1905),
    LocationName.gallery_den[6]: SlayThePrincessLocationData(RegionName.den_stubborn_blade, offset + memories + 1906),
    LocationName.gallery_den[7]: SlayThePrincessLocationData(RegionName.den_stubborn_blade, offset + memories + 1907),
    LocationName.gallery_den[8]: SlayThePrincessLocationData(
        RegionName.den_skeptic, offset + memories + 1908,
        rule=lambda state, world: has_blade(state, world, ItemName.blade_den)),
    LocationName.gallery_den[9]: SlayThePrincessLocationData(RegionName.den, offset + memories + 1909),
    LocationName.gallery_den[10]: SlayThePrincessLocationData(RegionName.den_skeptic, offset + memories + 1910),
    LocationName.gallery_den[11]: SlayThePrincessLocationData(RegionName.den_skeptic, offset + memories + 1911),
    LocationName.gallery_den[12]: SlayThePrincessLocationData(RegionName.den_skeptic, offset + memories + 1912),
    LocationName.gallery_den[13]: SlayThePrincessLocationData(RegionName.den_skeptic, offset + memories + 1913),
    LocationName.gallery_den[14]: SlayThePrincessLocationData(RegionName.den_skeptic, offset + memories + 1914),
    LocationName.gallery_den[15]: SlayThePrincessLocationData(RegionName.den_skeptic, offset + memories + 1915),
    LocationName.gallery_den[16]: SlayThePrincessLocationData(RegionName.den_stubborn_blade, offset + memories + 1916),
    LocationName.gallery_den[17]: SlayThePrincessLocationData(RegionName.den_stubborn_blade, offset + memories + 1917),
    LocationName.gallery_den[18]: SlayThePrincessLocationData(
        RegionName.den, offset + memories + 1918,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_den[19]: SlayThePrincessLocationData(
        RegionName.den, offset + memories + 1919,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_den[20]: SlayThePrincessLocationData(
        RegionName.den, offset + memories + 1920,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_wild[1]: SlayThePrincessLocationData(RegionName.wild, offset + memories + 2001),
    LocationName.gallery_wild[2]: SlayThePrincessLocationData(RegionName.wild, offset + memories + 2002),
    LocationName.gallery_wild[3]: SlayThePrincessLocationData(RegionName.wild, offset + memories + 2003),
    LocationName.gallery_wild[4]: SlayThePrincessLocationData(RegionName.wild_blade, offset + memories + 2004),
    LocationName.gallery_wild[5]: SlayThePrincessLocationData(RegionName.wild_blade, offset + memories + 2005),
    LocationName.gallery_wild[6]: SlayThePrincessLocationData(RegionName.wild_blade, offset + memories + 2006),
    LocationName.gallery_wild[7]: SlayThePrincessLocationData(
        RegionName.wild, offset + memories + 2007,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_wild[8]: SlayThePrincessLocationData(
        RegionName.wild, offset + memories + 2008,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_wild[9]: SlayThePrincessLocationData(
        RegionName.wild, offset + memories + 2009,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_wild[10]: SlayThePrincessLocationData(
        RegionName.wild, offset + memories + 2010,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_wild[11]: SlayThePrincessLocationData(
        RegionName.wild, offset + memories + 2011,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),
    LocationName.gallery_wild[12]: SlayThePrincessLocationData(
        RegionName.wild, offset + memories + 2012,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_thorn[1]: SlayThePrincessLocationData(RegionName.thorn, offset + memories + 2101),
    LocationName.gallery_thorn[2]: SlayThePrincessLocationData(RegionName.thorn, offset + memories + 2102),
    LocationName.gallery_thorn[3]: SlayThePrincessLocationData(RegionName.thorn, offset + memories + 2103),
    LocationName.gallery_thorn[4]: SlayThePrincessLocationData(RegionName.thorn, offset + memories + 2104),
    LocationName.gallery_thorn[5]: SlayThePrincessLocationData(RegionName.thorn_blade, offset + memories + 2105),
    LocationName.gallery_thorn[6]: SlayThePrincessLocationData(RegionName.thorn, offset + memories + 2106),
    LocationName.gallery_thorn[7]: SlayThePrincessLocationData(RegionName.thorn, offset + memories + 2107),
    LocationName.gallery_thorn[8]: SlayThePrincessLocationData(RegionName.thorn_blade, offset + memories + 2108),
    LocationName.gallery_thorn[9]: SlayThePrincessLocationData(RegionName.thorn_blade, offset + memories + 2109),
    LocationName.gallery_thorn[10]: SlayThePrincessLocationData(RegionName.thorn_blade, offset + memories + 2110),
    LocationName.gallery_thorn[11]: SlayThePrincessLocationData(RegionName.thorn_blade, offset + memories + 2111),
    LocationName.gallery_thorn[12]: SlayThePrincessLocationData(RegionName.thorn_blade, offset + memories + 2112),
    LocationName.gallery_thorn[13]: SlayThePrincessLocationData(RegionName.thorn_blade, offset + memories + 2113),
    LocationName.gallery_thorn[14]: SlayThePrincessLocationData(RegionName.thorn_blade, offset + memories + 2114),
    LocationName.gallery_thorn[15]: SlayThePrincessLocationData(RegionName.thorn_smitten_blade, offset + memories + 2115),
    LocationName.gallery_thorn[16]: SlayThePrincessLocationData(RegionName.thorn_smitten_blade, offset + memories + 2116),
    LocationName.gallery_thorn[17]: SlayThePrincessLocationData(
        RegionName.thorn, offset + memories + 2117,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_thorn[18]: SlayThePrincessLocationData(
        RegionName.thorn, offset + memories + 2118,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_thorn[19]: SlayThePrincessLocationData(
        RegionName.thorn, offset + memories + 2119,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_cage[1]: SlayThePrincessLocationData(RegionName.cage, offset + memories + 2201),
    LocationName.gallery_cage[2]: SlayThePrincessLocationData(RegionName.cage, offset + memories + 2202),
    LocationName.gallery_cage[3]: SlayThePrincessLocationData(RegionName.cage, offset + memories + 2203),
    LocationName.gallery_cage[4]: SlayThePrincessLocationData(RegionName.cage, offset + memories + 2204),
    LocationName.gallery_cage[5]: SlayThePrincessLocationData(RegionName.cage, offset + memories + 2205),
    LocationName.gallery_cage[6]: SlayThePrincessLocationData(RegionName.cage, offset + memories + 2206),
    LocationName.gallery_cage[7]: SlayThePrincessLocationData(RegionName.cage, offset + memories + 2207),
    LocationName.gallery_cage[8]: SlayThePrincessLocationData(RegionName.cage, offset + memories + 2208),
    LocationName.gallery_cage[9]: SlayThePrincessLocationData(RegionName.cage, offset + memories + 2209),
    LocationName.gallery_cage[10]: SlayThePrincessLocationData(RegionName.cage, offset + memories + 2210),
    LocationName.gallery_cage[11]: SlayThePrincessLocationData(RegionName.cage_not_paranoid, offset + memories + 2211),
    LocationName.gallery_cage[12]: SlayThePrincessLocationData(RegionName.cage_not_paranoid, offset + memories + 2212),
    LocationName.gallery_cage[13]: SlayThePrincessLocationData(RegionName.cage_not_paranoid, offset + memories + 2213),
    LocationName.gallery_cage[14]: SlayThePrincessLocationData(RegionName.cage_not_paranoid, offset + memories + 2214),
    LocationName.gallery_cage[15]: SlayThePrincessLocationData(RegionName.cage_not_paranoid, offset + memories + 2215),
    LocationName.gallery_cage[16]: SlayThePrincessLocationData(RegionName.cage_paranoid_blade, offset + memories + 2216),
    LocationName.gallery_cage[17]: SlayThePrincessLocationData(RegionName.cage_paranoid_blade, offset + memories + 2217),
    LocationName.gallery_cage[18]: SlayThePrincessLocationData(
        RegionName.cage, offset + memories + 2218,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_cage[19]: SlayThePrincessLocationData(
        RegionName.cage, offset + memories + 2219,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_cage[20]: SlayThePrincessLocationData(
        RegionName.cage, offset + memories + 2220,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_grey[1]: SlayThePrincessLocationData(RegionName.grey_drowned, offset + memories + 2301),
    LocationName.gallery_grey[2]: SlayThePrincessLocationData(RegionName.grey_burned, offset + memories + 2302),
    LocationName.gallery_grey[3]: SlayThePrincessLocationData(RegionName.grey_drowned, offset + memories + 2303),
    LocationName.gallery_grey[4]: SlayThePrincessLocationData(RegionName.grey_burned, offset + memories + 2304),
    LocationName.gallery_grey[5]: SlayThePrincessLocationData(RegionName.grey_drowned, offset + memories + 2305),
    LocationName.gallery_grey[6]: SlayThePrincessLocationData(RegionName.grey_burned, offset + memories + 2306),
    LocationName.gallery_grey[7]: SlayThePrincessLocationData(RegionName.grey_burned, offset + memories + 2307),
    LocationName.gallery_grey[8]: SlayThePrincessLocationData(RegionName.grey_drowned, offset + memories + 2308),
    LocationName.gallery_grey[9]: SlayThePrincessLocationData(RegionName.grey_burned, offset + memories + 2309),
    LocationName.gallery_grey[10]: SlayThePrincessLocationData(RegionName.grey_drowned, offset + memories + 2310),
    LocationName.gallery_grey[11]: SlayThePrincessLocationData(RegionName.grey_burned, offset + memories + 2311),
    LocationName.gallery_grey[12]: SlayThePrincessLocationData(RegionName.grey_drowned, offset + memories + 2312),
    LocationName.gallery_grey[13]: SlayThePrincessLocationData(RegionName.grey_burned, offset + memories + 2313),
    LocationName.gallery_grey[14]: SlayThePrincessLocationData(RegionName.grey_burned, offset + memories + 2314),
    LocationName.gallery_grey[15]: SlayThePrincessLocationData(
        RegionName.grey_burned, offset + memories + 2315,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_grey[16]: SlayThePrincessLocationData(
        RegionName.grey_burned, offset + memories + 2316,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_grey[17]: SlayThePrincessLocationData(
        RegionName.grey_drowned, offset + memories + 2317,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_grey[18]: SlayThePrincessLocationData(
        RegionName.grey_drowned, offset + memories + 2318,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_grey[19]: SlayThePrincessLocationData(
        RegionName.grey_burned, offset + memories + 2319,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),
    LocationName.gallery_grey[20]: SlayThePrincessLocationData(
        RegionName.grey_drowned, offset + memories + 2320,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),

    LocationName.gallery_happily[1]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2401),
    LocationName.gallery_happily[2]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2402),
    LocationName.gallery_happily[3]: SlayThePrincessLocationData(RegionName.happily_skeptic, offset + memories + 2403),
    LocationName.gallery_happily[4]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2404),
    LocationName.gallery_happily[5]: SlayThePrincessLocationData(RegionName.happily_opportunist, offset + memories + 2405),
    LocationName.gallery_happily[6]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2406),
    LocationName.gallery_happily[7]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2407),
    LocationName.gallery_happily[8]: SlayThePrincessLocationData(RegionName.happily_blade, offset + memories + 2408),
    LocationName.gallery_happily[9]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2409),
    LocationName.gallery_happily[10]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2410),
    LocationName.gallery_happily[11]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2411),
    LocationName.gallery_happily[12]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2412),
    LocationName.gallery_happily[13]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2413),
    LocationName.gallery_happily[14]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2414),
    LocationName.gallery_happily[15]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2415),
    LocationName.gallery_happily[16]: SlayThePrincessLocationData(RegionName.happily, offset + memories + 2416),
    LocationName.gallery_happily[17]: SlayThePrincessLocationData(
        RegionName.happily, offset + memories + 2417,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_happily[18]: SlayThePrincessLocationData(
        RegionName.happily, offset + memories + 2418,
        rule=lambda state, world: state.can_reach_region(RegionName.restart, world.player)),
    LocationName.gallery_happily[19]: SlayThePrincessLocationData(
        RegionName.happily, offset + memories + 2419,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),
    LocationName.gallery_happily[20]: SlayThePrincessLocationData(
        RegionName.happily, offset + memories + 2420,
        rule=lambda state, world: state.can_reach_region(RegionName.goddess, world.player)),
}

location_data_table: Dict[str, SlayThePrincessLocationData] = {**others_location_data_table,
                                                               **mirror_location_data_table,
                                                               **princess_location_data_table,
                                                               **global_chapter_location_data_table,
                                                               **heart_location_data_table,
                                                               **gallery_location_data_table}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
