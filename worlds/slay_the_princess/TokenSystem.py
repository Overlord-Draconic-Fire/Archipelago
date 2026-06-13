from BaseClasses import ItemClassification, CollectionState
from worlds.AutoWorld import World
from .DataTypes import SlayThePrincessLocationData, SlayThePrincessLocation
from .Items import SlayThePrincessItem
from .Names import LocationName, RegionName, TokenName, ItemName

EVENT_LOCATIONS = {
    TokenName.one: SlayThePrincessLocationData(RegionName.one),
    TokenName.one_blade: SlayThePrincessLocationData(RegionName.one_blade),
    TokenName.adversary: SlayThePrincessLocationData(RegionName.adversary),
    TokenName.adversary_blade: SlayThePrincessLocationData(RegionName.adversary_blade),
    TokenName.tower: SlayThePrincessLocationData(RegionName.tower),
    TokenName.tower_blade: SlayThePrincessLocationData(RegionName.tower_blade),
    TokenName.spectre: SlayThePrincessLocationData(RegionName.spectre),
    TokenName.spectre_blade: SlayThePrincessLocationData(RegionName.spectre_blade),
    TokenName.nightmare: SlayThePrincessLocationData(RegionName.nightmare),
    TokenName.nightmare_blade: SlayThePrincessLocationData(RegionName.nightmare_blade),
    TokenName.razor: SlayThePrincessLocationData(RegionName.razor),
    TokenName.razor_blade: SlayThePrincessLocationData(RegionName.razor_blade),
    TokenName.beast: SlayThePrincessLocationData(RegionName.beast),
    TokenName.beast_blade: SlayThePrincessLocationData(RegionName.beast_blade),
    TokenName.witch: SlayThePrincessLocationData(RegionName.witch),
    TokenName.witch_blade: SlayThePrincessLocationData(RegionName.witch_blade),
    TokenName.prisoner: SlayThePrincessLocationData(RegionName.prisoner),
    TokenName.prisoner_blade: SlayThePrincessLocationData(RegionName.prisoner_blade),
    TokenName.damsel: SlayThePrincessLocationData(RegionName.damsel),
    TokenName.damsel_blade: SlayThePrincessLocationData(RegionName.damsel_blade),

    TokenName.needle: SlayThePrincessLocationData(RegionName.needle),
    TokenName.fury: SlayThePrincessLocationData(RegionName.fury),
    TokenName.apotheosis: SlayThePrincessLocationData(RegionName.apotheosis),
    TokenName.dragon: SlayThePrincessLocationData(RegionName.dragon),
    TokenName.wraith: SlayThePrincessLocationData(RegionName.wraith),
    TokenName.clarity_blade: SlayThePrincessLocationData(RegionName.clarity_blade),
    TokenName.den: SlayThePrincessLocationData(RegionName.den),
    TokenName.wild: SlayThePrincessLocationData(RegionName.wild),
    TokenName.thorn: SlayThePrincessLocationData(RegionName.thorn),
    TokenName.cage: SlayThePrincessLocationData(RegionName.cage),
    TokenName.grey: SlayThePrincessLocationData(RegionName.grey),
    TokenName.happily: SlayThePrincessLocationData(RegionName.happily),
    TokenName.razor_chap4: SlayThePrincessLocationData(RegionName.razor_chap4),

    TokenName.needle_hunted_blade: SlayThePrincessLocationData(RegionName.needle_hunted_blade),
    TokenName.fury_weathered_heart: SlayThePrincessLocationData(RegionName.fury_weathered_heart),
    TokenName.dragon_kind: SlayThePrincessLocationData(RegionName.dragon_kind),
    TokenName.den_blade: SlayThePrincessLocationData(RegionName.den_blade),
    TokenName.wild_blade: SlayThePrincessLocationData(RegionName.wild_blade),
    TokenName.thorn_blade: SlayThePrincessLocationData(RegionName.thorn_blade),
    TokenName.cage_new_world: SlayThePrincessLocationData(RegionName.cage_new_world),
    TokenName.happily_blade: SlayThePrincessLocationData(RegionName.happily_blade),
}

RESET_REGIONS = {
    RegionName.adversary_blade,
    RegionName.tower,
    RegionName.spectre,
    RegionName.nightmare,
    RegionName.beast,
    RegionName.witch,
    RegionName.stranger_blade,
    RegionName.prisoner,
    RegionName.damsel,
    RegionName.needle,
    RegionName.fury,
    RegionName.apotheosis,
    RegionName.dragon,
    RegionName.wraith,
    RegionName.clarity_blade,
    RegionName.den,
    RegionName.wild,
    RegionName.thorn,
    RegionName.cage,
    RegionName.grey,
    RegionName.happily,
    RegionName.razor_chap4,
}

NEW_WORLD_REGIONS = {
    RegionName.stranger_blade,
    RegionName.damsel,
    RegionName.needle_hunted_blade,
    RegionName.fury_weathered_heart,
    RegionName.apotheosis,
    RegionName.dragon_kind,
    RegionName.wraith,
    RegionName.den_blade,
    RegionName.wild_blade,
    RegionName.thorn_blade,
    RegionName.cage_new_world,
    RegionName.grey,
    RegionName.happily_blade,
    RegionName.razor_chap4,
}

OBLIVION_REGIONS = {
    RegionName.adversary,
    RegionName.tower,
    RegionName.spectre,
    RegionName.nightmare,
    RegionName.beast,
    RegionName.witch,
    RegionName.stranger,
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

REGION_TO_TOKEN = {
    RegionName.adversary: {"main": TokenName.adversary, "extra": set()},
    RegionName.adversary_blade: {"main": TokenName.adversary_blade, "extra": set()},
    RegionName.tower: {"main": TokenName.tower, "extra": set()},
    RegionName.spectre: {"main": TokenName.spectre, "extra": set()},
    RegionName.nightmare: {"main": TokenName.nightmare, "extra": set()},
    RegionName.beast: {"main": TokenName.beast, "extra": set()},
    RegionName.witch: {"main": TokenName.witch, "extra": set()},
    RegionName.stranger: {"main": TokenName.stranger, "extra": set()},
    RegionName.stranger_blade: {"main": TokenName.stranger_blade, "extra": set()},
    RegionName.prisoner: {"main": TokenName.prisoner, "extra": set()},
    RegionName.damsel: {"main": TokenName.damsel, "extra": set()},
    RegionName.needle: {"main": TokenName.needle, "extra": set()},
    RegionName.fury: {"main": TokenName.fury, "extra": set()},
    RegionName.apotheosis: {"main": TokenName.apotheosis, "extra": set()},
    RegionName.dragon: {"main": TokenName.dragon, "extra": set()},
    RegionName.wraith: {"main": TokenName.wraith, "extra": set()},
    RegionName.clarity: {"main": TokenName.clarity, "extra": set()},
    RegionName.clarity_blade: {"main": TokenName.clarity_blade, "extra": set()},
    RegionName.den: {"main": TokenName.den, "extra": set()},
    RegionName.wild: {"main": TokenName.wild, "extra": set()},
    RegionName.thorn: {"main": TokenName.thorn, "extra": set()},
    RegionName.cage: {"main": TokenName.cage, "extra": set()},
    RegionName.grey: {"main": TokenName.grey, "extra": set()},
    RegionName.happily: {"main": TokenName.happily, "extra": set()},
    RegionName.razor_chap4: {"main": TokenName.razor_chap4, "extra": set()},

    RegionName.needle_hunted_blade: {"main": TokenName.needle_hunted_blade, "extra": set()},
    RegionName.fury_weathered_heart: {"main": TokenName.fury_weathered_heart, "extra": set()},
    RegionName.dragon_kind: {"main": TokenName.dragon_kind, "extra": set()},
    RegionName.den_blade: {"main": TokenName.den_blade, "extra": set()},
    RegionName.wild_blade: {"main": TokenName.wild_blade, "extra": set()},
    RegionName.thorn_blade: {"main": TokenName.thorn_blade, "extra": set()},
    RegionName.cage_new_world: {"main": TokenName.cage_new_world, "extra": set()},
    RegionName.happily_blade: {"main": TokenName.happily_blade, "extra": set()},
}

REGION_TO_ENTRANCES = {
    RegionName.needle: {
        RegionName.needle_hunted,
        RegionName.needle_skeptic,
    },

    RegionName.fury: {
        RegionName.fury_cold,
        RegionName.fury_contrarian,
        RegionName.fury_broken,
        RegionName.fury_tower,
    },

    RegionName.apotheosis: {
        RegionName.apotheosis_contrarian,
        RegionName.apotheosis_paranoid,
    },

    RegionName.dragon: {
        RegionName.dragon_kind,
        RegionName.dragon_harsh,
    },

    RegionName.wraith: {
        RegionName.wraith_cheated,
        RegionName.wraith_paranoid,
        RegionName.wraith_cold,
        RegionName.wraith_opportunist,
    },

    RegionName.clarity_blade: {
        RegionName.clarity,
    },

    RegionName.den: {
        RegionName.den_skeptic,
        RegionName.den_stubborn,
    },

    RegionName.wild: {
        RegionName.wild_beast_broken,
        RegionName.wild_beast_contrarian,
        RegionName.wild_beast_opportunist,
        RegionName.wild_beast_stubborn,
        RegionName.wild_witch_stubborn,
        RegionName.wild_witch_cheated,
        RegionName.wild_witch_paranoid,
    },

    RegionName.thorn: {
        RegionName.thorn_smitten,
        RegionName.thorn_cheated,
    },

    RegionName.cage: {
        RegionName.cage_paranoid,
        RegionName.cage_cheated,
        RegionName.cage_broken,
    },

    RegionName.grey: {
        RegionName.grey_drowned,
        RegionName.grey_burned,
    },

    RegionName.happily: {
        RegionName.happily_skeptic,
        RegionName.happily_opportunist,
    },

    RegionName.razor_chap4: {
        RegionName.razor_no_way_broken,
        RegionName.razor_no_way_paranoid,
        RegionName.razor_race_broken,
        RegionName.razor_race_paranoid,
        RegionName.razor_race_stubborn,
    },

    RegionName.needle_hunted_blade: {
        RegionName.needle_hunted,
    },

    RegionName.fury_weathered_heart: {
        RegionName.fury_cold,
        RegionName.fury_contrarian,
        RegionName.fury_broken,
        RegionName.fury_tower,
    },

    RegionName.dragon_kind: {
        RegionName.dragon_kind,
    },

    RegionName.den_blade: {
        RegionName.den_skeptic,
        RegionName.den_stubborn,
    },

    RegionName.wild_blade: {
        RegionName.wild_beast_broken,
        RegionName.wild_beast_contrarian,
        RegionName.wild_beast_opportunist,
        RegionName.wild_beast_stubborn,
        RegionName.wild_witch_stubborn,
        RegionName.wild_witch_cheated,
        RegionName.wild_witch_paranoid,
    },

    RegionName.thorn_blade: {
        RegionName.thorn_smitten,
        RegionName.thorn_cheated,
    },

    RegionName.cage_new_world: {
        RegionName.cage_paranoid,
        RegionName.cage_cheated,
        RegionName.cage_broken,
    },

    RegionName.happily_blade: {
        RegionName.happily_skeptic,
        RegionName.happily_opportunist,
    },
}

ENTRANCE = {
    RegionName.adversary: RegionName.adversary,
    RegionName.tower: RegionName.tower,
    RegionName.spectre: RegionName.spectre,
    RegionName.nightmare: RegionName.nightmare,
    RegionName.razor: RegionName.razor,
    RegionName.beast: RegionName.beast,
    RegionName.witch: RegionName.witch,
    RegionName.stranger: RegionName.stranger,
    RegionName.prisoner: RegionName.prisoner,
    RegionName.damsel: RegionName.damsel,

    RegionName.needle_hunted: RegionName.needle_hunted,
    RegionName.needle_skeptic: RegionName.needle_skeptic,

    RegionName.fury_broken: RegionName.fury_broken,
    RegionName.fury_cold: RegionName.fury_cold,
    RegionName.fury_contrarian: RegionName.fury_contrarian,

    RegionName.fury_tower: RegionName.fury_tower,

    RegionName.apotheosis_contrarian: RegionName.apotheosis_contrarian,
    RegionName.apotheosis_paranoid: RegionName.apotheosis_paranoid,

    RegionName.dragon_kind: RegionName.dragon_kind,
    RegionName.dragon_harsh: RegionName.dragon_harsh,

    RegionName.wraith_cheated: RegionName.wraith_cheated,
    RegionName.wraith_paranoid: RegionName.wraith_paranoid,

    RegionName.clarity: RegionName.clarity,

    RegionName.wraith_cold: RegionName.wraith_cold,
    RegionName.wraith_opportunist: RegionName.wraith_opportunist,

    RegionName.razor_no_way_broken: RegionName.razor_no_way_broken,
    RegionName.razor_no_way_paranoid: RegionName.razor_no_way_paranoid,

    RegionName.razor_race_broken: RegionName.razor_race_broken,
    RegionName.razor_race_paranoid: RegionName.razor_race_paranoid,
    RegionName.razor_race_stubborn: RegionName.razor_race_stubborn,

    RegionName.den_skeptic: RegionName.den_skeptic,
    RegionName.den_stubborn: RegionName.den_stubborn,

    RegionName.wild_beast_broken: RegionName.wild_beast_broken,
    RegionName.wild_beast_contrarian: RegionName.wild_beast_contrarian,
    RegionName.wild_beast_opportunist: RegionName.wild_beast_opportunist,
    RegionName.wild_beast_stubborn: RegionName.wild_beast_stubborn,

    RegionName.thorn_smitten: RegionName.thorn_smitten,
    RegionName.thorn_cheated: RegionName.thorn_cheated,

    RegionName.wild_witch_stubborn: RegionName.wild_witch_stubborn,
    RegionName.wild_witch_cheated: RegionName.wild_witch_cheated,
    RegionName.wild_witch_paranoid: RegionName.wild_witch_paranoid,

    RegionName.cage_paranoid: RegionName.cage_paranoid,
    RegionName.cage_cheated: RegionName.cage_cheated,
    RegionName.cage_broken: RegionName.cage_broken,

    RegionName.grey_drowned: RegionName.grey_drowned,

    RegionName.happily_skeptic: RegionName.happily_skeptic,
    RegionName.happily_opportunist: RegionName.happily_opportunist,

    RegionName.grey_burned: RegionName.grey_burned,
}

ENTRANCE_TO_TOKEN = {
    # Adversary
    RegionName.needle_hunted: TokenName.adversary_blade,
    RegionName.needle_skeptic: TokenName.adversary_blade,

    RegionName.fury_broken: TokenName.adversary,
    RegionName.fury_cold: TokenName.adversary,
    RegionName.fury_contrarian: TokenName.adversary,

    # Tower
    RegionName.fury_tower: TokenName.tower_blade,

    RegionName.apotheosis_contrarian: TokenName.tower_blade,
    RegionName.apotheosis_paranoid: TokenName.tower,

    # Spectre
    RegionName.dragon_kind: TokenName.spectre_blade,
    RegionName.dragon_harsh: TokenName.spectre_blade,

    RegionName.wraith_cheated: TokenName.spectre,
    RegionName.wraith_paranoid: TokenName.spectre,

    # Nightmare
    RegionName.clarity: TokenName.nightmare,

    RegionName.wraith_cold: TokenName.nightmare_blade,
    RegionName.wraith_opportunist: TokenName.nightmare_blade,

    # Razor
    RegionName.razor_no_way_broken: TokenName.razor,
    RegionName.razor_no_way_paranoid: TokenName.razor,

    RegionName.razor_race_broken: TokenName.razor_blade,
    RegionName.razor_race_paranoid: TokenName.razor_blade,
    RegionName.razor_race_stubborn: TokenName.razor_blade,

    # Beast
    RegionName.den_skeptic: TokenName.beast,
    RegionName.den_stubborn: TokenName.beast_blade,

    RegionName.wild_beast_broken: TokenName.beast,
    RegionName.wild_beast_contrarian: TokenName.beast,
    RegionName.wild_beast_opportunist: TokenName.beast_blade,
    RegionName.wild_beast_stubborn: TokenName.beast_blade,

    # Witch
    RegionName.thorn_smitten: TokenName.witch_blade,
    RegionName.thorn_cheated: TokenName.witch_blade,

    RegionName.wild_witch_stubborn: TokenName.witch_blade,
    RegionName.wild_witch_cheated: TokenName.witch_blade,
    RegionName.wild_witch_paranoid: TokenName.witch,

    # Prisoner
    RegionName.cage_paranoid: TokenName.prisoner_blade,
    RegionName.cage_cheated: TokenName.prisoner,
    RegionName.cage_broken: TokenName.prisoner,

    RegionName.grey_drowned: TokenName.prisoner_blade,

    # Damsel
    RegionName.happily_skeptic: TokenName.damsel,
    RegionName.happily_opportunist: TokenName.damsel,

    RegionName.grey_burned: TokenName.damsel_blade,
}


def rando_entrance(world: World) -> None:
    #Pas encore de rando entrance pour le moment...
    pass


def fill_region_tokens():
    for region, entrances in REGION_TO_ENTRANCES.items():
        data = REGION_TO_TOKEN.get(region)
        if data is None:
            continue

        for sub_entrance in entrances:
            # entrée randomisée
            new_entrance = ENTRANCE.get(sub_entrance)
            if new_entrance is None:
                continue

            # token associé
            token = ENTRANCE_TO_TOKEN.get(new_entrance)
            if token is None:
                continue

            data["extra"].add(token)


def create_token(world: World) -> None:
    for token_name, location_data in EVENT_LOCATIONS.items():
        world.multiworld.get_region(location_data.region, world.player).add_locations(
            {token_name: None}, SlayThePrincessLocation
        )

        world.multiworld.get_location(token_name, world.player).place_locked_item(
            SlayThePrincessItem(token_name, ItemClassification.progression, None, world.player)
        )


BLADE_ONLY_SUFFIX = " [Blade Only]"


def _token_group(token: str) -> str:
    region = EVENT_LOCATIONS[token].region
    if region.endswith(BLADE_ONLY_SUFFIX):
        return region[:-len(BLADE_ONLY_SUFFIX)]
    return region


def max_reset(state: CollectionState, world, regions: set[str], want: int) -> bool:
    from .Regions import region_data_table, Chapter

    max_count = state.count(ItemName.gift, world.player) if world.options.gift_rando else 5
    if max_count < want and regions != OBLIVION_REGIONS:
        return False

    owned_tokens = {token for token in EVENT_LOCATIONS if state.has(token, world.player)}

    chap2_regions = {r for r in regions if region_data_table[r].chapter == Chapter.two}
    chap3_regions = {r for r in regions if region_data_table[r].chapter == Chapter.three}

    usable_chap2 = {_token_group(REGION_TO_TOKEN[r]["main"]) for r in chap2_regions if REGION_TO_TOKEN[r]["main"] in owned_tokens}

    if len(usable_chap2) >= want:
        return True

    usable_chap3 = 0
    used_tokens = set(usable_chap2)
    candidates = []
    for r in chap3_regions:
        main = REGION_TO_TOKEN[r]["main"]
        if main in owned_tokens:
            available_extras = {e for e in REGION_TO_TOKEN[r]["extra"] if e in owned_tokens and _token_group(e) not in used_tokens}
            if available_extras:
                candidates.append((r, available_extras))
    candidates.sort(key=lambda x: len(x[1]))
    for r, extras in candidates:
        main = REGION_TO_TOKEN[r]["main"]
        if main not in used_tokens:
            available_extras = {e for e in extras if e not in used_tokens}
            if available_extras:
                to_consume_extra = next(iter(available_extras))
                used_tokens.add(main)
                used_tokens.add(to_consume_extra)
                usable_chap3 += 1
                if len(usable_chap2) + usable_chap3 >= want:
                    return True

    return False


def max_reachable_vessels(state: CollectionState, world, want: int) -> bool:
    return max_reset(state, world, RESET_REGIONS, want)


def can_reach_new_world(state: CollectionState, world) -> bool:
    return max_reset(state, world, NEW_WORLD_REGIONS, 5)


def can_reach_oblivion(state: CollectionState, world) -> bool:
    return max_reset(state, world, OBLIVION_REGIONS, 6)
