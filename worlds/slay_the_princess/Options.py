from dataclasses import dataclass
import random

from Options import Choice, Toggle, OptionGroup, PerGameCommonOptions, DefaultOnToggle, Range
from worlds.AutoWorld import World

class Goal(Choice):
    """
    Chooses which of the three possible endings to pursue:
    - Our Song: Complete the game's classic ending after collecting five vessels.
    - Your New World: Collect five vessels through violent or hostile outcomes and destroy her without outside help.
    - Oblivion: Reject the Princess and refuse to enter the cabin, ultimately choosing oblivion.
    """
    display_name = "Goal"
    option_our_song = 0
    option_your_new_world = 1
    option_oblivion = 2
    default = 0


class MemoriesHunt(Range):
    """
    Determines how many gallery images must be collected before the game can be completed.
    - 0: No memories are required, just complete the goal.
    - 1-439: The specified number of memories must be collected before completion.
    """
    display_name = "Memories Hunt"
    range_start = 0
    range_end = 439
    default = 0


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
    - Voices: You will only need the voice items to access a chapter (+10 items)
    - Both: You will need the princess and voice items to access a chapter (+33 items)
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


class NarratorRando(DefaultOnToggle):
    """
    Shuffles the narrator into the item pool as an item required to talk with him in the mirror in the space between. (+1 items)
    """
    display_name = "Narrator Rando"


class SaveSlotRando(Range): #RandomCharmCosts for exemple
    """
    Shuffles save slots into the item pool, indicating the number of possible saves
    It's just a slot, you can save multiple times to the same slot if you want

    Set to -1 so it's not randomized (you will have 5 pages of 6 slots (30 in total) available)
    Set to -2 so that all filler items become save slot items (= number of locations - number of items) [max 30]
    """
    display_name = "Save Slot Rando"
    range_start = -2
    range_end = 30
    default = -2


class GiftRando(Choice):
    """
    Chooses to randomize gifts in the world. (+5 locations/items)
    - Nothing: Gifts are not randomized
    - Item: Invitations are added as progression items required to complete loops
    - Location: Gifts are added as check locations. When you encounter the Shifting Mound for the Xth time during the same save
    - Both: Invitations and Gifts are both items and locations
    """
    display_name = "Gift Rando"
    option_nothing = 0
    option_item = 1
    option_location = 2
    option_both = 3
    default = 3


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


class VoiceRando(DefaultOnToggle):
    """
    Add the fact that a voice speaks for the first time as check locations in the world. (+10 locations)
    """
    display_name = "Voice Rando"


class LocationBladeRando(DefaultOnToggle):
    """
    Add the fact of taking a blade in a chapter as check locations in the world. (+22 locations)
    """
    display_name = "Location Blade Rando"


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


class MirrorRando(Choice):
    """
    Chooses to randomize facing a mirror in the world.
    - Nothing: Mirror are not random.
    - Space Between: Add facing the mirror in the end of the 5 loops as check locations in the world. (+5 locations)
    - Chapter: Add facing a mirror in a chapter as check locations in the world. (+19 locations)
    - Both: Facing the mirror in the space between and in a chapter are check locations in the world. (+24 locations)
    """
    display_name = "Mirror Rando"
    option_nothing = 0
    option_space_between = 1
    option_chapter = 2
    option_both = 3
    default = 3


class OblivionRando(DefaultOnToggle):
    """
    Add all oblivion steps as check locations in the world. (+6 location)
    """
    display_name = "Oblivion Rando"


@dataclass
class SlayThePrincessOptions(PerGameCommonOptions):
    #Game Options
    goal: Goal
    memories_hunt: MemoriesHunt
    death_link: DeathLink
    #entrance_rando: EntranceRando

    #Item
    chapter_access: ChapterAccessRando
    pristine_blade_rando: PristineBladeRando
    pristine_sword_rando: PristineSwordRando
    narrator_rando: NarratorRando
    save_slot_rando: SaveSlotRando

    #Both
    gift_rando: GiftRando
    memoriesanity: MemorieSanity

    #Location
    chapter_rando: ChapterRando
    voice_rando: VoiceRando
    location_blade_rando: LocationBladeRando
    heart_rando: HeartRando
    mirror_rando: MirrorRando
    oblivion_rando: OblivionRando

slay_the_princess_option_groups = [
    OptionGroup("Item Options", [
        ChapterAccessRando,
        PristineBladeRando,
        PristineSwordRando,
        NarratorRando,
        SaveSlotRando,
    ]),
    OptionGroup("Items/Location Options", [
        GiftRando,
        MemorieSanity,
    ]),
    OptionGroup("Location Options", [
        ChapterRando,
        VoiceRando,
        LocationBladeRando,
        HeartRando,
        MirrorRando,
        OblivionRando,
    ]),
]