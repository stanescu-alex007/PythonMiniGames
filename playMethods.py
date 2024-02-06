from archer import Archer
from knight import Knight
from npc_states import *
from pykeman import Pykeman
from wizard import Wizard


def choseName():
    player = input("What is your name: ")
    print(f"Ok, Mr. {player}. It's time for you to select your character!")
    return player


def choseCharacter():
    print("1.Knight")
    print("2.Archer")
    print("3.Pykeman")
    print("4.Wizard")

    choice = int(input("Which one are you?\n"))
    match choice:
        case 1:
            print("You are now a worthy Knight!")
            player = Knight()
        case 2:
            print("You are now a good Archer!")
            player = Archer()
        case 3:
            print("You are now a sharp Pykeman!")
            player = Pykeman()
        case 4:
            print("You are now a powerful Wizard!")
            player = Wizard()
        case _:
            print("You are just a tarnished!")

    return player


def choseAction(player1, player2):
    print("1.Attack")
    print("2.Heal")
    print("3.Fire")
    print("4.Poison")

    choice = int(input("What do you want to do?\n"))
    match choice:
        case 1:
            print("You have attacked your enemy")
            player1.attack(player2)
        case 2:
            print("You healed yourself!")
            player1.healing()
        case 3:
            print("You just burned your enemy alive")
            player2.takeBuffDamage(NPCDeBuff.BURNING)
        case 4:
            print("Your enemy is poisoned")
            player2.takeBuffDamage(NPCDeBuff.POISONED)
        case _:
            print("You are just a tarnished!")


def seeStats(player, name):
    print(f"Stats {name} --> HP: {player.hp}, DMG: {player.damage}, ARMOUR: {player.armour}, MAGIC: {player.magic}, "
          f"HUNGER: {player.hunger}, MANA: {player.mana}")


def checkWin(player1, player2, name1, name2):
    if player1.hp == 0:
        player1.dead()
        print(f"!!!!!!!!!!!!!!!!!! {name2} WINS!!!!!!!!!!!!!!!!!! ")
    if player2.hp == 0:
        player2.dead()
        print(f"!!!!!!!!!!!!!!!!!! {name1} WINS!!!!!!!!!!!!!!!!!! ")


def takeTurn(player1, player2):
    choseAction(player1, player2)
