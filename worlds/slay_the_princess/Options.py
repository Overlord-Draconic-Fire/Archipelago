from dataclasses import dataclass
import random

from Options import Choice, Toggle, OptionGroup, PerGameCommonOptions, DefaultOnToggle
from worlds.AutoWorld import World

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
    default = 1


class GiftRando(DefaultOnToggle):
    """
    Shuffles gifts into the item pool as progression items required to complete loops. (+5 items)
    """
    display_name = "Gift Rando"


class ChapterRando(DefaultOnToggle):
    """
    Add entering a chapter for the first time as check locations in the world. (+23 locations)
    """
    display_name = "Chapter Rando"


class GlobalChapterRando(DefaultOnToggle):
    """
    Add entering a global chapter (2 and 3) as check locations in the world. (+2 locations)
    """
    display_name = "Global Chapter Rando"


class HearthRando(DefaultOnToggle):
    """
    Add hearths (vessels) as check locations in the world. (+29 locations)
    """
    display_name = "Hearth Rando"


class MirrorRando(DefaultOnToggle):
    """
    Add facing the mirror in the end of the 5 loops as check locations in the world. (+5 locations)
    """
    display_name = "Mirror Rando"


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
    default = 0


@dataclass
class SlayThePrincessOptions(PerGameCommonOptions):
    #Game Options
    #goal: Goal
    #entrance_rando: EntranceRando

    #Item
    chapter_access: ChapterAccessRando
    #couple_princesses_and_voices: CouplePrincessesAndVoices
    #all_voices_chapter: AllVoicesChapter
    pristine_blade_rando: PristineBladeRando
    #force_chapter1_blade: ForceChapter1BladeRando
    gift_rando: GiftRando
    #narrator_rando: NarratorRando
    #good_oblivion_ending: GoodOblivionEnding
    #saves_rando: SavesRando

    #Location
    chapter_rando: ChapterRando
    global_chapter_rando: GlobalChapterRando
    heart_rando: HearthRando
    #heart_grouping: HeartGrouping
    mirror_rando: MirrorRando
    memoriesanity: MemorieSanity
    #branchsanity: BranchSanity

slay_the_princess_option_groups = [
    #OptionGroup("Game Options", [
        #Goal,
        #EntranceRando,
    #]),
    OptionGroup("Item Options", [
        ChapterAccessRando,
        #CouplePrincessesAndVoices
        #AllVoicesChapter
        PristineBladeRando,
        #ForceChapter1BladeRando,
        GiftRando,
        #NarratorRando,
        #GoodOblivionEnding,
        #SavesRando,
    ]),
    OptionGroup("Location Options", [
        ChapterRando,
        GlobalChapterRando,
        HearthRando,
        #HeartGrouping,
        MirrorRando,
        MemorieSanity,
        #BranchSanity,
    ]),
]