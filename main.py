# a text-based version of tic-tac-toe by Aidi Khalid

from art import logo
from player import Player
from enemy_ai import EnemyAI
from check_win import check_win

board_base = [1, 2, 3,
              4, 5, 6,
              7, 8, 9]


def draw_board(board):
    print("")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("")


def verify_number(select, choice, board, player):
    number_valid = False
    number_is_number = False

    while not number_valid:
        while not number_is_number:
            try:
                select = int(select)
            except ValueError:
                if board:
                    select = input(f"<({player.mark}){player.name}> That was not a number. Please try again: ")
                else:
                    select = input("That was not a number. Please try again: ")
            else:
                number_is_number = True

        if board:
            if select < 1 or select > choice:
                select = input(f"<({player.mark}){player.name}> Number selected is not on board. Please try again: ")
                number_is_number = False
            elif board[select - 1] != select:
                select = input(f"<({player.mark}){player.name}> That spot is already taken. Please try again: ")
                number_is_number = False
            else:
                number_valid = True
        else:
            if select < 1 or select > choice:
                select = input("Number selected is not valid. Please try again: ")
                number_is_number = False
            else:
                number_valid = True
    return select


def play_game():
    print("\nNEW GAME")
    menu_1 = "\n1. Player VS Computer\n2. Player VS Player"
    print(menu_1)
    versus = input("\nSelect 1 or 2 for type of game: ")
    versus = verify_number(versus, 2, None, None)

    # setup default players
    player_1 = Player("PLAYER 1", "X")
    player_2 = Player("PLAYER 2", "O")
    # query on who is playing, redefine players as needed
    if versus == 1:
        print("\nPLAYER VS COMPUTER")
        print("\n1. Easy\n2. Medium\n3. Impossible")
        difficulty = input("\nSelect difficulty level: ")
        difficulty = verify_number(difficulty, 3, None, None)
        if difficulty == 1:
            print("\nEASY DIFFICULTY")
        elif difficulty == 2:
            print("\nMEDIUM DIFFICULTY")
        else:
            print("\nIMPOSSIBLE DIFFICULTY")
        print("\n1. Player\n2. Computer")
        first = input("\nSelect 1 or 2 to decide who goes first: ")
        first = verify_number(first, 2, None, None)
        if first == 1:
            player_1 = Player("PLAYER", "X")
            player_2 = EnemyAI("COMPUTER", "O", difficulty)
        else:
            player_1 = EnemyAI("COMPUTER", "X", difficulty)
            player_2 = Player("PLAYER", "O")
    else:
        print("\nPLAYER VS PLAYER")

    # quick tip
    print("\nTip: the board's number arrangement is like the keypad so you may want to use the keypad.")

    # setup game
    board = board_base.copy()
    players = [player_1, player_2]
    game_over = False
    move_number = 0
    i = 0

    # start game
    while not game_over:
        # start with first player / switch players
        current_player = players[i]
        i = -(i - 1)
        next_player = players[i]

        print(f"\n{current_player.name}'S TURN")
        draw_board(board)

        # player move
        if current_player.name == "COMPUTER":
            select = current_player.update(board.copy(), next_player, move_number)
            print(f"<({current_player.mark}){current_player.name}> Selects: {select}")
        else:
            select = input(f"<({current_player.mark}){current_player.name}> Select a number above to mark: ")
            select = verify_number(select, 9, board, current_player)

        # put player's mark on selected board slot
        board[select - 1] = current_player.mark

        # check if a line is formed
        game_over = check_win(board, current_player.mark)
        if game_over:
            draw_board(board)
            print(f"({current_player.mark}){current_player.name} WINS!")
        else:
            # increment move_number and check if round limit reached
            move_number = move_number + 1
            if move_number == 9:
                draw_board(board)
                print(f"IT'S A DRAW!")
                game_over = True


# main
print(logo)
print("\nA text-based version of Tic-Tac-Toe by Aidi Khalid")
repeat = True
while repeat:
    play_game()
    menu_3 = "\n1. New game\n2. Exit"
    print(menu_3)
    play_again = input("\nSelect 1 or 2: ")
    play_again = verify_number(play_again, 2, None, None)
    if play_again == 1:
        continue
    else:
        repeat = False
