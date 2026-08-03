"""
Tic Tac Toe AI using Minimax Algorithm
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Creates and returns an empty 3x3 board.
    """
    return [[EMPTY for _ in range(3)] for _ in range(3)]


def player(board):
    """
    Determines whose turn it is.
    """

    total_x = sum(row.count(X) for row in board)
    total_o = sum(row.count(O) for row in board)

    return X if total_x == total_o else O


def actions(board):
    """
    Returns every empty position on the board.
    """

    available = set()

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                available.add((row, col))

    return available


def result(board, action):
    """
    Returns a new board after applying a move.
    """

    row, col = action

    if board[row][col] is not EMPTY:
        raise Exception("Move is not allowed.")

    updated_board = copy.deepcopy(board)
    updated_board[row][col] = player(board)

    return updated_board


def winner(board):
    """
    Returns X or O if either player wins.
    """

    winning_lines = []

    # Rows
    winning_lines.extend(board)

    # Columns
    winning_lines.extend([[board[r][c] for r in range(3)] for c in range(3)])

    # Diagonals
    winning_lines.append([board[i][i] for i in range(3)])
    winning_lines.append([board[i][2 - i] for i in range(3)])

    for line in winning_lines:
        if line[0] is not EMPTY and line.count(line[0]) == 3:
            return line[0]

    return None


def terminal(board):
    """
    Checks whether the game has ended.
    """

    if winner(board):
        return True

    return all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Assigns utility values to terminal states.
    """

    game_result = winner(board)

    if game_result == X:
        return 1

    if game_result == O:
        return -1

    return 0


def max_value(board):
    """
    Computes the highest possible utility.
    """

    if terminal(board):
        return utility(board)

    best = -math.inf

    for move in actions(board):
        score = min_value(result(board, move))
        best = max(best, score)

    return best


def min_value(board):
    """
    Computes the lowest possible utility.
    """

    if terminal(board):
        return utility(board)

    best = math.inf

    for move in actions(board):
        score = max_value(result(board, move))
        best = min(best, score)

    return best


def minimax(board):
    """
    Returns the best possible move.
    """

    if terminal(board):
        return None

    turn = player(board)

    if turn == X:

        highest_score = -math.inf
        chosen_move = None

        for move in actions(board):
            value = min_value(result(board, move))

            if value > highest_score:
                highest_score = value
                chosen_move = move

        return chosen_move

    else:

        lowest_score = math.inf
        chosen_move = None

        for move in actions(board):
            value = max_value(result(board, move))

            if value < lowest_score:
                lowest_score = value
                chosen_move = move

        return chosen_move