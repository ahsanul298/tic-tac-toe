import sys
from pathlib import Path

# Add the project root directory to Python's path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

import tictactoe as ttt

# Sample Tic-Tac-Toe board
board = [
    [ttt.X, ttt.O, ttt.X],
    [ttt.EMPTY, ttt.O, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.EMPTY]
]

# Display the board
print("Current Board:")
for row in board:
    print(row)

# Display current player
current_player = ttt.player(board)
print("\nCurrent Player:", current_player)

# Display available moves
available_moves = ttt.actions(board)
print("Available Moves:", available_moves)