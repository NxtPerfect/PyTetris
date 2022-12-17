import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class block:
    width = 25
    height = 25

    def __init__(self, pos_x=0, pos_y=0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = pygame.rect.Rect(
            self.pos_x, self.pos_y, self.width, self.height)

    def move(self):
        self.rect.move_ip()
        pass


class L_Block(block):
    pass


class I_Block(block):
    pass


class S_Block(block):
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

    test_rect_block = block(0, 0)

    exit = False

    # Game Loop
    while not exit:
        pygame.time.delay(200)

        test_rect = pygame.Rect(test_rect_block.pos_x, test_rect_block.pos_y,
                                test_rect_block.height, test_rect_block.width)

        window.fill(BLACK)
        window.blit(text_surface, (225, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        if test_rect_block.pos_y < 800-test_rect_block.height:
            test_rect_block.pos_y += 25
        else:
            test_rect_block.pos_y = 800-test_rect_block.height
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and test_rect_block.pos_x > 0:
            test_rect_block.pos_x -= 25
        if keys[pygame.K_RIGHT] and test_rect_block.pos_x < 500-test_rect_block.width:
            test_rect_block.pos_x += 25

        pygame.draw.rect(window, (255, 255, 255), test_rect)
        pygame.display.update()


if __name__ == "__main__":
    main()
