from archer import Archer
from knight import Knight
from pykeman import Pykeman
from wizard import Wizard
from npc_states import *


def game():
    knight = Knight()

    print(f"Stats Knight --> HP: {knight.hp}, DMG: {knight.damage}, ARMOUR: {knight.armour}, MAGIC: {knight.magic}, "
          f"HUNGER: {knight.hunger}, MANA: {knight.mana}")

    knight.takeDamage(NPCDeBuff.BURNING)

    print(f"Stats Knight --> HP: {knight.hp}, DMG: {knight.damage}, ARMOUR: {knight.armour}, MAGIC: {knight.magic}, "
          f"HUNGER: {knight.hunger}, MANA: {knight.mana}")

    knight.healing()

    print(f"Stats Knight --> HP: {knight.hp}, DMG: {knight.damage}, ARMOUR: {knight.armour}, MAGIC: {knight.magic}, "
          f"HUNGER: {knight.hunger}, MANA: {knight.mana}")


if __name__ == "__main__":
    game()
