from archer import Archer
from knight import Knight
from pykeman import Pykeman
from wizard import Wizard
from npc_states import *


def game():
    knight = Knight()
    knight2 = Knight()
    knight3 = Knight()
    knight4 = Knight()
    knight5 = Knight()


    print(f"Stats Knight --> HP: {knight.hp}, DMG: {knight.damage}, ARMOUR: {knight.armour}, MAGIC: {knight.magic}, "
          f"HUNGER: {knight.hunger}")

    knight.takeDamage(NPCDeBuff.STARVING, 75)

    print(f"Stats Knight --> HP: {knight.hp}, DMG: {knight.damage}, ARMOUR: {knight.armour}, MAGIC: {knight.magic}, "
          f"HUNGER: {knight.hunger}")


if __name__ == "__main__":
    game()
