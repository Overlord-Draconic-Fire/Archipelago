from dataclasses import dataclass
from enum import Enum

from BaseClasses import Region
from .Names import RegionName, ItemName
from .Rules import has_voice, has_all_voices, has_voices, has_blade, has_princess
from .TokenSystem import max_reachable_vessels, can_reach_new_world

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
    RegionName.one_blade: SlayThePrincessRegionData(RegionName.one, Chapter.one, False),
    RegionName.chap2: SlayThePrincessRegionData(RegionName.chap2, Chapter.two, False),
    RegionName.chap3: SlayThePrincessRegionData(RegionName.chap3, Chapter.three, False),

    # Chapters 2
    RegionName.adversary: SlayThePrincessRegionData(RegionName.adversary, Chapter.two),
    RegionName.tower: SlayThePrincessRegionData(RegionName.tower, Chapter.two),
    RegionName.spectre: SlayThePrincessRegionData(RegionName.spectre, Chapter.two),
    RegionName.nightmare: SlayThePrincessRegionData(RegionName.nightmare, Chapter.two),
    RegionName.razor: SlayThePrincessRegionData(RegionName.razor, Chapter.two),
    RegionName.beast: SlayThePrincessRegionData(RegionName.beast, Chapter.two),
    RegionName.witch: SlayThePrincessRegionData(RegionName.witch, Chapter.two),
    RegionName.stranger: SlayThePrincessRegionData(RegionName.stranger, Chapter.two),
    RegionName.prisoner: SlayThePrincessRegionData(RegionName.prisoner, Chapter.two),
    RegionName.damsel: SlayThePrincessRegionData(RegionName.damsel, Chapter.two),

    # Chapters 2 Dagger
    RegionName.adversary_blade: SlayThePrincessRegionData(RegionName.adversary, Chapter.two, False),
    RegionName.tower_blade: SlayThePrincessRegionData(RegionName.tower, Chapter.two, False),
    RegionName.spectre_blade: SlayThePrincessRegionData(RegionName.spectre, Chapter.two, False),
    RegionName.nightmare_blade: SlayThePrincessRegionData(RegionName.nightmare, Chapter.two, False),
    RegionName.razor_blade: SlayThePrincessRegionData(RegionName.razor, Chapter.two, False),
    RegionName.beast_blade: SlayThePrincessRegionData(RegionName.beast, Chapter.two, False),
    RegionName.witch_blade: SlayThePrincessRegionData(RegionName.witch, Chapter.two, False),
    RegionName.stranger_blade: SlayThePrincessRegionData(RegionName.stranger, Chapter.two, False),
    RegionName.prisoner_blade: SlayThePrincessRegionData(RegionName.prisoner, Chapter.two, False),
    RegionName.damsel_blade: SlayThePrincessRegionData(RegionName.damsel, Chapter.two, False),

    # Eye of the Needle
    RegionName.needle: SlayThePrincessRegionData(RegionName.needle, Chapter.three),
    RegionName.needle_blade: SlayThePrincessRegionData(RegionName.needle, Chapter.three, False),
    RegionName.needle_hunted: SlayThePrincessRegionData(RegionName.needle, Chapter.three),
    RegionName.needle_hunted_blade: SlayThePrincessRegionData(RegionName.needle, Chapter.three, False),
    RegionName.needle_skeptic: SlayThePrincessRegionData(RegionName.needle, Chapter.three),

    # Fury
    RegionName.fury: SlayThePrincessRegionData(RegionName.fury, Chapter.three),
    RegionName.fury_weathered_heart: SlayThePrincessRegionData(RegionName.fury, Chapter.three, False),
    RegionName.fury_cold: SlayThePrincessRegionData(RegionName.fury, Chapter.three),
    RegionName.fury_contrarian: SlayThePrincessRegionData(RegionName.fury, Chapter.three),
    RegionName.fury_broken: SlayThePrincessRegionData(RegionName.fury, Chapter.three),
    RegionName.fury_tower: SlayThePrincessRegionData(RegionName.fury, Chapter.three),
    RegionName.fury_tower_blade: SlayThePrincessRegionData(RegionName.fury, Chapter.three, False),
    RegionName.fury_broken_cold: SlayThePrincessRegionData(RegionName.fury, Chapter.three, False),

    # Apotheosis
    RegionName.apotheosis: SlayThePrincessRegionData(RegionName.apotheosis, Chapter.three),
    RegionName.apotheosis_blade: SlayThePrincessRegionData(RegionName.apotheosis, Chapter.three, False),
    RegionName.apotheosis_contrarian: SlayThePrincessRegionData(RegionName.apotheosis, Chapter.three),
    RegionName.apotheosis_contrarian_blade: SlayThePrincessRegionData(RegionName.apotheosis, Chapter.three, False),
    RegionName.apotheosis_paranoid: SlayThePrincessRegionData(RegionName.apotheosis, Chapter.three),
    RegionName.apotheosis_paranoid_blade: SlayThePrincessRegionData(RegionName.apotheosis, Chapter.three, False),

    # Dragon
    RegionName.dragon: SlayThePrincessRegionData(RegionName.dragon, Chapter.three),
    RegionName.dragon_fuse: SlayThePrincessRegionData(RegionName.dragon, Chapter.three, False),
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
    RegionName.clarity_blade: SlayThePrincessRegionData(RegionName.clarity, Chapter.three, False),

    # Razor
    RegionName.razor_chap3: SlayThePrincessRegionData(RegionName.razor_chap3, Chapter.three),
    RegionName.razor_no_way: SlayThePrincessRegionData(RegionName.razor_no_way, Chapter.three),
    RegionName.razor_no_way_broken: SlayThePrincessRegionData(RegionName.razor_no_way, Chapter.three),
    RegionName.razor_no_way_paranoid: SlayThePrincessRegionData(RegionName.razor_no_way, Chapter.three),

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
    RegionName.den_blade: SlayThePrincessRegionData(RegionName.den, Chapter.three, False),
    RegionName.den_skeptic: SlayThePrincessRegionData(RegionName.den, Chapter.three),
    RegionName.den_stubborn: SlayThePrincessRegionData(RegionName.den, Chapter.three),
    RegionName.den_stubborn_blade: SlayThePrincessRegionData(RegionName.den, Chapter.three, False),

    # Wild
    RegionName.wild: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_blade: SlayThePrincessRegionData(RegionName.wild, Chapter.three, False),
    RegionName.wild_beast_broken: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_beast_contrarian: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_beast_opportunist: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_beast_stubborn: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_witch_stubborn: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_witch_cheated: SlayThePrincessRegionData(RegionName.wild, Chapter.three),
    RegionName.wild_witch_paranoid: SlayThePrincessRegionData(RegionName.wild, Chapter.three),

    # Thorn
    RegionName.thorn: SlayThePrincessRegionData(RegionName.thorn, Chapter.three),
    RegionName.thorn_blade: SlayThePrincessRegionData(RegionName.thorn, Chapter.three, False),
    RegionName.thorn_smitten: SlayThePrincessRegionData(RegionName.thorn, Chapter.three),
    RegionName.thorn_smitten_blade: SlayThePrincessRegionData(RegionName.thorn, Chapter.three, False),
    RegionName.thorn_cheated: SlayThePrincessRegionData(RegionName.thorn, Chapter.three),

    # Cage
    RegionName.cage: SlayThePrincessRegionData(RegionName.cage, Chapter.three),
    RegionName.cage_paranoid: SlayThePrincessRegionData(RegionName.cage, Chapter.three),
    RegionName.cage_paranoid_blade: SlayThePrincessRegionData(RegionName.cage, Chapter.three, False),
    RegionName.cage_cheated: SlayThePrincessRegionData(RegionName.cage, Chapter.three),
    RegionName.cage_broken: SlayThePrincessRegionData(RegionName.cage, Chapter.three),
    RegionName.cage_not_paranoid: SlayThePrincessRegionData(RegionName.cage, Chapter.three, False),
    RegionName.cage_new_world: SlayThePrincessRegionData(RegionName.cage, Chapter.three, False),

    # Grey
    RegionName.grey: SlayThePrincessRegionData(RegionName.grey, Chapter.three),
    RegionName.grey_drowned: SlayThePrincessRegionData(RegionName.grey, Chapter.three),
    RegionName.grey_burned: SlayThePrincessRegionData(RegionName.grey, Chapter.three),

    # Happily Ever After
    RegionName.happily: SlayThePrincessRegionData(RegionName.happily, Chapter.three),
    RegionName.happily_blade: SlayThePrincessRegionData(RegionName.happily, Chapter.three, False),
    RegionName.happily_skeptic: SlayThePrincessRegionData(RegionName.happily, Chapter.three),
    RegionName.happily_opportunist: SlayThePrincessRegionData(RegionName.happily, Chapter.three),

    # META
    RegionName.space_between: SlayThePrincessRegionData(RegionName.space_between, Chapter.meta, False),
    RegionName.restart: SlayThePrincessRegionData(RegionName.space_between, Chapter.meta, False),
    RegionName.goddess: SlayThePrincessRegionData(RegionName.goddess, Chapter.meta),
    RegionName.goddess_blade: SlayThePrincessRegionData(RegionName.goddess, Chapter.meta, False),
    RegionName.new_world: SlayThePrincessRegionData(RegionName.goddess, Chapter.meta, False),
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
        connecting_region=regions[RegionName.one_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_princess)
    )  # Chapter I -> Blade Only

    regions[RegionName.one_blade].connect(regions[RegionName.adversary + entry])  # Chapter I -> Adversary
    regions[RegionName.one_blade].connect(regions[RegionName.tower + entry])  # Chapter I -> Tower
    regions[RegionName.one_blade].connect(regions[RegionName.spectre + entry])  # Chapter I -> Spectre
    regions[RegionName.one].connect(regions[RegionName.nightmare + entry])  # Chapter I -> Nightmare
    regions[RegionName.one_blade].connect(regions[RegionName.razor + entry])  # Chapter I -> Razor
    regions[RegionName.one_blade].connect(regions[RegionName.beast + entry])  # Chapter I -> Beast
    regions[RegionName.one_blade].connect(regions[RegionName.witch + entry])  # Chapter I -> Witch
    regions[RegionName.one].connect(regions[RegionName.stranger + entry])  # Chapter I -> Stranger
    regions[RegionName.one_blade].connect(regions[RegionName.prisoner + entry])  # Chapter I -> Prisoner
    regions[RegionName.one].connect(regions[RegionName.damsel + entry])  # Chapter I -> Damsel
    # endregion

    # region Chapter 2 Entry -> Main
    regions[RegionName.adversary + entry].connect(
        connecting_region=regions[RegionName.adversary],
        rule=lambda state: has_princess(state, world, ItemName.adversary) and has_voice(state, world, ItemName.stubborn)
    )  # Chapter II Adversary entry -> Adversary

    regions[RegionName.tower + entry].connect(
        connecting_region=regions[RegionName.tower],
        rule=lambda state: has_princess(state, world, ItemName.tower) and has_voice(state, world, ItemName.broken)
    )  # Chapter II Tower entry -> Tower

    regions[RegionName.spectre + entry].connect(
        connecting_region=regions[RegionName.spectre],
        rule=lambda state: has_princess(state, world, ItemName.spectre) and has_voice(state, world, ItemName.cold)
    )  # Chapter II Spectre entry -> Spectre

    regions[RegionName.nightmare + entry].connect(
        connecting_region=regions[RegionName.nightmare],
        rule=lambda state: has_princess(state, world, ItemName.nightmare) and has_voice(state, world, ItemName.paranoid)
    )  # Chapter II Nightmare entry -> Nightmare

    regions[RegionName.razor + entry].connect(
        connecting_region=regions[RegionName.razor],
        rule=lambda state: has_princess(state, world, ItemName.razor) and has_voice(state, world, ItemName.cheated)
    )  # Chapter II Razor entry -> Razor

    regions[RegionName.beast + entry].connect(
        connecting_region=regions[RegionName.beast],
        rule=lambda state: has_princess(state, world, ItemName.beast) and has_voice(state, world, ItemName.hunted)
    )  # Chapter II Beast entry -> Beast

    regions[RegionName.witch + entry].connect(
        connecting_region=regions[RegionName.witch],
        rule=lambda state: has_princess(state, world, ItemName.witch) and has_voice(state, world, ItemName.opportunist)
    )  # Chapter II Witch entry -> Witch

    regions[RegionName.stranger + entry].connect(
        connecting_region=regions[RegionName.stranger],
        rule=lambda state: has_princess(state, world, ItemName.stranger) and has_voice(state, world, ItemName.contrarian)
    )  # Chapter II Stranger entry -> Stranger

    regions[RegionName.prisoner + entry].connect(
        connecting_region=regions[RegionName.prisoner],
        rule=lambda state: has_princess(state, world, ItemName.prisoner) and has_voice(state, world, ItemName.skeptic)
    )  # Chapter II Prisoner entry -> Prisoner

    regions[RegionName.damsel + entry].connect(
        connecting_region=regions[RegionName.damsel],
        rule=lambda state: has_princess(state, world, ItemName.damsel) and has_voice(state, world, ItemName.smitten)
    )  # Chapter II Damsel entry -> Damsel
    # endregion

    # region Chapter 2 Blade Only
    regions[RegionName.adversary].connect(
        connecting_region=regions[RegionName.adversary_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_adversary)
    )  # Chapter II Adversary Blade Only

    regions[RegionName.tower].connect(
        connecting_region=regions[RegionName.tower_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_tower)
    )  # Chapter II Tower Blade Only

    regions[RegionName.spectre].connect(
        connecting_region=regions[RegionName.spectre_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_spectre)
    )  # Chapter II Spectre Blade Only

    regions[RegionName.nightmare].connect(
        connecting_region=regions[RegionName.nightmare_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_nightmare)
    )  # Chapter II Nightmare Blade Only

    regions[RegionName.razor].connect(
        connecting_region=regions[RegionName.razor_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_razor)
    )  # Chapter II Razor Blade Only

    regions[RegionName.beast].connect(
        connecting_region=regions[RegionName.beast_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_beast)
    )  # Chapter II Beast Blade Only

    regions[RegionName.witch].connect(
        connecting_region=regions[RegionName.witch_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_witch)
    )  # Chapter II Witch Blade Only

    regions[RegionName.stranger].connect(
        connecting_region=regions[RegionName.stranger_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_stranger)
    )  # Chapter II Stranger Blade Only

    regions[RegionName.prisoner].connect(
        connecting_region=regions[RegionName.prisoner_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_prisoner)
    )  # Chapter II Prisoner Blade Only

    regions[RegionName.damsel].connect(
        connecting_region=regions[RegionName.damsel_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_damsel)
    )  # Chapter II Damsel Blade Only

    # endregion

    # region Chapter 2 -> Chapter 3 Sub Entry
    # Adversary → Needle / Fury (entry)
    regions[RegionName.adversary_blade].connect(regions[RegionName.needle_hunted + entry])
    regions[RegionName.adversary_blade].connect(regions[RegionName.needle_skeptic + entry])

    regions[RegionName.adversary].connect(regions[RegionName.fury_broken + entry])
    regions[RegionName.adversary].connect(regions[RegionName.fury_cold + entry])
    regions[RegionName.adversary].connect(regions[RegionName.fury_contrarian + entry])

    # Tower → Apotheosis / Fury Tower (entry)
    regions[RegionName.tower_blade].connect(regions[RegionName.fury_tower + entry])

    regions[RegionName.tower_blade].connect(regions[RegionName.apotheosis_contrarian + entry])
    regions[RegionName.tower].connect(regions[RegionName.apotheosis_paranoid + entry])

    # Spectre → Dragon / Wraith (entry)
    regions[RegionName.spectre_blade].connect(regions[RegionName.dragon_kind + entry])
    regions[RegionName.spectre_blade].connect(regions[RegionName.dragon_harsh + entry])

    regions[RegionName.spectre].connect(regions[RegionName.wraith_cheated + entry])
    regions[RegionName.spectre].connect(regions[RegionName.wraith_paranoid + entry])

    # Nightmare → Clarity / Wraith (entry)
    regions[RegionName.nightmare].connect(regions[RegionName.clarity + entry])

    regions[RegionName.nightmare_blade].connect(regions[RegionName.wraith_cold + entry])
    regions[RegionName.nightmare_blade].connect(regions[RegionName.wraith_opportunist + entry])

    # Razor → No Way / Race (entry)
    regions[RegionName.razor].connect(regions[RegionName.razor_no_way_broken + entry])
    regions[RegionName.razor].connect(regions[RegionName.razor_no_way_paranoid + entry])

    regions[RegionName.razor_blade].connect(regions[RegionName.razor_race_broken + entry])
    regions[RegionName.razor_blade].connect(regions[RegionName.razor_race_paranoid + entry])
    regions[RegionName.razor_blade].connect(regions[RegionName.razor_race_stubborn + entry])

    # Beast → Den / Wild (entry)
    regions[RegionName.beast].connect(regions[RegionName.den_skeptic + entry])
    regions[RegionName.beast_blade].connect(regions[RegionName.den_stubborn + entry])

    regions[RegionName.beast].connect(regions[RegionName.wild_beast_broken + entry])
    regions[RegionName.beast].connect(regions[RegionName.wild_beast_contrarian + entry])
    regions[RegionName.beast_blade].connect(regions[RegionName.wild_beast_opportunist + entry])
    regions[RegionName.beast_blade].connect(regions[RegionName.wild_beast_stubborn + entry])

    # Witch → Thorn / Wild (entry)
    regions[RegionName.witch_blade].connect(regions[RegionName.thorn_smitten + entry])
    regions[RegionName.witch_blade].connect(regions[RegionName.thorn_cheated + entry])

    regions[RegionName.witch_blade].connect(regions[RegionName.wild_witch_stubborn + entry])
    regions[RegionName.witch_blade].connect(regions[RegionName.wild_witch_cheated + entry])
    regions[RegionName.witch].connect(regions[RegionName.wild_witch_paranoid + entry])

    # Prisoner → Cage / Grey (entry)
    regions[RegionName.prisoner_blade].connect(regions[RegionName.cage_paranoid + entry])
    regions[RegionName.prisoner].connect(regions[RegionName.cage_cheated + entry])
    regions[RegionName.prisoner].connect(regions[RegionName.cage_broken + entry])

    regions[RegionName.prisoner_blade].connect(regions[RegionName.grey_drowned + entry])

    # Damsel → Happily / Grey Burned (entry)
    regions[RegionName.damsel].connect(regions[RegionName.happily_skeptic + entry])
    regions[RegionName.damsel].connect(regions[RegionName.happily_opportunist + entry])

    regions[RegionName.damsel_blade].connect(regions[RegionName.grey_burned + entry])
    # endregion

    # region Chapter 3 Sub Entry -> Main Entry
    # Needle (entry)
    regions[RegionName.needle_hunted + entry].connect(regions[RegionName.needle + entry])
    regions[RegionName.needle_skeptic + entry].connect(regions[RegionName.needle + entry])

    # Fury (entry)
    regions[RegionName.fury_cold + entry].connect(regions[RegionName.fury + entry])
    regions[RegionName.fury_contrarian + entry].connect(regions[RegionName.fury + entry])
    regions[RegionName.fury_broken + entry].connect(regions[RegionName.fury + entry])
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
        rule=lambda state: has_princess(state, world, ItemName.needle) and has_voices(state, world, [ItemName.stubborn, ItemName.hunted])
    )  # Needle Hunted

    regions[RegionName.needle_skeptic + entry].connect(
        connecting_region=regions[RegionName.needle_skeptic],
        rule=lambda state: has_princess(state, world, ItemName.needle) and has_voices(state, world, [ItemName.stubborn, ItemName.skeptic])
    )  # Needle Skeptic

    # Fury (entry)
    regions[RegionName.fury_cold + entry].connect(
        connecting_region=regions[RegionName.fury_cold],
        rule=lambda state: has_princess(state, world, ItemName.fury) and has_voices(state, world, [ItemName.stubborn, ItemName.cold])
    )  # Fury Cold

    regions[RegionName.fury_contrarian + entry].connect(
        connecting_region=regions[RegionName.fury_contrarian],
        rule=lambda state: has_princess(state, world, ItemName.fury) and has_voices(state, world, [ItemName.stubborn, ItemName.contrarian])
    )  # Fury Unarmed Contrarian

    regions[RegionName.fury_broken + entry].connect(
        connecting_region=regions[RegionName.fury_broken],
        rule=lambda state: has_princess(state, world, ItemName.fury) and has_voices(state, world, [ItemName.stubborn, ItemName.broken])
    )  # Fury Broken

    regions[RegionName.fury_tower + entry].connect(
        connecting_region=regions[RegionName.fury_tower],
        rule=lambda state: has_princess(state, world, ItemName.fury) and has_voices(state, world, [ItemName.broken, ItemName.stubborn])
    )  # Fury Tower

    # Apotheosis (entry)
    regions[RegionName.apotheosis_contrarian + entry].connect(
        connecting_region=regions[RegionName.apotheosis_contrarian],
        rule=lambda state: has_princess(state, world, ItemName.apotheosis) and has_voices(state, world, [ItemName.broken, ItemName.contrarian])
    )  # Apotheosis Contrarian

    regions[RegionName.apotheosis_paranoid + entry].connect(
        connecting_region=regions[RegionName.apotheosis_paranoid],
        rule=lambda state: has_princess(state, world, ItemName.apotheosis) and has_voices(state, world, [ItemName.broken, ItemName.paranoid])
    )  # Apotheosis Paranoid

    # Dragon (entry)
    regions[RegionName.dragon_kind + entry].connect(
        connecting_region=regions[RegionName.dragon_kind],
        rule=lambda state: has_princess(state, world, ItemName.dragon) and has_voices(state, world, [ItemName.cold, ItemName.opportunist])
    )  # Dragon Kind

    regions[RegionName.dragon_harsh + entry].connect(
        connecting_region=regions[RegionName.dragon_harsh],
        rule=lambda state: has_princess(state, world, ItemName.dragon) and has_voices(state, world, [ItemName.cold, ItemName.opportunist])
    )  # Dragon Harsh

    # Wraith (entry)
    regions[RegionName.wraith_cheated + entry].connect(
        connecting_region=regions[RegionName.wraith_cheated],
        rule=lambda state: has_princess(state, world, ItemName.wraith) and has_voices(state, world, [ItemName.cold, ItemName.cheated])
    )  # Wraith Cheated

    regions[RegionName.wraith_paranoid + entry].connect(
        connecting_region=regions[RegionName.wraith_paranoid],
        rule=lambda state: has_princess(state, world, ItemName.wraith) and has_voices(state, world, [ItemName.cold, ItemName.paranoid])
    )  # Wraith Paranoid

    regions[RegionName.wraith_cold + entry].connect(
        connecting_region=regions[RegionName.wraith_cold],
        rule=lambda state: has_princess(state, world, ItemName.wraith) and has_voices(state, world, [ItemName.paranoid, ItemName.cold])
    )  # Wraith Cold

    regions[RegionName.wraith_opportunist + entry].connect(
        connecting_region=regions[RegionName.wraith_opportunist],
        rule=lambda state: has_princess(state, world, ItemName.wraith) and has_voices(state, world, [ItemName.paranoid, ItemName.opportunist])
    )  # Wraith Opportunist

    # Clarity (entry)
    regions[RegionName.clarity + entry].connect(
        connecting_region=regions[RegionName.clarity],
        rule=lambda state: has_princess(state, world, ItemName.clarity) and has_all_voices(state, world)
    )  # Clarity

    # Razor No Way (entry)
    regions[RegionName.razor_no_way_broken + entry].connect(
        connecting_region=regions[RegionName.razor_no_way_broken],
        rule=lambda state: has_princess(state, world, ItemName.razor) and has_all_voices(state, world)
    )  # Razor No Way Broken

    regions[RegionName.razor_no_way_paranoid + entry].connect(
        connecting_region=regions[RegionName.razor_no_way_paranoid],
        rule=lambda state: has_princess(state, world, ItemName.razor) and has_all_voices(state, world)
    )  # Razor No Way Paranoid

    # Razor Race (entry)
    regions[RegionName.razor_race_broken + entry].connect(
        connecting_region=regions[RegionName.razor_race_broken],
        rule=lambda state: has_princess(state, world, ItemName.razor) and has_all_voices(state, world)
    )  # Razor Race Broken

    regions[RegionName.razor_race_paranoid + entry].connect(
        connecting_region=regions[RegionName.razor_race_paranoid],
        rule=lambda state: has_princess(state, world, ItemName.razor) and has_all_voices(state, world)
    )  # Razor Race Paranoid

    regions[RegionName.razor_race_stubborn + entry].connect(
        connecting_region=regions[RegionName.razor_race_stubborn],
        rule=lambda state: has_princess(state, world, ItemName.razor) and has_all_voices(state, world)
    )  # Razor Race Stubborn

    # Den (entry)
    regions[RegionName.den_skeptic + entry].connect(
        connecting_region=regions[RegionName.den_skeptic],
        rule=lambda state: has_princess(state, world, ItemName.den) and has_voices(state, world, [ItemName.hunted, ItemName.skeptic])
    )  # Den Skeptic

    regions[RegionName.den_stubborn + entry].connect(
        connecting_region=regions[RegionName.den_stubborn],
        rule=lambda state: has_princess(state, world, ItemName.den) and has_voices(state, world, [ItemName.hunted, ItemName.stubborn])
    )  # Den Stubborn

    # Wild (entry)
    regions[RegionName.wild_beast_broken + entry].connect(
        connecting_region=regions[RegionName.wild_beast_broken],
        rule=lambda state: has_princess(state, world, ItemName.wild) and has_voices(state, world, [ItemName.hunted, ItemName.broken])
    )  # Wild Beast Broken

    regions[RegionName.wild_beast_contrarian + entry].connect(
        connecting_region=regions[RegionName.wild_beast_contrarian],
        rule=lambda state: has_princess(state, world, ItemName.wild) and has_voices(state, world, [ItemName.hunted, ItemName.contrarian])
    )  # Wild Beast Contrarian

    regions[RegionName.wild_beast_opportunist + entry].connect(
        connecting_region=regions[RegionName.wild_beast_opportunist],
        rule=lambda state: has_princess(state, world, ItemName.wild) and has_voices(state, world, [ItemName.hunted, ItemName.opportunist])
    )  # Wild Beast Opportunist

    regions[RegionName.wild_beast_stubborn + entry].connect(
        connecting_region=regions[RegionName.wild_beast_stubborn],
        rule=lambda state: has_princess(state, world, ItemName.wild) and has_voices(state, world, [ItemName.hunted, ItemName.stubborn])
    )  # Wild Beast Stubborn

    regions[RegionName.wild_witch_stubborn + entry].connect(
        connecting_region=regions[RegionName.wild_witch_stubborn],
        rule=lambda state: has_princess(state, world, ItemName.wild) and has_voices(state, world, [ItemName.opportunist, ItemName.stubborn])
    )  # Wild Witch Stubborn

    regions[RegionName.wild_witch_cheated + entry].connect(
        connecting_region=regions[RegionName.wild_witch_cheated],
        rule=lambda state: has_princess(state, world, ItemName.wild) and has_voices(state, world, [ItemName.opportunist, ItemName.cheated])
    )  # Wild Witch Cheated

    regions[RegionName.wild_witch_paranoid + entry].connect(
        connecting_region=regions[RegionName.wild_witch_paranoid],
        rule=lambda state: has_princess(state, world, ItemName.wild) and has_voices(state, world, [ItemName.opportunist, ItemName.paranoid])
    )  # Wild Witch Paranoid

    # Thorn (entry)
    regions[RegionName.thorn_smitten + entry].connect(
        connecting_region=regions[RegionName.thorn_smitten],
        rule=lambda state: has_princess(state, world, ItemName.thorn) and has_voices(state, world, [ItemName.opportunist, ItemName.smitten])
    )  # Thorn Smitten

    regions[RegionName.thorn_cheated + entry].connect(
        connecting_region=regions[RegionName.thorn_cheated],
        rule=lambda state: has_princess(state, world, ItemName.thorn) and has_voices(state, world, [ItemName.opportunist, ItemName.cheated])
    )  # Thorn Cheated

    # Cage (entry)
    regions[RegionName.cage_paranoid + entry].connect(
        connecting_region=regions[RegionName.cage_paranoid],
        rule=lambda state: has_princess(state, world, ItemName.cage) and has_voices(state, world, [ItemName.skeptic, ItemName.paranoid])
    )  # Cage Paranoid

    regions[RegionName.cage_cheated + entry].connect(
        connecting_region=regions[RegionName.cage_cheated],
        rule=lambda state: has_princess(state, world, ItemName.cage) and has_voices(state, world, [ItemName.skeptic, ItemName.cheated])
    )  # Cage Cheated

    regions[RegionName.cage_broken + entry].connect(
        connecting_region=regions[RegionName.cage_broken],
        rule=lambda state: has_princess(state, world, ItemName.cage) and has_voices(state, world, [ItemName.skeptic, ItemName.broken])
    )  # Cage Broken

    # Grey (entry)
    regions[RegionName.grey_drowned + entry].connect(
        connecting_region=regions[RegionName.grey_drowned],
        rule=lambda state: has_princess(state, world, ItemName.grey) and has_voices(state, world, [ItemName.skeptic, ItemName.cold])
    )  # Grey Drowned

    regions[RegionName.grey_burned + entry].connect(
        connecting_region=regions[RegionName.grey_burned],
        rule=lambda state: has_princess(state, world, ItemName.grey) and has_voices(state, world, [ItemName.smitten, ItemName.cold])
    )  # Grey Burned

    # Happily (entry)
    regions[RegionName.happily_skeptic + entry].connect(
        connecting_region=regions[RegionName.happily_skeptic],
        rule=lambda state: has_princess(state, world, ItemName.happily) and has_voices(state, world, [ItemName.skeptic])
    )  # Happily Paranoid

    regions[RegionName.happily_opportunist + entry].connect(
        connecting_region=regions[RegionName.happily_opportunist],
        rule=lambda state: has_princess(state, world, ItemName.happily) and has_voices(state, world, [ItemName.opportunist])
    )  # Happily Opportunist

    # endregion

    # region Chapter 3 Sub -> Main
    # Needle
    regions[RegionName.needle_hunted].connect(regions[RegionName.needle])
    regions[RegionName.needle_skeptic].connect(regions[RegionName.needle])

    # Fury
    regions[RegionName.fury_cold].connect(regions[RegionName.fury])
    regions[RegionName.fury_contrarian].connect(regions[RegionName.fury])
    regions[RegionName.fury_broken].connect(regions[RegionName.fury])
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
    regions[RegionName.razor_no_way].connect(
        connecting_region=regions[RegionName.razor_empty],
        rule=lambda state: has_all_voices(state, world)
    )
    regions[RegionName.razor_race].connect(
        connecting_region=regions[RegionName.razor_destruction],
        rule=lambda state: has_all_voices(state, world)
    )

    regions[RegionName.razor_empty].connect(regions[RegionName.razor_chap4])
    regions[RegionName.razor_destruction].connect(regions[RegionName.razor_chap4])
    # endregion

    # region Chapter 3 Blade Only
    regions[RegionName.needle].connect(
        connecting_region=regions[RegionName.needle_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_needle)
    )  # Chapter III Needle Blade Only

    regions[RegionName.needle_hunted].connect(
        connecting_region=regions[RegionName.needle_hunted_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_needle)
    )  # Chapter III Needle (Hunted) Blade Only

    regions[RegionName.fury_tower].connect(
        connecting_region=regions[RegionName.fury_tower_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_fury)
    )  # Chapter III Fury (Tower) Blade Only

    regions[RegionName.apotheosis].connect(
        connecting_region=regions[RegionName.apotheosis_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_apotheosis)
    )  # Chapter III Apotheosis Blade Only

    regions[RegionName.apotheosis_contrarian].connect(
        connecting_region=regions[RegionName.apotheosis_contrarian_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_apotheosis)
    )  # Chapter III Apotheosis (Contrarian) Blade Only

    regions[RegionName.apotheosis_paranoid].connect(
        connecting_region=regions[RegionName.apotheosis_paranoid_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_apotheosis)
    )  # Chapter III Apotheosis (Paranoid) Blade Only

    regions[RegionName.den].connect(
        connecting_region=regions[RegionName.den_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_den)
    )  # Chapter III Den Blade Only

    regions[RegionName.den_stubborn].connect(
        connecting_region=regions[RegionName.den_stubborn_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_den)
    )  # Chapter III Den (Stubborn) Blade Only

    regions[RegionName.wild].connect(
        connecting_region=regions[RegionName.wild_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_wild)
    )  # Chapter III Wild Blade Only

    regions[RegionName.thorn].connect(
        connecting_region=regions[RegionName.thorn_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_thorn)
    )  # Chapter III Thorn Blade Only

    regions[RegionName.thorn_smitten].connect(
        connecting_region=regions[RegionName.thorn_smitten_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_thorn)
    )  # Chapter III Thorn (Smitten) Blade Only

    regions[RegionName.cage_paranoid].connect(
        connecting_region=regions[RegionName.cage_paranoid_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_cage)
    )  # Chapter III Cage (Paranoid) Blade Only

    regions[RegionName.happily].connect(
        connecting_region=regions[RegionName.happily_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_happily)
    )  # Chapter III Happily Ever After Blade Only

    regions[RegionName.clarity].connect(
        connecting_region=regions[RegionName.clarity_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_clarity)
    )  # Chapter ??? Clarity Blade Only
    # endregion

    # region Special Furry
    # Fury Broken or Cold
    regions[RegionName.fury_cold].connect(regions[RegionName.fury_broken_cold])
    regions[RegionName.fury_broken].connect(regions[RegionName.fury_broken_cold])

    # Weathered Heart
    regions[RegionName.fury_broken_cold].connect(regions[RegionName.fury_weathered_heart])
    regions[RegionName.fury_contrarian].connect(regions[RegionName.fury_weathered_heart])
    regions[RegionName.fury_tower].connect(
        connecting_region=regions[RegionName.fury_weathered_heart],
        rule=lambda state: has_blade(state, world, ItemName.blade_fury)
    )
    # endregion

    # region Special Dragon
    regions[RegionName.dragon_harsh].connect(regions[RegionName.dragon_fuse])
    regions[RegionName.dragon_kind].connect(
        connecting_region=regions[RegionName.dragon_fuse],
        rule=lambda state: has_blade(state, world, ItemName.blade_dragon)
    )
    # endregion

    # region Special Cage
    regions[RegionName.cage_broken].connect(regions[RegionName.cage_not_paranoid])
    regions[RegionName.cage_cheated].connect(regions[RegionName.cage_not_paranoid])

    regions[RegionName.cage_not_paranoid].connect(regions[RegionName.cage_new_world])
    regions[RegionName.cage_paranoid_blade].connect(regions[RegionName.cage_new_world])
    # endregion

    # region The Space Between
    regions[RegionName.adversary_blade].connect(regions[RegionName.space_between])
    regions[RegionName.tower].connect(regions[RegionName.space_between])
    regions[RegionName.spectre].connect(regions[RegionName.space_between])
    regions[RegionName.nightmare].connect(regions[RegionName.space_between])
    regions[RegionName.beast].connect(regions[RegionName.space_between])
    regions[RegionName.witch].connect(regions[RegionName.space_between])
    regions[RegionName.stranger_blade].connect(regions[RegionName.space_between])
    regions[RegionName.prisoner].connect(regions[RegionName.space_between])
    regions[RegionName.damsel].connect(regions[RegionName.space_between])

    regions[RegionName.needle].connect(regions[RegionName.space_between])
    regions[RegionName.fury].connect(regions[RegionName.space_between])
    regions[RegionName.apotheosis].connect(regions[RegionName.space_between])
    regions[RegionName.dragon].connect(regions[RegionName.space_between])
    regions[RegionName.wraith].connect(regions[RegionName.space_between])
    regions[RegionName.clarity_blade].connect(regions[RegionName.space_between])
    regions[RegionName.den].connect(regions[RegionName.space_between])
    regions[RegionName.wild].connect(regions[RegionName.space_between])
    regions[RegionName.thorn].connect(regions[RegionName.space_between])
    regions[RegionName.cage].connect(regions[RegionName.space_between])
    regions[RegionName.grey].connect(regions[RegionName.space_between])
    regions[RegionName.happily].connect(regions[RegionName.space_between])
    regions[RegionName.razor_chap4].connect(regions[RegionName.space_between])
    # endregion

    # region The Goddess
    regions[RegionName.space_between].connect(regions[RegionName.goddess + entry])
    regions[RegionName.goddess + entry].connect(
        connecting_region=regions[RegionName.restart],
        rule = lambda state: max_reachable_vessels(state, world,1) and has_princess(state, world, ItemName.goddess)
    )
    regions[RegionName.goddess + entry].connect(
        connecting_region=regions[RegionName.goddess],
        rule=lambda state: max_reachable_vessels(state, world, 5) and has_princess(state, world, ItemName.goddess)
    )
    regions[RegionName.goddess].connect(
        connecting_region=regions[RegionName.goddess_blade],
        rule=lambda state: has_blade(state, world, ItemName.blade_goddess)
    )
    regions[RegionName.goddess].connect(
        connecting_region=regions[RegionName.new_world],
        rule=lambda state: can_reach_new_world(state, world)
    )

    regions[RegionName.goddess].connect(regions[RegionName.win])
    # endregion
