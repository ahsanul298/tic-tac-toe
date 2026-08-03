import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

import tictactoe as ttt


def show_board(board):
    """Display the Tic-Tac-Toe board."""
    print("Current Board")
    print("-" * 20)
    for row in board:
        print(row)
    print("-" * 20)


# Sample board
board = [
    [ttt.X, ttt.O, ttt.X],
    [ttt.O, ttt.X, ttt.EMPTY],
    [ttt.EMPTY, ttt.EMPTY, ttt.O]
]

# Display board
show_board(board)

# Display game information
current_player = ttt.player(board)
game_over = ttt.terminal(board)

print(f"Current Player : {current_player}")
print(f"Game Over      : {game_over}")

# Evaluate board using Minimax helper functions
print("\nBoard Evaluation")
print(f"Max Value : {ttt.max_value(board)}")
print(f"Min Value : {ttt.min_value(board)}")