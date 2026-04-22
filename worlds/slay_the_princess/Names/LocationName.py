win = "Victory Condition"

# Chapter
chap2 = "Reach Chapter 2"
chap3 = "Reach Chapter 3"

# The Long Quiet
mirror1 = "The Body"
mirror2 = "The Bloat"
mirror3 = "The Decay"
mirror4 = "The Remains"
mirror5 = "The Long Quiet"

# Princesses
adversary = "Find The Adversary"
tower = "Find The Tower"
spectre = "Find The Spectre"
nightmare = "Find The Nightmare"
razor = "Find The Razor"
beast = "Find The Beast"
witch = "Find The Witch"
stranger = "Find The Stranger"
prisoner = "Find The Prisoner"
damsel = "Find The Damsel"

needle = "Find The Eye of the Needle"
fury = "Find The Fury"
apotheosis = "Find The Apotheosis"
dragon = "Find The Princess and the Dragon"
wraith = "Find The Wraith"
clarity = "Find The Moment of Clarity"
den = "Find The Den"
wild = "Find The Wild"
thorn = "Find The Thorn"
cage = "Find The Cage"
grey = "Find The Grey"
happily = "Find Happily Ever After"

goddess = "Find The Shifting Mound"

# Heart
adversary_heart = "A Bold Heart"
tower_heart = "An Overwhelming Heart"
spectre_heart = "A Yearning Heart"
nightmare_heart = "A Tender Heart"
razor_heart_iron = "A Piercing Heart in a Cage of Iron"
razor_heart_free = "A Piercing Heart, Beating Free"
beast_heart = "A Cunning Heart"
witch_heart = "A Righteous Heart"
stranger_heart = "A Rich and Vibrant Heart"
prisoner_heart_patient = "A Patient Heart"
prisoner_heart_clever = "A Clever Heart"
damsel_heart_gentle = "A Gentle Heart"
damsel_heart_pliable = "A Pliable Heart"

needle_heart = "A Burning Heart"
fury_heart_weathered = "A Weathered Heart"
fury_heart_unwound = "A Weathered Heart, Held in Ribbons"
apotheosis_heart = "A Terrifying and Divine Heart"
dragon_heart_main = "An Empathetic Heart"
dragon_heart_stencil = "An Empathetic Heart, Held in Stencil"
wraith_heart = "A Driven Heart"
clarity_heart = "A Wise Heart"
den_heart = "A Ravenous Heart"
wild_heart_curious = "A Curious and Beautiful Heart"
wild_heart_scarred = "A Scarred and Beautiful Heart"
thorn_heart = "A Cautious Heart"
cage_heart_open = "An Open Heart, or a Watchful One"
grey_heart_bright = "A Bright Heart"
grey_heart_deep = "A Deep Heart"
happily_heart = "An Honest Heart"

# Gallery
def _gallery_list(route_name, count) -> list[str]:
    # Index 0 is intentionally empty so callers can use 1-based gallery indexes.
    return [""] + [f"{route_name} (Gallery {i})" for i in range(1, count + 1)]

# Beginnings & Endings
gallery_princess: list[str] = _gallery_list("The Hero and the Princess", 18)
gallery_spaceBetween: list[str] = _gallery_list("The Spaces Between", 9)
gallery_finale: list[str] = _gallery_list("The End of Everything", 20)

# 1st Row
gallery_adversary: list[str] = _gallery_list("The Adversary", 20)
gallery_tower: list[str] = _gallery_list("The Tower", 13)
gallery_spectre: list[str] = _gallery_list("The Spectre", 18)
gallery_nightmare: list[str] = _gallery_list("The Nightmare", 19)
gallery_razor: list[str] = _gallery_list("The Razor", 20)
gallery_beast: list[str] = _gallery_list("The Beast", 17)
gallery_witch: list[str] = _gallery_list("The Witch", 20)
gallery_stranger: list[str] = _gallery_list("The Stranger", 12)
gallery_prisoner: list[str] = _gallery_list("The Prisoner", 17)
gallery_damsel: list[str] = _gallery_list("The Damsel", 20)

# 2nd Row
gallery_needle: list[str] = _gallery_list("The Eye of the Needle", 20)
gallery_fury: list[str] = _gallery_list("The Fury", 20)
gallery_apotheosis: list[str] = _gallery_list("The Apotheosis", 20)
gallery_dragon: list[str] = _gallery_list("The Princess and the Dragon", 20)
gallery_wraith: list[str] = _gallery_list("The Wraith", 11)
gallery_clarity: list[str] = _gallery_list("The Moment of Clarity", 14)
gallery_den: list[str] = _gallery_list("The Den", 20)
gallery_wild: list[str] = _gallery_list("The Wild", 12)
gallery_thorn: list[str] = _gallery_list("The Thorn", 19)
gallery_cage: list[str] = _gallery_list("The Cage", 20)
gallery_grey: list[str] = _gallery_list("The Grey", 20)
gallery_happily: list[str] = _gallery_list("Happily Ever After", 20)
