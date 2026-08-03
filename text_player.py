import sys
from pathlib import Path

# Include the project directory
project_path = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_path))

import tictactoe as ttt


def display_board(board):
    """Print the board row by row."""
    for row in board:
        print(row)


# Create the initial game board
board = ttt.initial_state()

print("=== Tic-Tac-Toe Initial State ===")
display_board(board)

# Show whose turn it is
player = ttt.player(board)
print("\nCurrent Player:", player)

# Show all possible moves
moves = ttt.actions(board)
print("\nAvailable Moves:")
for move in sorted(moves):
    print(move)