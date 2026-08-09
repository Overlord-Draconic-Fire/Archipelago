from dataclasses import dataclass
import random

from Options import Choice, Toggle, OptionGroup, PerGameCommonOptions, DefaultOnToggle
from worlds.AutoWorld import World

class DeathLink(Choice):
    """
    Determines how DeathLink behaves.
    - Nothing: DeathLink is disabled.
    - Only Receive: You can receive DeathLinks from other players, but your deaths are never sent.
    - On Archipelago Death: Sends a DeathLink when you become stuck because you are missing required progression items.
    - On Real Death: Sends a DeathLink whenever the protagonist dies during the story.
    - Both: Combines Archipelago Death and Real Death behaviors.
    """
    display_name = "Death Link"
    option_nothing = 0
    option_only_receive = 1
    option_on_archipelago_death = 2
    option_on_real_death = 3
    option_both = 4
    default = 0


class ChapterAccessRando(Choice):
    """
    Determines which items are required to access chapters and shuffles them into the item pool.
    - Nothing: No items added, you can enter a chapter just like in the base game.
    - Princess: You will only need the princess item to enter a chapter (+23 items)
    - Voices: You will need the princess and voice items to access a chapter. (+10 items)
    - Both: Chapter access items are completely randomized (+33 items)
    """
    display_name = "Chapter Access Rando"
    option_nothing = 0
    option_princess = 1
    option_voices = 2
    option_both = 3
    default = 3


class PristineBladeRando(Choice):
    """
    Controls how many Pristine Blades are available and shuffles them into the item pool.
    - Nothing: Pristine Blade is not randomized
    - One Blade: Only one Pristine Blade is available for the entire game (+1 items)
    - Chapter Blade: One Pristine Blade per chapter [The fourth one is for the goddess] (+4 items)
    - Princess Blade: One Pristine Blade per princess (+23 items)
    """
    display_name = "Pristine Blade Rando"
    option_nothing = 0
    option_one_blade = 1
    option_chapter_blade = 2
    option_princess_blade = 3
    default = 3


class PristineSwordRando(DefaultOnToggle):
    """
    Shuffles the pristine sword in the apotheosis chapter into the item pool. (+1 items)
    """
    display_name = "Pristine Sword Rando"


class GiftRando(DefaultOnToggle):
    """
    Shuffles gifts into the item pool as progression items required to complete loops. (+5 items)
    """
    display_name = "Gift Rando"


class NarratorRando(DefaultOnToggle):
    """
    Shuffles the narrator into the item pool as an item required to talk with him in the mirror in the space between. (+1 items)
    """
    display_name = "Narrator Rando"


class ChapterRando(Choice):
    """
    Chooses to randomize entering a chapter in the world.
    - Nothing: Entering a chapter is not random.
    - Chapter: Entering a chapter for the first time is a check locations in the world. (+23 locations)
    - Global: Entering a global chapter (2 and 3) for the first time is a check locations in the world. (+2 locations)
    - Both: Entering chapter and global chapter are check locations in the world. (+25 locations)
    """
    display_name = "Chapter Rando"
    option_nothing = 0
    option_chapter = 1
    option_global = 2
    option_both = 3
    default = 3


class HeartRando(Choice):
    """
    Chooses to randomize hearts in the world.
    - Nothing: Hearts are not random.
    - Heart: Hearts are check locations in the world. (+29 locations)
    - Vessel: For example, for Damsel: "A Gentle Heart" and "A Pliable Heart" are combined into a single location
              Chapter affected: Razor, Prisoner, Damsel, Fury, Dragon, Wild, Grey. (+22 locations)
    """
    display_name = "Heart Rando"
    option_nothing = 0
    option_heart = 1
    option_vessel = 2
    default = 1


class MirrorRando(DefaultOnToggle):
    """
    Add facing the mirror in the end of the 5 loops as check locations in the world. (+5 locations)
    """
    display_name = "Mirror Rando"


class OblivionRando(DefaultOnToggle):
    """
    Add all oblivion step as check locations in the world. (+6 location)
    """
    display_name = "Oblivion Rando"


class MemorieSanity(Choice):
    """
    Chooses to randomize the memories in the world. (+439 locations/items)
    - Nothing: Memories are not randomized
    - Location: Memories are added as check locations, but the items are not shuffled.
    - Both: Memories are both items and locations
    """
    display_name = "Memories Sanity"
    option_nothing = 0
    option_location = 1
    option_both = 2
    default = 2


@dataclass
class SlayThePrincessOptions(PerGameCommonOptions):
    #Game Options
    #goal: Goal
    death_link: DeathLink
    #entrance_rando: EntranceRando

    #Item
    chapter_access: ChapterAccessRando
    pristine_blade_rando: PristineBladeRando
    pristine_sword_rando: PristineSwordRando
    #force_chapter1_blade: ForceChapter1BladeRando
    gift_rando: GiftRando
    narrator_rando: NarratorRando
    #saves_rando: SavesRando

    #Location
    chapter_rando: ChapterRando
    heart_rando: HeartRando
    mirror_rando: MirrorRando
    oblivion_rando: OblivionRando
    memoriesanity: MemorieSanity

slay_the_princess_option_groups = [
    OptionGroup("Item Options", [
        ChapterAccessRando,
        PristineBladeRando,
        PristineSwordRando,
        #ForceChapter1BladeRando,
        GiftRando,
        NarratorRando,
        #SavesRando,
    ]),
    OptionGroup("Location Options", [
        ChapterRando,
        HeartRando,
        MirrorRando,
        OblivionRando,
        MemorieSanity,
    ]),
]