import sys
from pathlib import Path

# Add project directory to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

import tictactoe as ttt


def display_board(board):
    """Print the board in a readable format."""
    for row in board:
        print(row)


def run_test(test_name, board):
    """Run a Tic-Tac-Toe AI test."""
    print("\n" + "=" * 40)
    print(f"Test Case: {test_name}")
    print("=" * 40)

    display_board(board)

    print("\nCurrent Player :", ttt.player(board))
    print("Available Moves:", ttt.actions(board))

    if ttt.terminal(board):
        print("Game Status    : Finished")
        print("Winner         :", ttt.winner(board))
        print("Utility Value  :", ttt.utility(board))
    else:
        print("Best Move      :", ttt.minimax(board))


# -------------------------
# Test Case 1
# X can win immediately
# -------------------------
board1 = [
    [ttt.X, ttt.O, ttt.X],
    [ttt.O, ttt.X, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.O]
]

run_test("Winning Move", board1)


# -------------------------
# Test Case 2
# O needs to block X
# -------------------------
board2 = [
    [ttt.X, ttt.X, ttt.EMPTY],
    [ttt.O, ttt.EMPTY, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.O]
]

run_test("Blocking Move", board2)


# -------------------------
# Test Case 3
# Empty Board
# -------------------------
board3 = ttt.initial_state()

run_test("Initial Board", board3)


# -------------------------
# Test Case 4
# Game Already Finished
# -------------------------
board4 = [
    [ttt.X, ttt.X, ttt.X],
    [ttt.O, ttt.O, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
]

run_test("Finished Game", board4)


# -------------------------
# Test Case 5
# Draw Game
# -------------------------
board5 = [
    [ttt.X, ttt.O, ttt.X],
    [ttt.X, ttt.O, ttt.O],
    [ttt.O, ttt.X, ttt.X]
]

run_test("Draw Game", board5)