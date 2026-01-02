from typing import List

from BaseClasses import Region, CollectionState, ItemClassification
from worlds.AutoWorld import World
from .Items import SlayThePrincessItem, item_table, princess_item_data_table, item_data_table, voice_item_data_table
from .Locations import SlayThePrincessLocation, location_data_table, location_table
from .Names import ItemName, LocationName, RegionName
from .Options import SlayThePrincessOptions, slay_the_princess_option_groups, resolve_options
from .Regions import region_data_table, SlayThePrincessRegionData, set_region_rules
from .Rules import has_dagger_for


class SlayThePrincessWorld(World):
    """You're on a path in the woods. On the end of that path is a cabin.
    And in the basement of that cabin is a Princess. You're here to Slay the Princess.
    If you don't, it will be the end of the world."""

    # Class Data
    game = "Slay The Princess"
    #options_dataclass = Celeste64Options
    #options: Celeste64Options
    location_name_to_id = location_table
    item_name_to_id = item_table

    """def generate_early(self) -> None:
        resolve_options(self)"""

    def create_regions(self) -> None:
        """
        sanity_tables = (
            (self.options.friendsanity, friend_location_data_table),
            (self.options.signsanity, sign_location_data_table),
            (self.options.carsanity, car_location_data_table),
        )

        for enabled, data_table in sanity_tables:
            if not enabled:
                continue

            region.add_locations({
                location_name: location_data.address for location_name, location_data in data_table.items()
                if data.region == region_name
            }, SlayThePrincessLocation)
        """

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

        # Create locations.
        for region_name, region_data in regions.items():
            region = self.multiworld.get_region(region_name, self.player)

            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name
            }, SlayThePrincessLocation)

        self.create_goal_region()

    def create_goal_region(self) -> None:
        # Credit (autre que good et oblivion)
        victory_location = self.multiworld.get_location(LocationName.win, self.player)
        victory_location.place_locked_item(SlayThePrincessItem(ItemName.credits_reached, ItemClassification.progression, None, self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemName.credits_reached, self.player)

    def create_item(self, name: str) -> SlayThePrincessItem:
        return SlayThePrincessItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[SlayThePrincessItem] = []
        item_pool += [self.create_item(name) for name in princess_item_data_table.keys()]
        item_pool += [self.create_item(name) for name in voice_item_data_table.keys()]
        item_pool += [self.create_item(ItemName.dagger)]
        item_pool += [self.create_item(ItemName.gift) for _ in range(5)]

        item_pool += [self.create_item(ItemName.filler) for _ in range(len(list(self.get_locations())) - len(item_pool) - 1)]
        self.multiworld.itempool += item_pool

    def set_rules(self) -> None:
        pass

    def connect_entrances(self) -> None:
        pass
