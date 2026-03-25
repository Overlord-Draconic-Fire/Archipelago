from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .Names import ItemName


offset: int = 63900000
princess: int = 100
voice: int = 200
dagger: int = 300
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

dagger_item_data_table: Dict[str, SlayThePrincessItemData] = {
    ItemName.dagger: SlayThePrincessItemData(offset + dagger + 0, ItemClassification.progression),
    ItemName.dagger1: SlayThePrincessItemData(offset + dagger + 1, ItemClassification.progression),
    ItemName.dagger2: SlayThePrincessItemData(offset + dagger + 2, ItemClassification.progression),
    ItemName.dagger3: SlayThePrincessItemData(offset + dagger + 3, ItemClassification.progression),
    ItemName.dagger_princess: SlayThePrincessItemData(offset + dagger + 4, ItemClassification.progression),
    ItemName.dagger_adversary: SlayThePrincessItemData(offset + dagger + 5, ItemClassification.progression),
    ItemName.dagger_tower: SlayThePrincessItemData(offset + dagger + 6, ItemClassification.progression),
    ItemName.dagger_spectre: SlayThePrincessItemData(offset + dagger + 7, ItemClassification.progression),
    ItemName.dagger_nightmare: SlayThePrincessItemData(offset + dagger + 8, ItemClassification.progression),
    ItemName.dagger_razor: SlayThePrincessItemData(offset + dagger + 9, ItemClassification.progression),
    ItemName.dagger_beast: SlayThePrincessItemData(offset + dagger + 10, ItemClassification.progression),
    ItemName.dagger_witch: SlayThePrincessItemData(offset + dagger + 11, ItemClassification.progression),
    ItemName.dagger_stranger: SlayThePrincessItemData(offset + dagger + 12, ItemClassification.progression),
    ItemName.dagger_prisoner: SlayThePrincessItemData(offset + dagger + 13, ItemClassification.progression),
    ItemName.dagger_damsel: SlayThePrincessItemData(offset + dagger + 14, ItemClassification.progression),
    ItemName.dagger_needle: SlayThePrincessItemData(offset + dagger + 15, ItemClassification.progression),
    ItemName.dagger_fury: SlayThePrincessItemData(offset + dagger + 16, ItemClassification.progression),
    ItemName.dagger_apotheosis: SlayThePrincessItemData(offset + dagger + 17, ItemClassification.progression),
    ItemName.dagger_dragon: SlayThePrincessItemData(offset + dagger + 18, ItemClassification.progression),
    ItemName.dagger_den: SlayThePrincessItemData(offset + dagger + 19, ItemClassification.progression),
    ItemName.dagger_wild: SlayThePrincessItemData(offset + dagger + 20, ItemClassification.progression),
    ItemName.dagger_thorn: SlayThePrincessItemData(offset + dagger + 21, ItemClassification.progression),
    ItemName.dagger_cage: SlayThePrincessItemData(offset + dagger + 22, ItemClassification.progression),
    ItemName.dagger_grey: SlayThePrincessItemData(offset + dagger + 23, ItemClassification.progression),
    ItemName.dagger_happily: SlayThePrincessItemData(offset + dagger + 24, ItemClassification.progression),
    ItemName.dagger_goddess: SlayThePrincessItemData(offset + dagger + 25, ItemClassification.progression),
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
                                                       **dagger_item_data_table,
                                                       **princess_item_data_table,
                                                       **voice_item_data_table}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
