def check_win(board, mark):
    if board[4] == mark:    # from number 5
        if board[0] == mark and board[8] == mark:
            return True
        elif board[1] == mark and board[7] == mark:
            return True
        elif board[2] == mark and board[6] == mark:
            return True
        elif board[3] == mark and board[5] == mark:
            return True
    if board[1] == mark:  # from number 2
        if board[0] == mark and board[2] == mark:
            return True
    if board[5] == mark:  # from number 6
        if board[2] == mark and board[8] == mark:
            return True
    if board[7] == mark:  # from number 8
        if board[6] == mark and board[8] == mark:
            return True
    if board[3] == mark:  # from number 4
        if board[0] == mark and board[6] == mark:
            return True

    return False
