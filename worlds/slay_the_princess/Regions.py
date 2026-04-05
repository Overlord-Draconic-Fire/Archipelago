from dataclasses import dataclass
from enum import Enum

from BaseClasses import Region
from .Names import RegionName, ItemName
from .Rules import has_voice, has_all_voices, has_voices, has_dagger_for, max_reachable_vessels

entry = " ENTRY"


class SlayThePrincessRegion(Region):
    game = "Slay The Princess"


class Chapter(str, Enum):
    one = 1
    two = 2
    three = 3
    meta = 4


@dataclass
class SlayThePrincessRegionData:
    master_region: str = ""
    chapter: Chapter = Chapter.meta
    have_entry: bool = True


region_data_table: dict[str, SlayThePrincessRegionData] = {
    RegionName.menu: SlayThePrincessRegionData(RegionName.menu, Chapter.meta, False),
    RegionName.one: SlayThePrincessRegionData(RegionName.one, Chapter.one, False),
    RegionName.chap2: SlayThePrincessRegionData(RegionName.chap2, Chapter.two, False),
    RegionName.chap3: SlayThePrincessRegionData(RegionName.chap3, Chapter.three, False),

    # Chapters 2
    RegionName.adversary: SlayThePrincessRegionData(RegionName.adversary, Chapter.two),
    RegionName.adversary_dagger: SlayThePrincessRegionData(RegionName.adversary, Chapter.two),
    RegionName.tower: SlayThePrincessRegionData(RegionName.tower, Chapter.two),
    RegionName.spectre: SlayThePrincessRegionData(RegionName.spectre, Chapter.two),
    RegionName.nightmare: SlayThePrincessRegionData(RegionName.nightmare, Chapter.two),
    RegionName.razor: SlayThePrincessRegionData(RegionName.razor, Chapter.two),
    RegionName.beast: SlayThePrincessRegionData(RegionName.beast, Chapter.two),
    RegionName.witch: SlayThePrincessRegionData(RegionName.witch, Chapter.two),
    RegionName.stranger: SlayThePrincessRegionData(RegionName.stranger, Chapter.two),
    RegionName.stranger_dagger: SlayThePrincessRegionData(RegionName.stranger, Chapter.two),
    RegionName.prisoner: SlayThePrincessRegionData(RegionName.prisoner, Chapter.two),
    RegionName.damsel: SlayThePrincessRegionData(RegionName.damsel, Chapter.two),

    # Eye of the Needle
    RegionName.needle: SlayThePrincessRegionData(RegionName.needle, Chapter.three),
    RegionName.needle_hunted: SlayThePrincessRegionData(RegionName.needle, Chapter.three),
    RegionName.needle_skeptic: SlayThePrincessRegionData(RegionName.needle, Chapter.three),

    # Fury
    RegionName.fury: SlayThePrincessRegionData(RegionName.fury, Chapter.three),
    RegionName.fury_weathered_heart: SlayThePrincessRegionData(RegionName.fury, Chapter.three, False),
    RegionName.fury_pacifism: SlayThePrincessRegionData(RegionName.fury, Chapter.three),
    RegionName.fury_unarmed_broken: SlayThePrincessRegionData(RegionName.fury, Chapter.three),
    RegionName.fury_unarmed_contrarian: SlayThePrincessRegionData(RegionName.fury, Chapter.three),
    RegionName.fury_other: SlayThePrincessRegionData(RegionName.fury, Chapter.three),
    RegionName.fury_tower: SlayThePrincessRegionData(RegionName.fury, Chapter.three),

    # Apotheosis
    RegionName.apotheosis: SlayThePrincessRegionData(RegionName.apotheosis, Chapter.three),
    RegionName.apotheosis_contrarian: SlayThePrincessRegionData(RegionName.apotheosis, Chapter.three),
    RegionName.apotheosis_paranoid: SlayThePrincessRegionData(RegionName.apotheosis, Chapter.three),

    # Dragon
    RegionName.dragon: SlayThePrincessRegionData(RegionName.dragon, Chapter.three),
    RegionName.dragon_kind: SlayThePrincessRegionData(RegionName.dragon, Chapter.three),
    RegionName.dragon_harsh: SlayThePrincessRegionData(RegionName.dragon, Chapter.three),

    # Wraith
    RegionName.wraith: SlayThePrincessRegionData(RegionName.wraith, Chapter.three),
    RegionName.wraith_cheated: SlayThePrincessRegionData(RegionName.wraith, Chapter.three),
    RegionName.wraith_paranoid: SlayThePrincessRegionData(RegionName.wraith, Chapter.three),
    RegionName.wraith_cold: SlayThePrincessRegionData(RegionName.wraith, Chapter.three),
    RegionName.wraith_opportunist: SlayThePrincessRegionData(RegionName.wraith, Chapter.three),

    # Moment of Clarity
    RegionName.clarity: SlayThePrincessRegionData(RegionName.clarity, Chapter.three),

    # Razor
    RegionName.razor_chap3: SlayThePrincessRegionData(RegionName.razor_chap3, Chapter.three),
    RegionName.razor_no_way: SlayThePrincessRegionData(RegionName.razor_no_way, Chapter.three),
    RegionName.razor_no_way_broken: SlayThePrincessRegionData(RegionName.razor_no_way, Chapter.three),
    RegionName.razor_no_way_paranoid: SlayThePrincessRegionData(RegionName.razor_no_way, Chapter.three),
    RegionName.razor_no_way_stubborn: SlayThePrincessRegionData(RegionName.razor_no_way, Chapter.three),

    RegionName.razor_race: SlayThePrincessRegionData(RegionName.razor_race, Chapter.three),
    RegionName.razor_race_broken: SlayThePrincessRegionData(RegionName.razor_race, Chapter.three),
    RegionName.razor_race_paranoid: SlayThePrincessRegionData(RegionName.razor_race, Chapter.three),
    RegionName.razor_race_stubborn: SlayThePrincessRegionData(RegionName.razor_race, Chapter.three),

    # Razor Chapter4
    RegionName.razor_chap4: SlayThePrincessRegionData(RegionName.razor_chap4, Chapter.three),
    RegionName.razor_empty: SlayThePrincessRegionData(RegionName.razor_chap4, Chapter.three),
    RegionName.razor_destruction: SlayThePrincessRegionData(RegionName.razor_chap4, Chapter.three),

    # Den
    RegionName.den: SlayThePrincessRegionData(RegionName.den, Chapter.three),
    RegionName.den_skeptic: SlayThePrincessRegionData(RegionName.den, Chapter.three),
    RegionName.den_stubborn: SlayThePrincessRegionData(RegionName.den, Chapter.three),

    # Wild
    RegionName.wild: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_dagger: SlayThePrincessRegionData(RegionName.wild, Chapter.three, False),
    RegionName.wild_beast_broken: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_beast_contrarian: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_beast_opportunist: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_beast_stubborn: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_witch_stubborn: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_witch_cheated: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_witch_paranoid: SlayThePrincessRegionData(RegionName.wild, Chapter.three),

    # Thorn
    RegionName.thorn: SlayThePrincessRegionData(RegionName.thorn, Chapter.three),
    RegionName.thorn_smitten: SlayThePrincessRegionData(RegionName.thorn, Chapter.three),
    RegionName.thorn_cheated: SlayThePrincessRegionData(RegionName.thorn, Chapter.three),

    # Cage
    RegionName.cage: SlayThePrincessRegionData(RegionName.cage, Chapter.three),
    RegionName.cage_paranoid: SlayThePrincessRegionData(RegionName.cage, Chapter.three),
    RegionName.cage_cheated: SlayThePrincessRegionData(RegionName.cage, Chapter.three),
    RegionName.cage_broken: SlayThePrincessRegionData(RegionName.cage, Chapter.three),

    # Grey
    RegionName.grey: SlayThePrincessRegionData(RegionName.grey, Chapter.three),
    RegionName.grey_drowned: SlayThePrincessRegionData(RegionName.grey, Chapter.three),
    RegionName.grey_burned: SlayThePrincessRegionData(RegionName.grey, Chapter.three),

    # Happily Ever After
    RegionName.happily: SlayThePrincessRegionData(RegionName.happily, Chapter.three),
    RegionName.happily_skeptic: SlayThePrincessRegionData(RegionName.happily, Chapter.three),
    RegionName.happily_opportunist: SlayThePrincessRegionData(RegionName.happily, Chapter.three),

    # META
    RegionName.space_between: SlayThePrincessRegionData(RegionName.space_between, Chapter.meta, False),
    RegionName.goddess: SlayThePrincessRegionData(RegionName.goddess, Chapter.meta),
    RegionName.win: SlayThePrincessRegionData(RegionName.win, Chapter.meta, False),

}


def set_region_rules(world, regions: dict[str, Region]):
    # region Chapter Location
    # Chapter 2 sub Entry -> Chap2
    regions[RegionName.adversary + entry].connect(regions[RegionName.chap2])
    regions[RegionName.tower + entry].connect(regions[RegionName.chap2])
    regions[RegionName.spectre + entry].connect(regions[RegionName.chap2])
    regions[RegionName.nightmare + entry].connect(regions[RegionName.chap2])
    regions[RegionName.razor + entry].connect(regions[RegionName.chap2])
    regions[RegionName.beast + entry].connect(regions[RegionName.chap2])
    regions[RegionName.witch + entry].connect(regions[RegionName.chap2])
    regions[RegionName.stranger + entry].connect(regions[RegionName.chap2])
    regions[RegionName.prisoner + entry].connect(regions[RegionName.chap2])
    regions[RegionName.damsel + entry].connect(regions[RegionName.chap2])

    # Chapter 3 main Entry -> Chap3
    regions[RegionName.needle + entry].connect(regions[RegionName.chap3])
    regions[RegionName.fury + entry].connect(regions[RegionName.chap3])
    regions[RegionName.apotheosis + entry].connect(regions[RegionName.chap3])
    regions[RegionName.dragon + entry].connect(regions[RegionName.chap3])
    regions[RegionName.wraith + entry].connect(regions[RegionName.chap3])
    regions[RegionName.clarity + entry].connect(regions[RegionName.chap3])
    regions[RegionName.razor_chap3].connect(regions[RegionName.chap3])
    regions[RegionName.den + entry].connect(regions[RegionName.chap3])
    regions[RegionName.wild + entry].connect(regions[RegionName.chap3])
    regions[RegionName.thorn + entry].connect(regions[RegionName.chap3])
    regions[RegionName.cage + entry].connect(regions[RegionName.chap3])
    regions[RegionName.grey + entry].connect(regions[RegionName.chap3])
    regions[RegionName.happily + entry].connect(regions[RegionName.chap3])
    # endregion

    # region Chapter 1
    regions[RegionName.menu].connect(regions[RegionName.one])  # Menu -> Chapter I

    regions[RegionName.one].connect(
        connecting_region=regions[RegionName.adversary + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_princess)
    )  # Chapter I -> Adversary

    regions[RegionName.one].connect(
        connecting_region=regions[RegionName.tower + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_princess)
    )  # Chapter I -> Tower

    regions[RegionName.one].connect(
        connecting_region=regions[RegionName.spectre + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_princess)
    )  # Chapter I -> Spectre

    regions[RegionName.one].connect(regions[RegionName.nightmare + entry])  # Chapter I -> Nightmare

    regions[RegionName.one].connect(
        connecting_region=regions[RegionName.razor + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_princess)
    )  # Chapter I -> Razor

    regions[RegionName.one].connect(
        connecting_region=regions[RegionName.beast + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_princess)
    )  # Chapter I -> Beast

    regions[RegionName.one].connect(
        connecting_region=regions[RegionName.witch + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_princess)
    )  # Chapter I -> Witch

    regions[RegionName.one].connect(regions[RegionName.stranger + entry])  # Chapter I -> Stranger

    regions[RegionName.one].connect(
        connecting_region=regions[RegionName.prisoner + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_princess)
    )  # Chapter I -> Prisoner

    regions[RegionName.one].connect(regions[RegionName.damsel + entry])  # Chapter I -> Damsel
    # endregion

    # region Chapter 2 Entry -> Main
    regions[RegionName.adversary + entry].connect(
        connecting_region=regions[RegionName.adversary],
        rule=lambda state: state.has(ItemName.adversary, world.player) and has_voice(state, world, ItemName.stubborn)
    )  # Chapter II Adversary entry -> Adversary

    regions[RegionName.tower + entry].connect(
        connecting_region=regions[RegionName.tower],
        rule=lambda state: state.has(ItemName.tower, world.player) and has_voice(state, world, ItemName.broken)
    )  # Chapter II Tower entry -> Tower

    regions[RegionName.spectre + entry].connect(
        connecting_region=regions[RegionName.spectre],
        rule=lambda state: state.has(ItemName.spectre, world.player) and has_voice(state, world, ItemName.cold)
    )  # Chapter II Spectre entry -> Spectre

    regions[RegionName.nightmare + entry].connect(
        connecting_region=regions[RegionName.nightmare],
        rule=lambda state: state.has(ItemName.nightmare, world.player) and has_voice(state, world, ItemName.paranoid)
    )  # Chapter II Nightmare entry -> Nightmare

    regions[RegionName.razor + entry].connect(
        connecting_region=regions[RegionName.razor],
        rule=lambda state: state.has(ItemName.razor, world.player) and has_voice(state, world, ItemName.cheated)
    )  # Chapter II Razor entry -> Razor

    regions[RegionName.beast + entry].connect(
        connecting_region=regions[RegionName.beast],
        rule=lambda state: state.has(ItemName.beast, world.player) and has_voice(state, world, ItemName.hunted)
    )  # Chapter II Beast entry -> Beast

    regions[RegionName.witch + entry].connect(
        connecting_region=regions[RegionName.witch],
        rule=lambda state: state.has(ItemName.witch, world.player) and has_voice(state, world, ItemName.opportunist)
    )  # Chapter II Witch entry -> Witch

    regions[RegionName.stranger + entry].connect(
        connecting_region=regions[RegionName.stranger],
        rule=lambda state: state.has(ItemName.stranger, world.player) and has_voice(state, world, ItemName.contrarian)
    )  # Chapter II Stranger entry -> Stranger

    regions[RegionName.prisoner + entry].connect(
        connecting_region=regions[RegionName.prisoner],
        rule=lambda state: state.has(ItemName.prisoner, world.player) and has_voice(state, world, ItemName.skeptic)
    )  # Chapter II Prisoner entry -> Prisoner

    regions[RegionName.damsel + entry].connect(
        connecting_region=regions[RegionName.damsel],
        rule=lambda state: state.has(ItemName.damsel, world.player) and has_voice(state, world, ItemName.smitten)
    )  # Chapter II Damsel entry -> Damsel
    # endregion

    # region Chapter 2 Dagger Only
    regions[RegionName.adversary].connect(
        connecting_region=regions[RegionName.adversary_dagger],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_adversary)
    )  # Chapter II Adversary Dagger Only

    regions[RegionName.stranger].connect(
        connecting_region=regions[RegionName.stranger_dagger],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_stranger)
    )  # Chapter II Stranger Dagger Only
    # endregion

    # region Chapter 2 -> Chapter 3 Sub Entry
    # Adversary → Needle / Fury (entry)
    regions[RegionName.adversary].connect(
        connecting_region=regions[RegionName.needle_hunted + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_adversary)
    )
    regions[RegionName.adversary].connect(
        connecting_region=regions[RegionName.needle_skeptic + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_adversary)
    )

    regions[RegionName.adversary].connect(
        connecting_region=regions[RegionName.fury_other + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_adversary)
    )
    regions[RegionName.adversary].connect(regions[RegionName.fury_pacifism + entry])
    regions[RegionName.adversary].connect(regions[RegionName.fury_unarmed_broken + entry])
    regions[RegionName.adversary].connect(regions[RegionName.fury_unarmed_contrarian + entry])

    # Tower → Apotheosis / Fury Tower (entry)
    regions[RegionName.tower].connect(
        connecting_region=regions[RegionName.fury_tower + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_tower)
    )

    regions[RegionName.tower].connect(
        connecting_region=regions[RegionName.apotheosis_contrarian + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_tower)
    )
    regions[RegionName.tower].connect(regions[RegionName.apotheosis_paranoid + entry])

    # Spectre → Dragon / Wraith (entry)
    regions[RegionName.spectre].connect(
        connecting_region=regions[RegionName.dragon_kind + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_spectre)
    )
    regions[RegionName.spectre].connect(
        connecting_region=regions[RegionName.dragon_harsh + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_spectre)
    )

    regions[RegionName.spectre].connect(regions[RegionName.wraith_cheated + entry])
    regions[RegionName.spectre].connect(regions[RegionName.wraith_paranoid + entry])

    # Nightmare → Clarity / Wraith (entry)
    regions[RegionName.nightmare].connect(regions[RegionName.clarity + entry])

    regions[RegionName.nightmare].connect(
        connecting_region=regions[RegionName.wraith_cold + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_nightmare)
    )
    regions[RegionName.nightmare].connect(
        connecting_region=regions[RegionName.wraith_opportunist + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_nightmare)
    )

    # Razor → No Way / Race (entry)
    regions[RegionName.razor].connect(regions[RegionName.razor_no_way_broken + entry])
    regions[RegionName.razor].connect(regions[RegionName.razor_no_way_paranoid + entry])
    regions[RegionName.razor].connect(regions[RegionName.razor_no_way_stubborn + entry])

    regions[RegionName.razor].connect(
        connecting_region=regions[RegionName.razor_race_broken + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_razor)
    )
    regions[RegionName.razor].connect(
        connecting_region=regions[RegionName.razor_race_paranoid + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_razor)
    )
    regions[RegionName.razor].connect(
        connecting_region=regions[RegionName.razor_race_stubborn + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_razor)
    )

    # Beast → Den / Wild (entry)
    regions[RegionName.beast].connect(regions[RegionName.den_skeptic + entry])
    regions[RegionName.beast].connect(
        connecting_region=regions[RegionName.den_stubborn + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_beast)
    )

    regions[RegionName.beast].connect(regions[RegionName.wild_beast_broken + entry])
    regions[RegionName.beast].connect(regions[RegionName.wild_beast_contrarian + entry])
    regions[RegionName.beast].connect(
        connecting_region=regions[RegionName.wild_beast_opportunist + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_beast)
    )
    regions[RegionName.beast].connect(
        connecting_region=regions[RegionName.wild_beast_stubborn + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_beast)
    )

    # Witch → Thorn / Wild (entry)
    regions[RegionName.witch].connect(
        connecting_region=regions[RegionName.thorn_smitten + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_witch)
    )
    regions[RegionName.witch].connect(
        connecting_region=regions[RegionName.thorn_cheated + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_witch)
    )

    regions[RegionName.witch].connect(
        connecting_region=regions[RegionName.wild_witch_stubborn + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_witch))
    regions[RegionName.witch].connect(
        connecting_region=regions[RegionName.wild_witch_cheated + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_witch))
    regions[RegionName.witch].connect(regions[RegionName.wild_witch_paranoid + entry])

    # Prisoner → Cage / Grey (entry)
    regions[RegionName.prisoner].connect(
        connecting_region=regions[RegionName.cage_paranoid + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_prisoner)
    )
    regions[RegionName.prisoner].connect(regions[RegionName.cage_cheated + entry])
    regions[RegionName.prisoner].connect(regions[RegionName.cage_broken + entry])

    regions[RegionName.prisoner].connect(
        connecting_region=regions[RegionName.grey_drowned + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_prisoner)
    )

    # Damsel → Happily / Grey Burned (entry)
    regions[RegionName.damsel].connect(regions[RegionName.happily_skeptic + entry])
    regions[RegionName.damsel].connect(regions[RegionName.happily_opportunist + entry])

    regions[RegionName.damsel].connect(
        connecting_region=regions[RegionName.grey_burned + entry],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_damsel)
    )
    # endregion

    # region Chapter 3 Sub Entry -> Main Entry
    # Needle (entry)
    regions[RegionName.needle_hunted + entry].connect(regions[RegionName.needle + entry])
    regions[RegionName.needle_skeptic + entry].connect(regions[RegionName.needle + entry])

    # Fury (entry)
    regions[RegionName.fury_pacifism + entry].connect(regions[RegionName.fury + entry])
    regions[RegionName.fury_unarmed_broken + entry].connect(regions[RegionName.fury + entry])
    regions[RegionName.fury_unarmed_contrarian + entry].connect(regions[RegionName.fury + entry])
    regions[RegionName.fury_other + entry].connect(regions[RegionName.fury + entry])
    regions[RegionName.fury_tower + entry].connect(regions[RegionName.fury + entry])

    # Apotheosis (entry)
    regions[RegionName.apotheosis_contrarian + entry].connect(regions[RegionName.apotheosis + entry])
    regions[RegionName.apotheosis_paranoid + entry].connect(regions[RegionName.apotheosis + entry])

    # Dragon (entry)
    regions[RegionName.dragon_kind + entry].connect(regions[RegionName.dragon + entry])
    regions[RegionName.dragon_harsh + entry].connect(regions[RegionName.dragon + entry])

    # Wraith (entry)
    regions[RegionName.wraith_cheated + entry].connect(regions[RegionName.wraith + entry])
    regions[RegionName.wraith_paranoid + entry].connect(regions[RegionName.wraith + entry])
    regions[RegionName.wraith_cold + entry].connect(regions[RegionName.wraith + entry])
    regions[RegionName.wraith_opportunist + entry].connect(regions[RegionName.wraith + entry])

    # Razor No Way (entry)
    regions[RegionName.razor_no_way_broken + entry].connect(regions[RegionName.razor_no_way + entry])
    regions[RegionName.razor_no_way_paranoid + entry].connect(regions[RegionName.razor_no_way + entry])
    regions[RegionName.razor_no_way_stubborn + entry].connect(regions[RegionName.razor_no_way + entry])

    # Razor Race (entry)
    regions[RegionName.razor_race_broken + entry].connect(regions[RegionName.razor_race + entry])
    regions[RegionName.razor_race_paranoid + entry].connect(regions[RegionName.razor_race + entry])
    regions[RegionName.razor_race_stubborn + entry].connect(regions[RegionName.razor_race + entry])

    # Den (entry)
    regions[RegionName.den_skeptic + entry].connect(regions[RegionName.den + entry])
    regions[RegionName.den_stubborn + entry].connect(regions[RegionName.den + entry])

    # Wild (entry)
    regions[RegionName.wild_beast_broken + entry].connect(regions[RegionName.wild + entry])
    regions[RegionName.wild_beast_contrarian + entry].connect(regions[RegionName.wild + entry])
    regions[RegionName.wild_beast_opportunist + entry].connect(regions[RegionName.wild + entry])
    regions[RegionName.wild_beast_stubborn + entry].connect(regions[RegionName.wild + entry])
    regions[RegionName.wild_witch_stubborn + entry].connect(regions[RegionName.wild + entry])
    regions[RegionName.wild_witch_cheated + entry].connect(regions[RegionName.wild + entry])
    regions[RegionName.wild_witch_paranoid + entry].connect(regions[RegionName.wild + entry])

    # Thorn (entry)
    regions[RegionName.thorn_smitten + entry].connect(regions[RegionName.thorn + entry])
    regions[RegionName.thorn_cheated + entry].connect(regions[RegionName.thorn + entry])

    # Cage (entry)
    regions[RegionName.cage_paranoid + entry].connect(regions[RegionName.cage + entry])
    regions[RegionName.cage_cheated + entry].connect(regions[RegionName.cage + entry])
    regions[RegionName.cage_broken + entry].connect(regions[RegionName.cage + entry])

    # Grey (entry)
    regions[RegionName.grey_drowned + entry].connect(regions[RegionName.grey + entry])
    regions[RegionName.grey_burned + entry].connect(regions[RegionName.grey + entry])

    # Happily (entry)
    regions[RegionName.happily_skeptic + entry].connect(regions[RegionName.happily + entry])
    regions[RegionName.happily_opportunist + entry].connect(regions[RegionName.happily + entry])

    # endregion

    # region Chapter 3 Sub Entry -> Sub
    # Needle (entry)
    regions[RegionName.needle_hunted + entry].connect(
        connecting_region=regions[RegionName.needle_hunted],
        rule=lambda state: state.has(ItemName.needle, world.player) and has_voices(state, world, [ItemName.stubborn, ItemName.hunted])
    )  # Needle Hunted

    regions[RegionName.needle_skeptic + entry].connect(
        connecting_region=regions[RegionName.needle_skeptic],
        rule=lambda state: state.has(ItemName.needle, world.player) and has_voices(state, world, [ItemName.stubborn, ItemName.skeptic])
    )  # Needle Skeptic

    # Fury (entry)
    regions[RegionName.fury_pacifism + entry].connect(
        connecting_region=regions[RegionName.fury_pacifism],
        rule=lambda state: state.has(ItemName.fury, world.player) and has_voices(state, world, [ItemName.stubborn, ItemName.cold])
    )  # Fury Pacifism

    regions[RegionName.fury_unarmed_broken + entry].connect(
        connecting_region=regions[RegionName.fury_unarmed_broken],
        rule=lambda state: state.has(ItemName.fury, world.player) and has_voices(state, world, [ItemName.stubborn, ItemName.broken])
    )  # Fury Unarmed Broken

    regions[RegionName.fury_unarmed_contrarian + entry].connect(
        connecting_region=regions[RegionName.fury_unarmed_contrarian],
        rule=lambda state: state.has(ItemName.fury, world.player) and has_voices(state, world, [ItemName.stubborn, ItemName.contrarian])
    )  # Fury Unarmed Contrarian

    regions[RegionName.fury_other + entry].connect(
        connecting_region=regions[RegionName.fury_other],
        rule=lambda state: state.has(ItemName.fury, world.player) and has_voices(state, world, [ItemName.stubborn, ItemName.broken])
    )  # Fury Other

    regions[RegionName.fury_tower + entry].connect(
        connecting_region=regions[RegionName.fury_tower],
        rule=lambda state: state.has(ItemName.fury, world.player) and has_voices(state, world, [ItemName.broken, ItemName.stubborn])
    )  # Fury Tower

    # Apotheosis (entry)
    regions[RegionName.apotheosis_contrarian + entry].connect(
        connecting_region=regions[RegionName.apotheosis_contrarian],
        rule=lambda state: state.has(ItemName.apotheosis, world.player) and has_voices(state, world, [ItemName.broken, ItemName.contrarian])
    )  # Apotheosis Contrarian

    regions[RegionName.apotheosis_paranoid + entry].connect(
        connecting_region=regions[RegionName.apotheosis_paranoid],
        rule=lambda state: state.has(ItemName.apotheosis, world.player) and has_voices(state, world, [ItemName.broken, ItemName.paranoid])
    )  # Apotheosis Paranoid

    # Dragon (entry)
    regions[RegionName.dragon_kind + entry].connect(
        connecting_region=regions[RegionName.dragon_kind],
        rule=lambda state: state.has(ItemName.dragon, world.player) and has_voices(state, world, [ItemName.cold, ItemName.opportunist])
    )  # Dragon Kind

    regions[RegionName.dragon_harsh + entry].connect(
        connecting_region=regions[RegionName.dragon_harsh],
        rule=lambda state: state.has(ItemName.dragon, world.player) and has_voices(state, world, [ItemName.cold, ItemName.opportunist])
    )  # Dragon Harsh

    # Wraith (entry)
    regions[RegionName.wraith_cheated + entry].connect(
        connecting_region=regions[RegionName.wraith_cheated],
        rule=lambda state: state.has(ItemName.wraith, world.player) and has_voices(state, world, [ItemName.cold, ItemName.cheated])
    )  # Wraith Cheated

    regions[RegionName.wraith_paranoid + entry].connect(
        connecting_region=regions[RegionName.wraith_paranoid],
        rule=lambda state: state.has(ItemName.wraith, world.player) and has_voices(state, world, [ItemName.cold, ItemName.paranoid])
    )  # Wraith Paranoid

    regions[RegionName.wraith_cold + entry].connect(
        connecting_region=regions[RegionName.wraith_cold],
        rule=lambda state: state.has(ItemName.wraith, world.player) and has_voices(state, world, [ItemName.paranoid, ItemName.cold])
    )  # Wraith Cold

    regions[RegionName.wraith_opportunist + entry].connect(
        connecting_region=regions[RegionName.wraith_opportunist],
        rule=lambda state: state.has(ItemName.wraith, world.player) and has_voices(state, world, [ItemName.paranoid, ItemName.opportunist])
    )  # Wraith Opportunist

    # Clarity (entry)
    regions[RegionName.clarity + entry].connect(
        connecting_region=regions[RegionName.clarity],
        rule=lambda state: state.has(ItemName.clarity, world.player) and has_all_voices(state, world)
    )  # Clarity

    # Razor No Way (entry)
    regions[RegionName.razor_no_way_broken + entry].connect(
        connecting_region=regions[RegionName.razor_no_way_broken],
        rule=lambda state: state.has(ItemName.razor, world.player) and has_voices(state, world, [ItemName.cheated, ItemName.contrarian, ItemName.broken])
    )  # Razor No Way Broken

    regions[RegionName.razor_no_way_paranoid + entry].connect(
        connecting_region=regions[RegionName.razor_no_way_paranoid],
        rule=lambda state: state.has(ItemName.razor, world.player) and has_voices(state, world, [ItemName.cheated, ItemName.contrarian, ItemName.paranoid])
    )  # Razor No Way Paranoid

    regions[RegionName.razor_no_way_stubborn + entry].connect(
        connecting_region=regions[RegionName.razor_no_way_stubborn],
        rule=lambda state: state.has(ItemName.razor, world.player) and has_voices(state, world, [ItemName.cheated, ItemName.contrarian, ItemName.stubborn])
    )  # Razor No Way Stubborn

    # Razor Race (entry)
    regions[RegionName.razor_race_broken + entry].connect(
        connecting_region=regions[RegionName.razor_race_broken],
        rule=lambda state: state.has(ItemName.razor, world.player) and has_voices(state, world, [ItemName.cheated, ItemName.hunted, ItemName.broken])
    )  # Razor Race Broken

    regions[RegionName.razor_race_paranoid + entry].connect(
        connecting_region=regions[RegionName.razor_race_paranoid],
        rule=lambda state: state.has(ItemName.razor, world.player) and has_voices(state, world, [ItemName.cheated, ItemName.hunted, ItemName.paranoid])
    )  # Razor Race Paranoid

    regions[RegionName.razor_race_stubborn + entry].connect(
        connecting_region=regions[RegionName.razor_race_stubborn],
        rule=lambda state: state.has(ItemName.razor, world.player) and has_voices(state, world, [ItemName.cheated, ItemName.hunted, ItemName.stubborn])
    )  # Razor Race Stubborn

    # Den (entry)
    regions[RegionName.den_skeptic + entry].connect(
        connecting_region=regions[RegionName.den_skeptic],
        rule=lambda state: state.has(ItemName.den, world.player) and has_voices(state, world, [ItemName.hunted, ItemName.skeptic])
    )  # Den Skeptic

    regions[RegionName.den_stubborn + entry].connect(
        connecting_region=regions[RegionName.den_stubborn],
        rule=lambda state: state.has(ItemName.den, world.player) and has_voices(state, world, [ItemName.hunted, ItemName.stubborn])
    )  # Den Stubborn

    # Wild (entry)
    regions[RegionName.wild_beast_broken + entry].connect(
        connecting_region=regions[RegionName.wild_beast_broken],
        rule=lambda state: state.has(ItemName.wild, world.player) and has_voices(state, world, [ItemName.hunted, ItemName.broken])
    )  # Wild Beast Broken

    regions[RegionName.wild_beast_contrarian + entry].connect(
        connecting_region=regions[RegionName.wild_beast_contrarian],
        rule=lambda state: state.has(ItemName.wild, world.player) and has_voices(state, world, [ItemName.hunted, ItemName.contrarian])
    )  # Wild Beast Contrarian

    regions[RegionName.wild_beast_opportunist + entry].connect(
        connecting_region=regions[RegionName.wild_beast_opportunist],
        rule=lambda state: state.has(ItemName.wild, world.player) and has_voices(state, world, [ItemName.hunted, ItemName.opportunist])
    )  # Wild Beast Opportunist

    regions[RegionName.wild_beast_stubborn + entry].connect(
        connecting_region=regions[RegionName.wild_beast_stubborn],
        rule=lambda state: state.has(ItemName.wild, world.player) and has_voices(state, world, [ItemName.hunted, ItemName.stubborn])
    )  # Wild Beast Stubborn

    regions[RegionName.wild_witch_stubborn + entry].connect(
        connecting_region=regions[RegionName.wild_witch_stubborn],
        rule=lambda state: state.has(ItemName.witch, world.player) and has_voices(state, world, [ItemName.opportunist, ItemName.stubborn])
    )  # Wild Witch Stubborn

    regions[RegionName.wild_witch_cheated + entry].connect(
        connecting_region=regions[RegionName.wild_witch_cheated],
        rule=lambda state: state.has(ItemName.witch, world.player) and has_voices(state, world, [ItemName.opportunist, ItemName.cheated])
    )  # Wild Witch Cheated

    regions[RegionName.wild_witch_paranoid + entry].connect(
        connecting_region=regions[RegionName.wild_witch_paranoid],
        rule=lambda state: state.has(ItemName.witch, world.player) and has_voices(state, world, [ItemName.opportunist, ItemName.paranoid])
    )  # Wild Witch Paranoid

    # Thorn (entry)
    regions[RegionName.thorn_smitten + entry].connect(
        connecting_region=regions[RegionName.thorn_smitten],
        rule=lambda state: state.has(ItemName.thorn, world.player) and has_voices(state, world, [ItemName.opportunist, ItemName.smitten])
    )  # Thorn Smitten

    regions[RegionName.thorn_cheated + entry].connect(
        connecting_region=regions[RegionName.thorn_cheated],
        rule=lambda state: state.has(ItemName.thorn, world.player) and has_voices(state, world, [ItemName.opportunist, ItemName.cheated])
    )  # Thorn Cheated

    # Cage (entry)
    regions[RegionName.cage_paranoid + entry].connect(
        connecting_region=regions[RegionName.cage_paranoid],
        rule=lambda state: state.has(ItemName.cage, world.player) and has_voices(state, world, [ItemName.skeptic, ItemName.paranoid])
    )  # Cage Paranoid

    regions[RegionName.cage_cheated + entry].connect(
        connecting_region=regions[RegionName.cage_cheated],
        rule=lambda state: state.has(ItemName.cage, world.player) and has_voices(state, world, [ItemName.skeptic, ItemName.cheated])
    )  # Cage Cheated

    regions[RegionName.cage_broken + entry].connect(
        connecting_region=regions[RegionName.cage_broken],
        rule=lambda state: state.has(ItemName.cage, world.player) and has_voices(state, world, [ItemName.skeptic, ItemName.broken])
    )  # Cage Broken

    # Grey (entry)
    regions[RegionName.grey_drowned + entry].connect(
        connecting_region=regions[RegionName.grey_drowned],
        rule=lambda state: state.has(ItemName.grey, world.player) and has_voices(state, world, [ItemName.skeptic, ItemName.cold])
    )  # Grey Drowned

    regions[RegionName.grey_burned + entry].connect(
        connecting_region=regions[RegionName.grey_burned],
        rule=lambda state: state.has(ItemName.grey, world.player) and has_voices(state, world, [ItemName.smitten, ItemName.cold])
    )  # Grey Burned

    # Happily (entry)
    regions[RegionName.happily_skeptic + entry].connect(
        connecting_region=regions[RegionName.happily_skeptic],
        rule=lambda state: state.has(ItemName.happily, world.player) and has_voices(state, world, [ItemName.skeptic])
    )  # Happily Paranoid

    regions[RegionName.happily_opportunist + entry].connect(
        connecting_region=regions[RegionName.happily_opportunist],
        rule=lambda state: state.has(ItemName.happily, world.player) and has_voices(state, world, [ItemName.opportunist])
    )  # Happily Opportunist

    # endregion

    # region Chapter 3 Sub -> Main
    # Needle
    regions[RegionName.needle_hunted].connect(regions[RegionName.needle])
    regions[RegionName.needle_skeptic].connect(regions[RegionName.needle])

    # Fury
    regions[RegionName.fury_pacifism].connect(regions[RegionName.fury])
    regions[RegionName.fury_unarmed_broken].connect(regions[RegionName.fury])
    regions[RegionName.fury_unarmed_contrarian].connect(regions[RegionName.fury])
    regions[RegionName.fury_other].connect(regions[RegionName.fury])
    regions[RegionName.fury_tower].connect(regions[RegionName.fury_tower])

    # Apotheosis
    regions[RegionName.apotheosis_contrarian].connect(regions[RegionName.apotheosis])
    regions[RegionName.apotheosis_paranoid].connect(regions[RegionName.apotheosis])

    # Dragon
    regions[RegionName.dragon_kind].connect(regions[RegionName.dragon])
    regions[RegionName.dragon_harsh].connect(regions[RegionName.dragon])

    # Wraith
    regions[RegionName.wraith_cheated].connect(regions[RegionName.wraith])
    regions[RegionName.wraith_paranoid].connect(regions[RegionName.wraith])
    regions[RegionName.wraith_cold].connect(regions[RegionName.wraith])
    regions[RegionName.wraith_opportunist].connect(regions[RegionName.wraith])

    # Razor No Way
    regions[RegionName.razor_no_way].connect(regions[RegionName.razor_chap3])
    regions[RegionName.razor_no_way_broken].connect(regions[RegionName.razor_no_way])
    regions[RegionName.razor_no_way_paranoid].connect(regions[RegionName.razor_no_way])
    regions[RegionName.razor_no_way_stubborn].connect(regions[RegionName.razor_no_way])

    # Razor Race
    regions[RegionName.razor_race].connect(regions[RegionName.razor_chap3])
    regions[RegionName.razor_race_broken].connect(regions[RegionName.razor_race])
    regions[RegionName.razor_race_paranoid].connect(regions[RegionName.razor_race])
    regions[RegionName.razor_race_stubborn].connect(regions[RegionName.razor_race])

    # Den
    regions[RegionName.den_skeptic].connect(regions[RegionName.den])
    regions[RegionName.den_stubborn].connect(regions[RegionName.den])

    # Wild
    regions[RegionName.wild_beast_broken].connect(regions[RegionName.wild])
    regions[RegionName.wild_beast_contrarian].connect(regions[RegionName.wild])
    regions[RegionName.wild_beast_opportunist].connect(regions[RegionName.wild])
    regions[RegionName.wild_beast_stubborn].connect(regions[RegionName.wild])
    regions[RegionName.wild_witch_stubborn].connect(regions[RegionName.wild])
    regions[RegionName.wild_witch_cheated].connect(regions[RegionName.wild])
    regions[RegionName.wild_witch_paranoid].connect(regions[RegionName.wild])

    # Thorn
    regions[RegionName.thorn_smitten].connect(regions[RegionName.thorn])
    regions[RegionName.thorn_cheated].connect(regions[RegionName.thorn])

    # Cage
    regions[RegionName.cage_paranoid].connect(regions[RegionName.cage])
    regions[RegionName.cage_cheated].connect(regions[RegionName.cage])
    regions[RegionName.cage_broken].connect(regions[RegionName.cage])

    # Grey
    regions[RegionName.grey_drowned].connect(regions[RegionName.grey])
    regions[RegionName.grey_burned].connect(regions[RegionName.grey])

    # Happily
    regions[RegionName.happily_skeptic].connect(regions[RegionName.happily])
    regions[RegionName.happily_opportunist].connect(regions[RegionName.happily])
    # endregion

    # region Chapter 3 + 4 Razor
    regions[RegionName.razor_no_way].connect(regions[RegionName.razor_empty])
    regions[RegionName.razor_race].connect(regions[RegionName.razor_destruction])

    regions[RegionName.razor_empty].connect(
        connecting_region=regions[RegionName.razor_chap4],
        rule=lambda state: has_all_voices(state, world)
    )

    regions[RegionName.razor_destruction].connect(
        connecting_region=regions[RegionName.razor_chap4],
        rule=lambda state: has_all_voices(state, world)
    )
    # endregion

    # region Chapter 3 Dagger Only
    regions[RegionName.wild].connect(
        connecting_region=regions[RegionName.wild_dagger],
        rule=lambda state: has_dagger_for(state, world, ItemName.dagger_wild)
    )  # Chapter III Wild Dagger Only
    # endregion

    # region Special (Furry Weathered Heart)
    regions[RegionName.fury_pacifism].connect(regions[RegionName.fury_weathered_heart])
    regions[RegionName.fury_unarmed_broken].connect(regions[RegionName.fury_weathered_heart])
    regions[RegionName.fury_unarmed_contrarian].connect(regions[RegionName.fury_weathered_heart])
    regions[RegionName.fury_other].connect(regions[RegionName.fury_weathered_heart])
    regions[RegionName.fury_tower].connect(connecting_region=regions[RegionName.fury_weathered_heart],
                                           rule=lambda state: has_dagger_for(state, world, ItemName.dagger_fury))
    # endregion

    # region The Space Between
    regions[RegionName.adversary_dagger].connect(regions[RegionName.space_between])
    regions[RegionName.tower].connect(regions[RegionName.space_between])
    regions[RegionName.spectre].connect(regions[RegionName.space_between])
    regions[RegionName.nightmare].connect(regions[RegionName.space_between])
    regions[RegionName.beast].connect(regions[RegionName.space_between])
    regions[RegionName.witch].connect(regions[RegionName.space_between])
    regions[RegionName.stranger_dagger].connect(regions[RegionName.space_between])
    regions[RegionName.prisoner].connect(regions[RegionName.space_between])
    regions[RegionName.damsel].connect(regions[RegionName.space_between])

    regions[RegionName.needle].connect(regions[RegionName.space_between])
    regions[RegionName.fury].connect(regions[RegionName.space_between])
    regions[RegionName.apotheosis].connect(regions[RegionName.space_between])
    regions[RegionName.dragon].connect(regions[RegionName.space_between])
    regions[RegionName.wraith].connect(regions[RegionName.space_between])
    regions[RegionName.clarity].connect(regions[RegionName.space_between])
    regions[RegionName.den].connect(regions[RegionName.space_between])
    regions[RegionName.wild].connect(regions[RegionName.space_between])
    regions[RegionName.thorn].connect(regions[RegionName.space_between])
    regions[RegionName.cage].connect(regions[RegionName.space_between])
    regions[RegionName.grey].connect(regions[RegionName.space_between])
    regions[RegionName.happily].connect(regions[RegionName.space_between])
    regions[RegionName.razor_chap4].connect(regions[RegionName.space_between])

    regions[RegionName.space_between].connect(regions[RegionName.goddess + entry])
    regions[RegionName.goddess + entry].connect(
        connecting_region=regions[RegionName.goddess],
        rule=lambda state: max_reachable_vessels(state, world) > 4 and state.has(ItemName.goddess, world.player)
    )
    regions[RegionName.goddess].connect(regions[RegionName.win])
    # endregion
