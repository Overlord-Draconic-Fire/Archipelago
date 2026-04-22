from typing import List

from BaseClasses import Region, CollectionState, ItemClassification
from worlds.AutoWorld import World, WebWorld
from .Items import SlayThePrincessItem, item_table, princess_item_data_table, item_data_table, voice_item_data_table, \
    blade_princess_item_data_table, blade_chapter_item_data_table, gallery_item_data_table
from .Locations import SlayThePrincessLocation, location_table, others_location_data_table, princess_location_data_table, \
    global_chapter_location_data_table, heart_location_data_table, mirror_location_data_table, location_data_table, gallery_location_data_table
from .Names import ItemName, LocationName, RegionName
from .Options import SlayThePrincessOptions, slay_the_princess_option_groups
from .Regions import region_data_table, SlayThePrincessRegionData, set_region_rules
from .Rules import has_blade


class SlayThePrincessWeb(WebWorld):
    option_groups = slay_the_princess_option_groups


class SlayThePrincessWorld(World):
    """You're on a path in the woods. On the end of that path is a cabin.
    And in the basement of that cabin is a Princess. You're here to Slay the Princess.
    If you don't, it will be the end of the world."""

    # Class Data
    game = "Slay The Princess"
    web = SlayThePrincessWeb()
    options_dataclass = SlayThePrincessOptions
    options: SlayThePrincessOptions
    location_name_to_id = location_table
    item_name_to_id = item_table
    optional_location_tables = {
        "chapter_rando": princess_location_data_table,
        "global_chapter_rando": global_chapter_location_data_table,
        "heart_rando": heart_location_data_table,
        "mirror_rando": mirror_location_data_table,
        "memoriesanity": gallery_location_data_table,
    }

    def create_regions(self) -> None:
        # Create regions
        regions: dict[str, Region] = {}
        for region_name, region_data in region_data_table.items():
            region = Region(region_name, self.player, self.multiworld)
            regions[region_name] = region
            self.multiworld.regions.append(region)

            if region_data_table[region_name].have_entry:
                region_entry_name = region_name + " ENTRY"
                region_entry = Region(region_entry_name, self.player, self.multiworld)
                regions[region_entry_name] = region_entry
                self.multiworld.regions.append(region_entry)

        # Create entrance
        set_region_rules(self, regions)

        # Build active locations table from always-on + option-gated tables.
        active_location_data_table = dict(others_location_data_table)
        for option_name, data_table in self.optional_location_tables.items():
            if getattr(self.options, option_name):
                active_location_data_table.update(data_table)

        # Create locations.
        for region_name, region_data in regions.items():
            region = self.multiworld.get_region(region_name, self.player)

            region.add_locations({
                location_name: location_data.address for location_name, location_data in active_location_data_table.items()
                if location_data.region == region_name
            }, SlayThePrincessLocation)

        self.create_goal_region()

    def create_goal_region(self) -> None:
        # Credit (autre que good et oblivion)

        # region.add_locations for LocationName.win !!!

        victory_location = self.multiworld.get_location(LocationName.win, self.player)
        victory_location.place_locked_item(SlayThePrincessItem(ItemName.credits_reached, ItemClassification.progression, None, self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemName.credits_reached, self.player)

    def create_item(self, name: str) -> SlayThePrincessItem:
        return SlayThePrincessItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[SlayThePrincessItem] = []

        if self.options.chapter_access in [1, 3]:
            item_pool += [self.create_item(name) for name in princess_item_data_table.keys()]
        if self.options.chapter_access in [2, 3]:
            item_pool += [self.create_item(name) for name in voice_item_data_table.keys()]

        if self.options.pristine_blade_rando == 1:
            item_pool += [self.create_item(ItemName.blade)]
        if self.options.pristine_blade_rando == 2:
            item_pool += [self.create_item(name) for name in blade_chapter_item_data_table.keys()]
        if self.options.pristine_blade_rando == 3:
            item_pool += [self.create_item(name) for name in blade_princess_item_data_table.keys()]

        if self.options.gift_rando:
            item_pool += [self.create_item(ItemName.gift) for _ in range(5)]

        if self.options.memoriesanity == 2:
            item_pool += [self.create_item(name) for name in gallery_item_data_table.keys()]

        item_pool += [self.create_item(ItemName.filler) for _ in range(len(list(self.get_locations())) - len(item_pool) - 1)]
        self.multiworld.itempool += item_pool

    def set_rules(self) -> None:
        for location_name, location_data in location_data_table.items():
            if location_data.rule is None:
                continue

            location = self.multiworld.get_location(location_name, self.player)
            location.access_rule = (lambda state, rule=location_data.rule: rule(state, self))

    def connect_entrances(self) -> None:
        pass

    def fill_slot_data(self):
        return {
            "chapter_access": self.options.chapter_access.value,
            "pristine_blade_rando": self.options.pristine_blade_rando.value,
            "gift_rando": self.options.gift_rando.value,
            "chapter_rando": self.options.chapter_rando.value,
            "global_chapter_rando": self.options.global_chapter_rando.value,
            "heart_rando": self.options.heart_rando.value,
            "mirror_rando": self.options.mirror_rando.value,
            "memoriesanity": self.options.memoriesanity.value,
        }