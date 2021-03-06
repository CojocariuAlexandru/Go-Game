from graphics import *

dl = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


"""Resets the board - all elemenets have 0 value"""
def reset_board():
    global board
    board = []
    for i in range(0, 19):
        row = []
        for j in range(0, 19):
            row.append(0)
        board.append(row)


"""Check is coordinates are valid for a piece"""
def check_valid_position(x, y):
    global board
    if board[x][y] == 0:
        return True
    return False


"""Counts the number of pieces on the board"""
def get_winner():
    global board
    free = 0
    white = 0
    black = 0
    total = 19*19
    for i in range(0, 19):
        for j in range(0, 19):
            if board[i][j] == 0:
                free += 1
            elif board[i][j] == 1:
                white += 1
            else:
                black += 1
    if white > free + black:
        return 'white'
    elif black > free + white:
        return 'black'
    else:
        return 'nowinner'


"""Adds a piece on the board"""
def add_piece(x, y, turn, score_white, score_black):
    global board
    if turn == 'white':
        board[x][y] = 1
        score_white += 1
    else:
        board[x][y] = 2
        score_black += 1
    return (score_white, score_black)


"""Crosses on screen the eliminated pieces"""
def mark_eliminated_pieces(window):
    global board_aux
    for i in range(0, 19):
        for j in range(0, 19):
            if board_aux[i][j] == -3:
                line1 = Line(Point(35 + j*30, 35+i*30),
                             Point(35 + (j+1)*30, 35+(i+1)*30))
                line1.setFill('red')
                line1.draw(window)


"""Marks on the matrix the eliminated pieces"""
def eliminate_surrounded_pieces(score_white, score_black):
    global board
    global board_aux
    board_aux = []
    board_aux = board
    score_white = 0
    score_black = 0
    for i in range(0, 19):
        for j in range(0, 19):
            if board_aux[i][j] == 1 or board_aux[i][j] == 2:
                if not has_liberty(i, j):
                    fill(i, j, -3)
    for i in range(0, 19):
        for j in range(0, 19):
            if board_aux[i][j] == -1:
                board[i][j] = 1
                score_white += 1
            elif board_aux[i][j] == -2:
                board[i][j] = 2
                score_black += 1
    return (score_white, score_black)


"""Applies Lee's algorithm to check if a piece is surrounded"""
def has_liberty(x, y):
    global queue
    queue = []
    hasLibery = False
    color = board_aux[x][y]
    queue.append([x, y])
    while len(queue) > 0:
        curr_pos = queue.pop(0)
        new_pos = curr_pos
        for i in range(0, 4):
            new_pos[0] += dl[i]
            new_pos[1] += dc[i]
            if 0 <= new_pos[0] <= 18 and 0 <= new_pos[1] <= 18:
                if board_aux[new_pos[0]][new_pos[1]] == color:
                    queue.append([new_pos[0], new_pos[1]])
                if board_aux[new_pos[0]][new_pos[1]] == 0:
                    hasLibery = True
            new_pos[0] -= dl[i]
            new_pos[1] -= dc[i]
        board_aux[curr_pos[0]][curr_pos[1]] = -color
    return hasLibery


"""If a piece is surounded propagate its value to all neighbours"""
def fill(x, y, new_val):
    color = board_aux[x][y]
    queue.append([x, y])
    while len(queue) > 0:
        curr_pos = queue.pop(0)
        new_pos = curr_pos
        for i in range(0, 4):
            new_pos[0] += dl[i]
            new_pos[1] += dc[i]
            if 0 <= new_pos[0] <= 18 and 0 <= new_pos[1] <= 18:
                if board_aux[new_pos[0]][new_pos[1]] == color:
                    queue.append([new_pos[0], new_pos[1]])
            new_pos[0] -= dl[i]
            new_pos[1] -= dc[i]
        board_aux[curr_pos[0]][curr_pos[1]] = new_val
