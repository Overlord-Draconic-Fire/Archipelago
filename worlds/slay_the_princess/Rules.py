from typing import List

from BaseClasses import CollectionState
from .Names import ItemName, RegionName

CHAPTER_2_DAGGERS = {
    ItemName.dagger_adversary,
    ItemName.dagger_tower,
    ItemName.dagger_spectre,
    ItemName.dagger_nightmare,
    ItemName.dagger_razor,
    ItemName.dagger_beast,
    ItemName.dagger_witch,
    ItemName.dagger_stranger,
    ItemName.dagger_prisoner,
    ItemName.dagger_damsel,
}

CHAPTER_3_DAGGERS = {
    ItemName.dagger_needle,
    ItemName.dagger_fury,
    ItemName.dagger_apotheosis,
    ItemName.dagger_dragon,
    ItemName.dagger_den,
    ItemName.dagger_wild,
    ItemName.dagger_thorn,
    ItemName.dagger_cage,
    ItemName.dagger_grey,
    ItemName.dagger_happily,
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


def has_dagger_for(state: CollectionState, world, dagger: str) -> bool:
    #mode = world.options.dagger_mode
    mode = 1
    if mode == 0:
        return True
    elif mode == 1:
        return state.has(ItemName.dagger, world.player)
    elif mode == 2:
        if dagger is ItemName.dagger_princess:
            return state.has(ItemName.dagger1, world.player)
        elif dagger in CHAPTER_2_DAGGERS:
            return state.has(ItemName.dagger2, world.player)
        elif dagger in CHAPTER_3_DAGGERS:
            return state.has(ItemName.dagger3, world.player)
        elif dagger is ItemName.dagger_goddess:
            return state.has(ItemName.dagger_goddess, world.player)

    return state.has(dagger, world.player)


def has_voice(state: CollectionState, world, voice: str) -> bool:
    # return not world.options.rando_voice or state.has(voice, world.player)
    return state.has(voice, world.player)


def has_voices(state: CollectionState, world, voices: List[str]) -> bool:
    """if not world.options.rando_voice:
        return True"""

    for voice in voices:
        if not state.has(voice, world.player):
            return False
    return True


def has_all_voices(state: CollectionState, world) -> bool:
    return has_voices(state, world, [ItemName.stubborn, ItemName.broken, ItemName.cold, ItemName.paranoid, ItemName.cheated, ItemName.hunted, ItemName.opportunist, ItemName.contrarian, ItemName.skeptic, ItemName.smitten])


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

    return min(count, state.count(ItemName.gift, world.player))


def test_goal(state: CollectionState, world) -> bool:
    return state.has(ItemName.credits_reached, world.player)
