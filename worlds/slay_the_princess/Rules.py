from functools import lru_cache
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

OBLIVION_REGIONS = {
    RegionName.adversary,
    RegionName.tower,
    RegionName.spectre,
    RegionName.nightmare,
    RegionName.beast,
    RegionName.witch,
    RegionName.prisoner,
    RegionName.damsel,
    RegionName.needle,
    RegionName.fury,
    RegionName.wraith,
    RegionName.clarity,
    RegionName.den,
    RegionName.thorn,
    RegionName.cage,
    RegionName.grey,
}


#FONCTION MERDIQUE (à supprimer dès que possible)
def can_reach_region_without(state: CollectionState, world, target_region_name: str, forbidden: list[str]) -> bool:
    from .Regions import region_data_table
    from collections import deque

    target_region = world.multiworld.get_region(target_region_name, world.player)
    if target_region in forbidden:
        return False

    starting_region = world.multiworld.get_region(RegionName.menu, world.player)
    queue = deque([starting_region])
    visited = set()

    while queue:
        region = queue.popleft()

        if region in visited:
            continue
        if region in forbidden:
            continue

        visited.add(region)

        if region == target_region:
            return True

        for entrance in region.exits:
            if entrance.connected_region is None:
                continue

            if entrance.connected_region in visited:
                continue

            # règle normale
            if not entrance.can_reach(state):
                continue

            queue.append(entrance.connected_region)

    return False


#FONCTION MERDIQUE (à cause de can_reach + can_reach_region_without)
def can_reach_oblivion(state: CollectionState, world) -> bool:
    return (
        any(state.can_reach_region(region, world.player) for region in OBLIVION_REGIONS)
        or (can_reach_region_without(state, world, RegionName.restart, [RegionName.stranger]) and state.can_reach_region(RegionName.stranger_blade, world.player))
    )


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
