import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class block:
    def __init__(self, pos_x, pos_y, width, height):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move_x(self, pos_x):  # Moves to the right, use negative to move to left
        self.pos_x += pos_x

    def move_y(self, pos_y):  # Moves up, use negative to move down
        self.pos_y -= pos_y

    def move(self, pos_x, pos_y):  # Moves up and right, use negative to move down and left
        self.pos_x += pos_x
        self.pos_y -= pos_y


class L_block(block):
    pass


class Square(block):
    pass


class I_block(block):
    pass


class S_block(block):
    pass


def main():
    # Initialize pygame
    pygame.init()

    # Set window size and caption
    window_size = (500, 800)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("PyTetris")
    pygame.font.init()
    score_font = pygame.font.SysFont("Times New Roman", 20)
    text_surface = score_font.render("Score: 0", True, (255, 255, 255))
    window.blit(text_surface, (225, 0))

    test_rect = pygame.Rect(250, 400, 50, 50)

    pygame.draw.rect(window, (255, 255, 255), test_rect)

    exit = False

    # Game Loop
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        pygame.display.update()


if __name__ == "__main__":
    main()
