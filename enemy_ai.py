import random
from check_win import check_win

CORNERS = [0, 2, 6, 8]
EDGES = [1, 3, 5, 7]


class EnemyAI:
    def __init__(self, name, mark, mode):
        self.name = name
        self.mark = mark
        self.available_slots = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.available_slots_corners = [0, 2, 6, 8]
        self.available_slots_edges = [1, 3, 5, 7]
        self.difficulty = mode

    def update(self, board, player, move_number):
        # update available slots data
        available_slots_copy = self.available_slots.copy()
        for i in available_slots_copy:
            if board[i] == self.mark or board[i] == player.mark:
                self.available_slots.remove(i)
                if i in self.available_slots_corners:
                    self.available_slots_corners.remove(i)
                if i in self.available_slots_edges:
                    self.available_slots_edges.remove(i)

        # selection depends on move number
        match move_number:
            case 0:  # Computer is player 1
                if self.difficulty == 3:
                    # select a corner as first move
                    select = random.choice(self.available_slots_corners)
                    return select + 1
                else:
                    select = random.choice(self.available_slots)
                    return select + 1

            case 1:  # Computer is player 2
                if self.difficulty == 3:
                    # if player didn't start at center, select the center
                    if board[4] != player.mark:
                        return 5
                    # else select any available corner
                    else:
                        select = random.choice(self.available_slots_corners)
                        return select + 1
                else:
                    select = random.choice(self.available_slots)
                    return select + 1

            case 2:  # Computer is player 1
                if self.difficulty == 3:
                    # if player didn't select center, select a corner
                    if board[4] != player.mark:
                        select = self.possible_win_move(board, self.mark, 1)
                        return select + 1
                    # else if player select center then select opposite corner
                    elif self.difficulty == 3:
                        select = self.opposite_corner(board.copy(), self.mark)
                        return select + 1
                # else select any available slot
                select = random.choice(self.available_slots)
                return select + 1

            case 3:  # Computer is player 2
                if self.difficulty > 1:
                    # block player if player is about to win
                    possible_win_block = self.check_possible_win(board.copy(), player.mark)
                    if possible_win_block != "False":
                        return possible_win_block + 1
                    if self.difficulty == 3:
                        # if player has both opposite corners, select an edge
                        opposite = self.opposite_corner_same(board.copy(), player.mark)
                        if opposite != "False":
                            select = random.choice(self.available_slots_edges)
                            return select + 1
                        # block player if player is about to make a two winning move
                        possible_two_block = self.possible_win_move(board.copy(), player.mark, 2)
                        if possible_two_block != "False":
                            return possible_two_block + 1
                        # else select opposite corner if computer's first move was not center slot
                        if board[4] != self.mark:
                            select = self.opposite_corner(board, self.mark)
                            if select != "False":
                                return select + 1
                    # else select any available corner
                    select = random.choice(self.available_slots_corners)
                    return select + 1
                # else select any available slot
                select = random.choice(self.available_slots)
                return select + 1

            case 4 | 5:  # Computer is player 1 or 2
                # check if computer can win
                possible_win = self.check_possible_win(board.copy(), self.mark)
                if possible_win != "False":
                    return possible_win + 1
                if self.difficulty > 1:
                    # else block player if player is about to win
                    possible_win_block = self.check_possible_win(board.copy(), player.mark)
                    if possible_win_block != "False":
                        return possible_win_block + 1
                    if self.difficulty == 3:
                        # else check if two winning moves is possible
                        possible_two = self.possible_win_move(board.copy(), self.mark, 2)
                        if possible_two != "False":
                            return possible_two + 1
                        # else check if one winning move is possible
                        possible_one = self.possible_win_move(board.copy(), self.mark, 1)
                        if possible_one != "False":
                            return possible_one + 1
                # else select any available slot
                select = random.choice(self.available_slots)
                return select + 1

            case _:  # rest of move numbers. Computer is player 1 or 2
                # check if computer can win
                possible_win = self.check_possible_win(board.copy(), self.mark)
                if possible_win != "False":
                    return possible_win + 1
                # else block player if player is about to win
                if self.difficulty > 1:
                    possible_win_block = self.check_possible_win(board.copy(), player.mark)
                    if possible_win_block != "False":
                        return possible_win_block + 1
                # else select any available slot
                select = random.choice(self.available_slots)
                return select + 1

    def check_possible_win(self, board, mark):
        for i in self.available_slots:
            original_i = board[i]
            board[i] = mark
            win_imminent = check_win(board, mark)
            if win_imminent:
                return i
            board[i] = original_i
        return "False"

    def possible_win_move(self, board, mark, winning_move):
        # setup
        center = []
        available_slots_corners_base = self.available_slots_corners.copy()
        available_slots_corners_opposite = []
        if 4 in self.available_slots:
            center.append(4)
        for current_slot in available_slots_corners_base:
            opposite_slot = -(current_slot - 8)
            if board[opposite_slot] == mark:
                available_slots_corners_base.remove(current_slot)
                available_slots_corners_opposite.append(current_slot)
        # prioritise corners that are not opposite first, then opposite corner, center, and edges
        slots_to_check = [available_slots_corners_base, available_slots_corners_opposite,
                          center, self.available_slots_edges]
        for available_slots_target in slots_to_check:
            print(available_slots_target)
            for i in available_slots_target:
                original_i = board[i]
                board[i] = mark
                available_slots_lvl1 = self.available_slots.copy()
                available_slots_lvl1.remove(original_i - 1)
                for j in available_slots_lvl1:
                    original_j = board[j]
                    board[j] = mark
                    win_imminent = check_win(board.copy(), mark)
                    board[j] = original_j
                    if win_imminent:
                        if winning_move == 1:
                            return i
                        else:
                            available_slots_lvl2 = available_slots_lvl1.copy()
                            available_slots_lvl2.remove(original_j - 1)
                            for k in available_slots_lvl2:
                                original_k = board[k]
                                board[k] = mark
                                win_imminent = check_win(board.copy(), mark)
                                if win_imminent:
                                    return i
                                board[k] = original_k
                board[i] = original_i
        return "False"

    def opposite_corner(self, board, mark):
        for current_slot in self.available_slots_corners:
            opposite_slot = -(current_slot - 8)
            if board[opposite_slot] == mark:
                return current_slot
        return "False"

    def opposite_corner_same(self, board, mark):
        self.is_not_used()
        for current_slot in CORNERS:
            if board[current_slot] == mark:
                opposite_slot = -(current_slot - 8)
                if board[opposite_slot] == mark:
                    return current_slot
        return "False"

    def is_not_used(self):
        pass
