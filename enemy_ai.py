import random
from check_win import check_win


def check_possible_win(board, player, available_slots):
    for i in available_slots:
        original_i = board[i]
        board[i] = player.mark
        win_imminent = check_win(board, player.mark)
        if win_imminent == True:
            return i
        board[i] = original_i
    return False


def check_possible_two(board, player, available_slots, available_corners):
    # prioritise corners first
    slots_to_check = [available_corners, available_slots]
    for available_slots_lvl1 in slots_to_check:
        for i in available_slots_lvl1:
            original_i = board[i]
            board[i] = player.mark
            available_slots_lvl2 = available_slots_lvl1.copy()
            available_slots_lvl2.remove(i)
            for j in available_slots_lvl2:
                original_j = board[j]
                board[j] = player.mark
                win_imminent = check_win(board.copy(), player.mark)
                board[j] = original_j
                if win_imminent == True:
                    available_slots_lvl3 = available_slots_lvl2.copy()
                    available_slots_lvl3.remove(j)
                    for k in available_slots_lvl3:
                        original_k = board[k]
                        board[k] = player.mark
                        win_imminent = check_win(board.copy(), player.mark)
                        if win_imminent == True:
                            return i
                        board[k] = original_k
            board[i] = original_i

    return False


def check_opposite_corner(board, player, opponent):
    if board[0] == player.mark:
        if board[8] != opponent.mark:
            return 8
    if board[2] == player.mark:
        if board[6] != opponent.mark:
            return 6
    if board[6] == player.mark:
        if board[2] != opponent.mark:
            return 2
    if board[8] == player.mark:
        if board[0] != opponent.mark:
            return 0

    return False


def main(board, computer, player, round):
    select = None
    # collect data of available slots into array
    available_slots = []
    available_slots_corners = []
    corners = [0, 2, 6, 8]
    edges = [1, 3, 5, 7]
    for i in range(0, 9):
        if board[i] != computer.mark and board[i] != player.mark:
            available_slots.append(i)
            if i in corners:
                available_slots_corners.append(i)

    # selection depends on round
    if round == 0:  # Computer is player 1
        # select a corner as first move
        select = random.choice(corners)
        return select + 1
    elif round == 1:  # Computer is player 2
        # if player starts at corner, select the center
        for i in corners:
            if board[i] == player.mark:
                return 5
        else:
            # else select any available corner
            select = random.choice(available_slots_corners)
            return select + 1
    elif round == 2:  # Computer is player 1
        # if player didn't select center
        if board[4] != player.mark:
            for i in corners:
                if board[i] == player.mark:
                    select = random.choice(available_slots_corners)
                    return select + 1
            return 5
        # else select opposite corner
        select = check_opposite_corner(board.copy(), computer, player)
        return select + 1
    elif round == 3:  # Computer is player 2
        # block player if player is about to win
        possible_win = check_possible_win(board.copy(), player, available_slots)
        if possible_win != False:
            return possible_win + 1

        # if player has both opposite corners, select an edge
        opposite = check_opposite_corner(board, player, computer)
        if opposite != False:
            select = random.choice(edges)
            return select + 1

        # block player if player is about to make a two winning move
        possible_two = check_possible_two(board.copy(), player, available_slots, available_slots_corners)
        if possible_two != False:
            return possible_two + 1

        # else select opposite corner if first move was not center slot
        if board[4] != computer.mark:
            select = check_opposite_corner(board, computer, player)
            if select != False:
                return select + 1

        # else select any available corner
        select = random.choice(available_slots_corners)
        return select + 1
    elif round == 4 or round == 5:  # Computer is player 1 or 2
        # check if computer can win
        possible_win = check_possible_win(board.copy(), computer, available_slots)
        if possible_win != False:
            return possible_win + 1

        # else block player if player is about to win
        possible_win = check_possible_win(board.copy(), player, available_slots)
        if possible_win != False:
            return possible_win + 1

        # else check if two winning moves is possible
        possible_two = check_possible_two(board.copy(), computer, available_slots, available_slots_corners)
        if possible_two != False:
            return possible_two + 1

        # else select any available slot
        select = random.choice(available_slots)
        return select + 1
    else:   # rest of the rounds. Computer is player 1 or 2
        # check if computer can win
        possible_win = check_possible_win(board.copy(), computer, available_slots)
        if possible_win != False:
            return possible_win + 1

        # else block player if player is about to win
        possible_win = check_possible_win(board.copy(), player, available_slots)
        if possible_win != False:
            return possible_win + 1

        # else select any available slot
        select = random.choice(available_slots)
        return select + 1