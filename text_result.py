import sys
from pathlib import Path

# Add project directory to the Python path
project_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_dir))

import tictactoe as ttt


def print_board(title, board):
    """Display a Tic-Tac-Toe board."""
    print(f"\n{title}")
    print("-" * 20)
    for row in board:
        print(row)


# Initial board
board = [
    [ttt.X, ttt.O, ttt.X],
    [ttt.O, ttt.EMPTY, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
]

# Show original board
print_board("Original Board", board)

# Apply a move at row 1, column 1
move = (1, 1)
updated_board = ttt.result(board, move)

# Show updated board
print_board("Board After Move", updated_board)

# Verify the original board is unchanged
print_board("Original Board (Unchanged)", board)

print(f"\nMove Applied: {move}")