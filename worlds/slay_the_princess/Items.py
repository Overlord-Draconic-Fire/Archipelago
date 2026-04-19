from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .Names import ItemName


offset: int = 63900000
princess: int = 100
voice: int = 200
blade: int = 300
other: int = 400
memories: int = 10000


class SlayThePrincessItem(Item):
    game = "Slay The Princess"


class SlayThePrincessItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler


other_item_data_table: Dict[str, SlayThePrincessItemData] = {
    ItemName.filler: SlayThePrincessItemData(offset + 0, ItemClassification.filler),
    ItemName.mirror: SlayThePrincessItemData(offset + other + 1, ItemClassification.progression),
    ItemName.gift: SlayThePrincessItemData(offset + other + 2, ItemClassification.progression),
}

blade_item_data_table: Dict[str, SlayThePrincessItemData] = {
    ItemName.blade: SlayThePrincessItemData(offset + blade + 0, ItemClassification.progression),
}

blade_chapter_item_data_table: Dict[str, SlayThePrincessItemData] = {
    ItemName.blade1: SlayThePrincessItemData(offset + blade + 1, ItemClassification.progression),
    ItemName.blade2: SlayThePrincessItemData(offset + blade + 2, ItemClassification.progression),
    ItemName.blade3: SlayThePrincessItemData(offset + blade + 3, ItemClassification.progression),
    ItemName.blade4: SlayThePrincessItemData(offset + blade + 4, ItemClassification.progression),
}

blade_princess_item_data_table: Dict[str, SlayThePrincessItemData] = {
    ItemName.blade_princess: SlayThePrincessItemData(offset + blade + 5, ItemClassification.progression),
    ItemName.blade_adversary: SlayThePrincessItemData(offset + blade + 6, ItemClassification.progression),
    ItemName.blade_tower: SlayThePrincessItemData(offset + blade + 7, ItemClassification.progression),
    ItemName.blade_spectre: SlayThePrincessItemData(offset + blade + 8, ItemClassification.progression),
    ItemName.blade_nightmare: SlayThePrincessItemData(offset + blade + 9, ItemClassification.progression),
    ItemName.blade_razor: SlayThePrincessItemData(offset + blade + 10, ItemClassification.progression),
    ItemName.blade_beast: SlayThePrincessItemData(offset + blade + 11, ItemClassification.progression),
    ItemName.blade_witch: SlayThePrincessItemData(offset + blade + 12, ItemClassification.progression),
    ItemName.blade_stranger: SlayThePrincessItemData(offset + blade + 13, ItemClassification.progression),
    ItemName.blade_prisoner: SlayThePrincessItemData(offset + blade + 14, ItemClassification.progression),
    ItemName.blade_damsel: SlayThePrincessItemData(offset + blade + 15, ItemClassification.progression),
    ItemName.blade_needle: SlayThePrincessItemData(offset + blade + 16, ItemClassification.progression),
    ItemName.blade_fury: SlayThePrincessItemData(offset + blade + 17, ItemClassification.progression),
    ItemName.blade_apotheosis: SlayThePrincessItemData(offset + blade + 18, ItemClassification.progression),
    ItemName.blade_dragon: SlayThePrincessItemData(offset + blade + 19, ItemClassification.progression),
    ItemName.blade_den: SlayThePrincessItemData(offset + blade + 20, ItemClassification.progression),
    ItemName.blade_clarity: SlayThePrincessItemData(offset + blade + 21, ItemClassification.progression),
    ItemName.blade_wild: SlayThePrincessItemData(offset + blade + 22, ItemClassification.progression),
    ItemName.blade_thorn: SlayThePrincessItemData(offset + blade + 23, ItemClassification.progression),
    ItemName.blade_cage: SlayThePrincessItemData(offset + blade + 24, ItemClassification.progression),
    ItemName.blade_grey: SlayThePrincessItemData(offset + blade + 25, ItemClassification.progression),
    ItemName.blade_happily: SlayThePrincessItemData(offset + blade + 26, ItemClassification.progression),
    ItemName.blade_goddess: SlayThePrincessItemData(offset + blade + 27, ItemClassification.progression),
}

princess_item_data_table: Dict[str, SlayThePrincessItemData] = {
    ItemName.adversary: SlayThePrincessItemData(offset + princess + 0, ItemClassification.progression),
    ItemName.tower: SlayThePrincessItemData(offset + princess + 1, ItemClassification.progression),
    ItemName.spectre: SlayThePrincessItemData(offset + princess + 2, ItemClassification.progression),
    ItemName.nightmare: SlayThePrincessItemData(offset + princess + 3, ItemClassification.progression),
    ItemName.razor: SlayThePrincessItemData(offset + princess + 4, ItemClassification.progression),
    ItemName.beast: SlayThePrincessItemData(offset + princess + 5, ItemClassification.progression),
    ItemName.witch: SlayThePrincessItemData(offset + princess + 6, ItemClassification.progression),
    ItemName.stranger: SlayThePrincessItemData(offset + princess + 7, ItemClassification.progression),
    ItemName.prisoner: SlayThePrincessItemData(offset + princess + 8, ItemClassification.progression),
    ItemName.damsel: SlayThePrincessItemData(offset + princess + 9, ItemClassification.progression),

    ItemName.needle: SlayThePrincessItemData(offset + princess + 10, ItemClassification.progression),
    ItemName.fury: SlayThePrincessItemData(offset + princess + 11, ItemClassification.progression),
    ItemName.apotheosis: SlayThePrincessItemData(offset + princess + 12, ItemClassification.progression),
    ItemName.dragon: SlayThePrincessItemData(offset + princess + 13, ItemClassification.progression),
    ItemName.wraith: SlayThePrincessItemData(offset + princess + 14, ItemClassification.progression),
    ItemName.clarity: SlayThePrincessItemData(offset + princess + 15, ItemClassification.progression),
    ItemName.den: SlayThePrincessItemData(offset + princess + 16, ItemClassification.progression),
    ItemName.wild: SlayThePrincessItemData(offset + princess + 17, ItemClassification.progression),
    ItemName.thorn: SlayThePrincessItemData(offset + princess + 18, ItemClassification.progression),
    ItemName.cage: SlayThePrincessItemData(offset + princess + 19, ItemClassification.progression),
    ItemName.grey: SlayThePrincessItemData(offset + princess + 20, ItemClassification.progression),
    ItemName.happily: SlayThePrincessItemData(offset + princess + 21, ItemClassification.progression),

    ItemName.goddess: SlayThePrincessItemData(offset + princess + 22, ItemClassification.progression)
}

voice_item_data_table: Dict[str, SlayThePrincessItemData] = {
    ItemName.broken: SlayThePrincessItemData(offset + voice + 0, ItemClassification.progression),
    ItemName.cheated: SlayThePrincessItemData(offset + voice + 1, ItemClassification.progression),
    ItemName.cold: SlayThePrincessItemData(offset + voice + 2, ItemClassification.progression),
    ItemName.contrarian: SlayThePrincessItemData(offset + voice + 3, ItemClassification.progression),
    ItemName.hunted: SlayThePrincessItemData(offset + voice + 4, ItemClassification.progression),
    ItemName.opportunist: SlayThePrincessItemData(offset + voice + 5, ItemClassification.progression),
    ItemName.paranoid: SlayThePrincessItemData(offset + voice + 6, ItemClassification.progression),
    ItemName.skeptic: SlayThePrincessItemData(offset + voice + 7, ItemClassification.progression),
    ItemName.smitten: SlayThePrincessItemData(offset + voice + 8, ItemClassification.progression),
    ItemName.stubborn: SlayThePrincessItemData(offset + voice + 9, ItemClassification.progression),
}

item_data_table: Dict[str, SlayThePrincessItemData] = {**other_item_data_table,
                                                       **blade_item_data_table,
                                                       **blade_chapter_item_data_table,
                                                       **blade_princess_item_data_table,
                                                       **princess_item_data_table,
                                                       **voice_item_data_table}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
