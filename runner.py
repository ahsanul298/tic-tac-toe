import pygame
import sys
import time
import tictactoe as ttt

# Initialize pygame
pygame.init()

WIDTH, HEIGHT = 600, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe AI")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
TITLE_FONT = pygame.font.Font("OpenSans-Regular.ttf", 40)
TEXT_FONT = pygame.font.Font("OpenSans-Regular.ttf", 28)
MOVE_FONT = pygame.font.Font("OpenSans-Regular.ttf", 60)

# Game variables
user = None
board = ttt.initial_state()
ai_turn = False

while True:

    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill(BLACK)

    # -----------------------------
    # Choose Player Screen
    # -----------------------------
    if user is None:

        title = TITLE_FONT.render("Play Tic-Tac-Toe", True, WHITE)
        SCREEN.blit(title, title.get_rect(center=(WIDTH // 2, 50)))

        x_button = pygame.Rect(WIDTH // 8, HEIGHT // 2, WIDTH // 4, 50)
        o_button = pygame.Rect(5 * WIDTH // 8, HEIGHT // 2, WIDTH // 4, 50)

        pygame.draw.rect(SCREEN, WHITE, x_button)
        pygame.draw.rect(SCREEN, WHITE, o_button)

        SCREEN.blit(
            TEXT_FONT.render("Play as X", True, BLACK),
            TEXT_FONT.render("Play as X", True, BLACK).get_rect(center=x_button.center)
        )

        SCREEN.blit(
            TEXT_FONT.render("Play as O", True, BLACK),
            TEXT_FONT.render("Play as O", True, BLACK).get_rect(center=o_button.center)
        )

        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()

            if x_button.collidepoint(mouse):
                user = ttt.X
                time.sleep(0.2)

            elif o_button.collidepoint(mouse):
                user = ttt.O
                time.sleep(0.2)

    # -----------------------------
    # Game Screen
    # -----------------------------
    else:

        TILE = 80
        origin = (
            WIDTH / 2 - 1.5 * TILE,
            HEIGHT / 2 - 1.5 * TILE
        )

        tiles = []

        for row in range(3):

            current = []

            for col in range(3):

                rect = pygame.Rect(
                    origin[0] + col * TILE,
                    origin[1] + row * TILE,
                    TILE,
                    TILE
                )

                pygame.draw.rect(SCREEN, WHITE, rect, 3)

                if board[row][col] != ttt.EMPTY:
                    symbol = MOVE_FONT.render(board[row][col], True, WHITE)
                    SCREEN.blit(symbol, symbol.get_rect(center=rect.center))

                current.append(rect)

            tiles.append(current)

        game_over = ttt.terminal(board)
        current_player = ttt.player(board)

        # Title
        if game_over:

            winner = ttt.winner(board)

            if winner:
                message = f"Game Over: {winner} Wins!"
            else:
                message = "Game Over: Tie!"

        elif current_player == user:
            message = f"Your Turn ({user})"

        else:
            message = "Computer Thinking..."

        text = TITLE_FONT.render(message, True, WHITE)
        SCREEN.blit(text, text.get_rect(center=(WIDTH // 2, 30)))

        # -----------------------------
        # AI Move
        # -----------------------------
        if not game_over and current_player != user:

            if ai_turn:

                time.sleep(0.5)
                best_move = ttt.minimax(board)
                board = ttt.result(board, best_move)
                ai_turn = False

            else:
                ai_turn = True

        # -----------------------------
        # Human Move
        # -----------------------------
        if pygame.mouse.get_pressed()[0] and current_player == user and not game_over:

            mouse = pygame.mouse.get_pos()

            for i in range(3):
                for j in range(3):

                    if board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse):
                        board = ttt.result(board, (i, j))
                        time.sleep(0.15)

        # -----------------------------
        # Restart Button
        # -----------------------------
        if game_over:

            again_button = pygame.Rect(WIDTH // 3, HEIGHT - 65, WIDTH // 3, 50)

            pygame.draw.rect(SCREEN, WHITE, again_button)

            again = TEXT_FONT.render("Play Again", True, BLACK)

            SCREEN.blit(
                again,
                again.get_rect(center=again_button.center)
            )

            if pygame.mouse.get_pressed()[0]:

                mouse = pygame.mouse.get_pos()

                if again_button.collidepoint(mouse):

                    board = ttt.initial_state()
                    user = None
                    ai_turn = False
                    time.sleep(0.2)

    pygame.display.update()