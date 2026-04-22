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

OBLIVION_REGIONS = (
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
)

# Each group represents one collectible heart, possibly with multiple route variants.
# Every option is (target_region, prerequisite_regions_to_consume).
HEART_GROUPS = (
    ((RegionName.adversary_blade,), (
        (RegionName.adversary_blade, (RegionName.adversary,)),
    )),
    ((RegionName.tower,), (
        (RegionName.tower, (RegionName.tower,)),
    )),
    ((RegionName.spectre,), (
        (RegionName.spectre, (RegionName.spectre,)),
    )),
    ((RegionName.nightmare,), (
        (RegionName.nightmare, (RegionName.nightmare,)),
    )),
    ((RegionName.razor_destruction, RegionName.razor_empty), (
        (RegionName.razor_destruction, (RegionName.razor, RegionName.razor_chap4)),
        (RegionName.razor_empty, (RegionName.razor, RegionName.razor_chap4)),
    )),
    ((RegionName.beast,), (
        (RegionName.beast, (RegionName.beast,)),
    )),
    ((RegionName.witch,), (
        (RegionName.witch, (RegionName.witch,)),
    )),
    ((RegionName.stranger_blade,), (
        (RegionName.stranger_blade, (RegionName.stranger,)),
    )),
    ((RegionName.prisoner,), (
        (RegionName.prisoner, (RegionName.prisoner,)),
    )),
    ((RegionName.damsel,), (
        (RegionName.damsel, (RegionName.damsel,)),
    )),
    ((RegionName.needle,), (
        (RegionName.needle, (RegionName.adversary, RegionName.needle)),
    )),
    ((RegionName.fury_weathered_heart, RegionName.fury,), (
        (RegionName.fury_weathered_heart, (RegionName.adversary, RegionName.fury)),
        (RegionName.fury_weathered_heart, (RegionName.tower, RegionName.fury)),
        (RegionName.fury, (RegionName.adversary, RegionName.fury)),
        (RegionName.fury, (RegionName.tower, RegionName.fury)),
    )),
    ((RegionName.apotheosis,), (
        (RegionName.apotheosis, (RegionName.tower, RegionName.apotheosis)),
    )),
    ((RegionName.dragon, RegionName.dragon_fuse), (
        (RegionName.dragon, (RegionName.spectre, RegionName.dragon)),
        (RegionName.dragon_fuse, (RegionName.spectre, RegionName.dragon)),
    )),
    ((RegionName.wraith,), (
        (RegionName.wraith, (RegionName.spectre, RegionName.wraith)),
        (RegionName.wraith, (RegionName.nightmare, RegionName.wraith)),
    )),
    ((RegionName.clarity_blade,), (
        (RegionName.clarity_blade, (RegionName.nightmare, RegionName.clarity)),
    )),
    ((RegionName.den,), (
        (RegionName.den, (RegionName.beast, RegionName.den)),
    )),
    ((RegionName.wild, RegionName.wild_blade), (
        (RegionName.wild, (RegionName.beast, RegionName.wild)),
        (RegionName.wild_blade, (RegionName.witch, RegionName.wild)),
    )),
    ((RegionName.thorn,), (
        (RegionName.thorn, (RegionName.witch, RegionName.thorn)),
    )),
    ((RegionName.cage,), (
        (RegionName.cage, (RegionName.prisoner, RegionName.cage)),
    )),
    ((RegionName.grey_burned, RegionName.grey_drowned), (
        (RegionName.grey_burned, (RegionName.damsel, RegionName.grey)),
        (RegionName.grey_drowned, (RegionName.prisoner, RegionName.grey)),
    )),
    ((RegionName.happily,), (
        (RegionName.happily, (RegionName.damsel, RegionName.happily)),
    )),
)

NEW_WORLD_GROUPS = (
    ((RegionName.damsel,), (
        (RegionName.damsel, (RegionName.damsel,)),
    )),
    ((RegionName.razor_chap4,), (
        (RegionName.razor_chap4, (RegionName.razor, RegionName.razor_chap4)),
    )),
    ((RegionName.stranger,), (
        (RegionName.stranger, (RegionName.stranger,)),
    )),
    ((RegionName.apotheosis,), (
        (RegionName.apotheosis, (RegionName.tower, RegionName.apotheosis)),
    )),
    ((RegionName.cage_not_paranoid, RegionName.cage_paranoid_blade), (
        (RegionName.cage_not_paranoid, (RegionName.prisoner, RegionName.cage)),
        (RegionName.cage_paranoid_blade, (RegionName.prisoner, RegionName.cage)),
    )),
    ((RegionName.den_blade,), (
        (RegionName.den_blade, (RegionName.beast, RegionName.den)),
    )),
    ((RegionName.needle_hunted_blade,), (
        (RegionName.needle_hunted_blade, (RegionName.adversary, RegionName.needle)),
    )),
    ((RegionName.fury_weathered_heart,), (
        (RegionName.fury_weathered_heart, (RegionName.adversary, RegionName.fury)),
        (RegionName.fury_weathered_heart, (RegionName.tower, RegionName.fury)),
    )),
    ((RegionName.grey,), (
        (RegionName.grey, (RegionName.prisoner, RegionName.grey)),
        (RegionName.grey, (RegionName.damsel, RegionName.grey)),
    )),
    ((RegionName.happily_blade,), (
        (RegionName.happily_blade, (RegionName.damsel, RegionName.happily)),
    )),
    ((RegionName.dragon_kind,), (
        (RegionName.dragon_kind, (RegionName.spectre, RegionName.dragon)),
    )),
    ((RegionName.wild_blade,), (
        (RegionName.wild_blade, (RegionName.beast, RegionName.wild)),
        (RegionName.wild_blade, (RegionName.witch, RegionName.wild)),
    )),
    ((RegionName.wraith,), (
        (RegionName.wraith, (RegionName.spectre, RegionName.wraith)),
        (RegionName.wraith, (RegionName.nightmare, RegionName.wraith)),
    )),
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


def can_reach_region_without(state: CollectionState, world, target_region: str, blocked_regions: frozenset[str]) -> bool:
    if target_region in blocked_regions:
        return False

    starting_region = world.multiworld.get_region(RegionName.menu, world.player)
    queue = [starting_region]
    visited = {starting_region.name}

    while queue:
        region = queue.pop()
        if region.name == target_region:
            return True

        for entrance in region.exits:
            next_region = entrance.connected_region
            if next_region is None or next_region.name in blocked_regions or next_region.name in visited:
                continue
            if entrance.can_reach(state):
                visited.add(next_region.name)
                queue.append(next_region)

    return False


def can_reach_oblivion(state: CollectionState, world) -> bool:
    return (
        any(state.can_reach_region(region, world.player) for region in OBLIVION_REGIONS)
        or (can_reach_region_without(state, world, RegionName.restart, frozenset({RegionName.stranger})) and state.can_reach_region(RegionName.stranger_blade, world.player))
    )

def can_reach_new_world(state: CollectionState, world) -> bool:
    required_count = 5

    @lru_cache(maxsize=None)
    def search(blocked_regions: frozenset[str], group_index: int) -> int:
        best = 0

        for index in range(group_index, len(NEW_WORLD_GROUPS)):
            target_variants, options = NEW_WORLD_GROUPS[index]

            if all(target_region in blocked_regions for target_region in target_variants):
                continue

            for target_region, required_regions in options:
                if target_region in blocked_regions:
                    continue
                if not can_reach_region_without(state, world, target_region, blocked_regions):
                    continue

                next_blocked = blocked_regions.union(target_variants).union(required_regions)
                best = max(best, 1 + search(next_blocked, index + 1))
                if best >= required_count:
                    return best

        return best

    return search(frozenset(), 0) >= required_count


def max_reachable_vessels(state: CollectionState, world) -> int:
    max_count = state.count(ItemName.gift, world.player) if world.options.gift_rando else 5

    if max_count <= 0:
        return 0

    @lru_cache(maxsize=None)
    def search(blocked_regions: frozenset[str], group_index: int) -> int:
        best = 0

        for index in range(group_index, len(HEART_GROUPS)):
            target_variants, options = HEART_GROUPS[index]

            if all(target_region in blocked_regions for target_region in target_variants):
                continue

            for target_region, required_regions in options:
                if target_region in blocked_regions:
                    continue
                if not can_reach_region_without(state, world, target_region, blocked_regions):
                    continue

                next_blocked = blocked_regions.union(target_variants).union(required_regions)
                best = max(best, 1 + search(next_blocked, index + 1))

        return min(best, max_count)

    return search(frozenset(), 0)


def test_goal(state: CollectionState, world) -> bool:
    return state.has(ItemName.credits_reached, world.player)
