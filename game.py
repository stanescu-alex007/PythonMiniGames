from utilz.playMethods import *


def game():
    print("----------------PLAYER 1-----------------")
    player1_name = choseName()
    player1_character = choseCharacter()
    print("----------------PLAYER 2-----------------")
    player2_name = choseName()
    player2_character = choseCharacter()
    print("\n\n\n\n\n")
    while player1_character.hp > 0 or player2_character.hp > 0:
        print(f"---------{player1_name} turn---------")
        takeTurn(player1_character, player2_character)

        if player1_character.hp <= 0 or player2_character.hp <= 0:
            seeStats(player1_character, player1_name)
            seeStats(player2_character, player2_name)
            return checkWin(player1_character, player2_character, player1_name, player2_name)

        print(f"---------{player2_name} turn---------")
        takeTurn(player2_character, player1_character)


if __name__ == "__main__":
    game()
