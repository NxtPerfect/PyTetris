'''For blocks to move down, just move the points lower
or move the polygon lower
if one of the points goes out of bounds, stop moving the block
and spawn new one
if all blocks on a line are occupied, clear them and get points
as well as move all the above ones one step lower'''


from copy import deepcopy
import pygame
import random


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Setting up game window (not main window), where you interact with blocks
GAME_WIDTH = 10
GAME_HEIGHT = 20
TILE_SIZE = 50
GAME_RESOLUTION = GAME_WIDTH * TILE_SIZE, GAME_HEIGHT * TILE_SIZE

FPS = 10

figures_position = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
                    [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                    [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                    [(0, 0), (-1, 0), (0, 1), (-1, -1)],
                    [(0, 0), (0, -1), (0, 1), (-1, -1)],
                    [(0, 0), (0, -1), (0, 1), (1, -1)],
                    [(0, 0), (0, -1), (0, 1), (-1, 0)]]


def check_borders(figure):
    if figure.x < 0 or figure.x > GAME_WIDTH - 1:
        return False
    return True


def main():
    # Initialize pygame
    pygame.init()
    game_sc = pygame.display.set_mode(GAME_RESOLUTION)
    clock = pygame.time.Clock()
    pygame.display.set_caption("PyTetris")

    exit = False

    # Game Grid
    grid = [pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            for x in range(GAME_WIDTH) for y in range(GAME_HEIGHT)]

    figures = [[pygame.Rect(x + GAME_WIDTH // 2, y + 1, 1, 1)
                for x, y in figures_pos] for figures_pos in figures_position]
    figure_rectangle = pygame.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)

    figure = deepcopy(figures[2])

    # Game Loop
    while not exit:
        # move left and right
        move_right = 0

        game_sc.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_right = -1
                elif event.key == pygame.K_RIGHT:
                    move_right = 1
        # Move x
        figure_old = deepcopy(figure)
        for i in range(len(figure)):
            figure[i].x += move_right
            if not check_borders(figure[i]):
                figure = deepcopy(figure_old)
                break

        # Draw grid for game window
        [pygame.draw.rect(game_sc, (50, 50, 50), i_rect, 1) for i_rect in grid]

        # Move the figure down
        figure_old = deepcopy(figure)
        for i in range(len(figure)):
            if figure[i].y >= GAME_HEIGHT - 1:
                figure = deepcopy(figure_old)
                break
            figure[i].y += 1

        # Draw figures
        for i in range(len(figure)):
            figure_rectangle.x = figure[i].x * TILE_SIZE
            figure_rectangle.y = figure[i].y * TILE_SIZE
            pygame.draw.rect(game_sc, pygame.Color('white'), figure_rectangle)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
