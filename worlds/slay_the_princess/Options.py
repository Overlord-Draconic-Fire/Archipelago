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
    nothing = 1
    princess = 2
    voices = 3
    both = 4
    default = 4


class PristineDaggerRando(Choice):
    """
    Controls how many Pristine Daggers are available and shuffles them into the item pool.
    - Nothing: Pristine Dagger is not randomized
    - One Dagger: Only one Pristine Dagger is available for the entire game (+1 items)
    - Chapter Dagger: One Pristine Dagger per chapter [The fourth one is for the goddess] (+4 items)
    - Princess Dagger: One Pristine Dagger per princess (+23 items)
    """
    display_name = "Pristine Dagger Rando"
    nothing = 1
    one_dagger = 2
    chapter_dagger = 3
    princess_dagger = 4
    default = 2


class GiftRando(DefaultOnToggle):
    """
    Shuffles gifts into the item pool as progression items required to complete loops. (+5 items)
    """
    display_name = "Gift Rando"


class ChapterRando(DefaultOnToggle):
    """
    Adds all chapter as check locations in the world. (+23 locations)
    """
    display_name = "Chapter Rando"


class GlobalChapterRando(DefaultOnToggle):
    """
    Adds global chapter (2 and 3) as check locations in the world. (+2 locations)
    """
    display_name = "Chapter Rando"


class HearthRando(DefaultOnToggle):
    """
    Adds hearths (vessels) as check locations in the world. (+29 locations)
    """
    display_name = "Hearth Rando"


class MirrorRando(DefaultOnToggle):
    """
    Adds facing the mirror in the end of the 5 loops as check locations in the world. (+5 locations)
    """
    display_name = "Mirror Rando"


@dataclass
class SlayThePrincessOptions(PerGameCommonOptions):
    #Game Options
    #goal: Goal
    #entrance_rando: EntranceRando

    #Item
    chapter_access: ChapterAccessRando
    #couple_princesses_and_voices: CouplePrincessesAndVoices
    #all_voices_chapter: AllVoicesChapter
    pristine_dagger_rando: PristineDaggerRando
    #force_chapter1_dagger: ForceChapter1DaggerRando
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
    #memoriesanity: Memoriesanity

slay_the_princess_option_groups = [
    #OptionGroup("Game Options", [
        #Goal,
        #EntranceRando,
    #]),
    OptionGroup("Item Options", [
        ChapterAccessRando,
        #CouplePrincessesAndVoices
        #AllVoicesChapter
        PristineDaggerRando,
        #ForceChapter1DaggerRando,
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
        #Memoriesanity,
    ]),
]