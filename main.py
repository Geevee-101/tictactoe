# a text-based version of tic-tac-toe by Aidi Khalid

from art import logo
from player import Player
import enemy_ai
from check_win import check_win

board_base = [1, 2, 3,
              4, 5, 6,
              7, 8, 9]


def draw_board(board):
    print("")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("")


def verify_number(select, board, player):
    number_valid = False
    number_is_number = False

    while number_valid == False:

        while number_is_number == False:
            try:
                select = int(select)
            except ValueError:
                draw_board(board)
                select = input(f"<({player.mark}){player.name}> That was not a number. Please try again: ")
            else:
                number_is_number = True

        if select < 1 or select > 9:
            draw_board(board)
            select = input(f"<({player.mark}){player.name}> Number selected is not on board. Please try again: ")
            number_is_number = False
        elif board[select - 1] != select:
            draw_board(board)
            select = input(f"<({player.mark}){player.name}> That spot is already taken. Please try again: ")
            number_is_number = False
        else:
            number_valid = True
    return select


def verify_menu_number(choice, menu):
    number_valid = False
    number_is_number = False

    while number_valid == False:

        while number_is_number == False:
            try:
                choice = int(choice)
            except ValueError:
                print(menu)
                choice = input("\nThat was not a number. Please try again: ")
            else:
                number_is_number = True

        if choice < 1 or choice > 2:
            print(menu)
            choice = input("\nOnly option 1 or 2 is available. Please try again: ")
            number_is_number = False
        else:
            number_valid = True
    return choice


def play_game():
    print("\nNEW GAME")
    menu_1 = "\n1. Player VS Computer\n2. Player VS Player"
    print(menu_1)
    versus = input("\nSelect 1 or 2 for type of game: ")
    versus = verify_menu_number(versus, menu_1)

    # setup players
    player_1 = Player("PLAYER 1", "X")
    player_2 = Player("PLAYER 2", "O")

    if versus == 1:
        print("\nPLAYER VS COMPUTER")
        menu_2 = "\n1. Player\n2. Computer"
        print(menu_2)
        first = input("\nSelect 1 or 2 to decide who goes first: ")
        first = verify_menu_number(first, menu_2)
        if first == 1:
            player_1.name = "PLAYER"
            player_2.name = "COMPUTER"
        else:
            player_1.name = "COMPUTER"
            player_2.name = "PLAYER"
    else:
        print("\nPLAYER VS PLAYER")

    # setup game
    board = board_base.copy()
    current_player = player_1
    game_over = False
    round = 0

    while game_over == False:
        print(f"\n{current_player.name}'S TURN")
        draw_board(board)

        if current_player.name == "COMPUTER":
            computer = current_player
            player = player_1
            if current_player == player_1:
                player = player_2
            select = enemy_ai.main(board.copy(), computer, player, round)
            print(f"<({current_player.mark}){current_player.name}> Selects: {select}")
        else:
            select = input(f"<({current_player.mark}){current_player.name}> Select a number above to mark: ")

            # verify number is valid
            select = verify_number(select, board, current_player)

        # revert the board and mark it
        board[select - 1] = current_player.mark

        # check if a line is formed
        game_over = check_win(board, current_player.mark)

        round = round + 1

        if game_over == True:
            draw_board(board)
            print(f"({current_player.mark}){current_player.name} WINS!")
        elif round == 9:
            draw_board(board)
            print(f"IT'S A DRAW!")
            game_over = True
        else:
            # swap to next player
            if current_player == player_1:
                current_player = player_2
            else:
                current_player = player_1

# main
print(logo)
print("\nA text-based version of Tic-Tac_Toe by Aidi Khalid")
repeat = True
while repeat == True:
    play_game()
    menu_3 = "\n1. New game\n2. Exit"
    print(menu_3)
    play_again = input("\nSelect 1 or 2: ")
    play_again = verify_menu_number(play_again, menu_3)
    if play_again == 1:
        continue
    else:
        repeat = False
