from typing import List

from BaseClasses import CollectionState
from .Names import ItemName, RegionName

CHAPTER_2_BLADES = {
    ItemName.blade_adversary,
    ItemName.blade_tower,
    ItemName.blade_spectre,
    ItemName.blade_nightmare,
    ItemName.blade_razor,
    ItemName.blade_beast,
    ItemName.blade_witch,
    ItemName.blade_stranger,
    ItemName.blade_prisoner,
    ItemName.blade_damsel,
}

CHAPTER_3_BLADES = {
    ItemName.blade_needle,
    ItemName.blade_fury,
    ItemName.blade_apotheosis,
    ItemName.blade_dragon,
    ItemName.blade_den,
    ItemName.blade_wild,
    ItemName.blade_thorn,
    ItemName.blade_cage,
    ItemName.blade_grey,
    ItemName.blade_happily,
}

VESSEL_GRAPH = {
    # --- CHAPITRE 2 ---
    RegionName.adversary: (RegionName.fury, RegionName.tower),
    RegionName.tower: (RegionName.apotheosis, RegionName.adversary),
    RegionName.spectre: (RegionName.dragon, RegionName.nightmare),
    RegionName.nightmare: (RegionName.clarity, RegionName.spectre),
    RegionName.razor: (RegionName.razor, None),
    RegionName.beast: (RegionName.den, RegionName.witch),
    RegionName.witch: (RegionName.thorn, RegionName.beast),
    RegionName.stranger: (RegionName.stranger, None),
    RegionName.prisoner: (RegionName.cage, RegionName.damsel),
    RegionName.damsel: (RegionName.happily, RegionName.prisoner),

    # --- CHAPITRE 3 (terminaux) ---
    RegionName.needle: (None, None),
    RegionName.fury: (None, None),
    RegionName.apotheosis: (None, None),
    RegionName.dragon: (None, None),
    RegionName.wraith: (None, None),
    RegionName.clarity: (None, None),
    RegionName.den: (None, None),
    RegionName.wild: (None, None),
    RegionName.thorn: (None, None),
    RegionName.cage: (None, None),
    RegionName.grey: (None, None),
    RegionName.happily: (None, None),
}


def has_blade(state: CollectionState, world, blade: str) -> bool:
    mode = world.options.pristine_blade_rando
    if mode == 0:
        return True
    elif mode == 1:
        return state.has(ItemName.blade, world.player)
    elif mode == 2:
        if blade is ItemName.blade_princess:
            return state.has(ItemName.blade1, world.player)
        elif blade in CHAPTER_2_BLADES:
            return state.has(ItemName.blade2, world.player)
        elif blade in CHAPTER_3_BLADES:
            return state.has(ItemName.blade3, world.player)
        elif blade is ItemName.blade_goddess:
            return state.has(ItemName.blade_goddess, world.player)

    return state.has(blade, world.player)

def has_princess(state: CollectionState, world, princess: str) -> bool:
    return world.options.chapter_access in [0, 2] or state.has(princess, world.player)

def has_voice(state: CollectionState, world, voice: str) -> bool:
    return world.options.chapter_access in [0, 1] or state.has(voice, world.player)


def has_voices(state: CollectionState, world, voices: List[str]) -> bool:
    if world.options.chapter_access in [0, 1]:
        return True

    for voice in voices:
        if not state.has(voice, world.player):
            return False
    return True


def has_all_voices(state: CollectionState, world) -> bool:
    return world.options.chapter_access in [0, 1] or has_voices(state, world, [ItemName.stubborn, ItemName.broken, ItemName.cold, ItemName.paranoid, ItemName.cheated, ItemName.hunted, ItemName.opportunist, ItemName.contrarian, ItemName.skeptic, ItemName.smitten])


def max_reachable_vessels(state: CollectionState, world) -> int:
    reachable = {
        r for r in VESSEL_GRAPH if state.can_reach(r, "Region", world.player)
    }

    used = set()
    count = 0

    for chap2 in reachable:
        if chap2 in used:
            continue

        chap3, sister = VESSEL_GRAPH[chap2]

        used.add(chap2)

        if chap3 and chap3 in reachable:
            used.add(chap3)
            count += 1
        elif sister and sister in reachable:
            used.add(sister)
            count += 1
        elif chap2 == chap3:
            count += 1

        if count >= 5:
            break

    if world.options.gift_rando:
        max_count = state.count(ItemName.gift, world.player)
    else:
        max_count = 5

    return min(count, max_count)


def test_goal(state: CollectionState, world) -> bool:
    return state.has(ItemName.credits_reached, world.player)
