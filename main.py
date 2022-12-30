'''Make horizontal line that shows the trajectory
border around play zone
unionize Block into other shapes
add score for each line at the bottom'''


import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800


class Block:
    width = 10
    height = 10

    def __init__(self, pos_x=0, pos_y=0):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self, rect: pygame.Rect):
        rect.move_ip()
        pass

    def rotate(self):
        pass


class Cube_Block(Block):
    pass


class L_Block(Block):
    pass


class I_Block(Block):
    pass


class S_Block(Block):
    pass


def main():
    # Initialize pygame
    pygame.init()

    # Set window size and caption
    window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("PyTetris")

    # Initialize score text "Score: 0"
    pygame.font.init()
    font = pygame.font.SysFont("Times New Roman", 20)
    score_text = font.render("Score: 0", True, WHITE)
    text_rect = score_text.get_rect(center=(WINDOW_WIDTH/2, 15))

    exit = False

    placed_blocks = []

    new_block = True

    # Game Loop
    while not exit:
        pygame.time.delay(100)

        # Test the display with a rectangle
        test_rect_block = Block(WINDOW_WIDTH/2, 50)

        while new_block:
            player_block = pygame.Rect(test_rect_block.pos_x, test_rect_block.pos_y,
                                       test_rect_block.height, test_rect_block.width)
            new_block = False

        # Fill background with black and draw score
        window.fill(BLACK)
        window.blit(score_text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        if player_block.y < WINDOW_HEIGHT-10:
            player_block.move_ip(0, 10)
        else:
            player_block.y = WINDOW_HEIGHT-10

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_block.x > 0:
            player_block.move_ip(-10, 0)
        if keys[pygame.K_RIGHT] and player_block.x < WINDOW_WIDTH-10:
            player_block.move_ip(10, 0)

        for block in placed_blocks:
            if not block.x == player_block.x:
                pass
            if block.y == player_block.y+10:
                placed_blocks.append(player_block)  # TODO: Function this
                new_block = True

        if (not new_block) and player_block.y == WINDOW_HEIGHT-10:  # TODO: unnested if
            placed_blocks.append(player_block)  # TODO: New function
            new_block = True

        for block in placed_blocks:
            pygame.draw.rect(window, (255, 0, 0), block)

        pygame.draw.rect(window, (255, 255, 255), player_block)
        pygame.display.update()


if __name__ == "__main__":
    main()
