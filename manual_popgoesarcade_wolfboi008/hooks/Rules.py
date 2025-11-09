from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

def defeatCorruptChica(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "{ItemValue(battle_points:10)}"

def defeatCorruptFoxy(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "{ItemValue(battle_points:19)}"

def defeatCorruptBonnie(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "{ItemValue(battle_points:28)}"

def defeatCorruptBB(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "{ItemValue(battle_points:37)} AND |@Gate Keys:3|"

def defeatDeadChica(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "{ItemValue(battle_points:43)} AND |@Gate Keys:3|"

def defeatDeadFoxy(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "{ItemValue(battle_points:46)} AND |@Gate Keys:3| AND |Jump|"

def defeatDeadBonnie(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "{ItemValue(battle_points:49)} AND |@Gate Keys:3| AND |Jump| AND |Hook|"

def defeatDeadKingFreddy(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "{ItemValue(battle_points:49)} AND |@Gate Keys:3| AND |@Door Keys:3| AND |Jump| AND |Hook| AND |Dig|"