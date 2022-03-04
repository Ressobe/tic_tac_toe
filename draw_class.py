import pygame


class Draw:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    BACKGROUND = (0, 109, 119)

    LINE_COLOR = (23, 145, 135)
    LINE_WIDTH = 10

    CIRCLE_COLOR = (239, 231, 200)
    CROSS_COLOR = (66, 66, 66)
    CIRCLE_RADIUS = 60
    CIRCLE_WIDTH = 15

    PADDING = 10
    MARGIN = 20

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        self.board_width = self.width // 3 - self.MARGIN
        self.board_height = self.height // 3 - self.MARGIN

        pygame.display.set_caption("Tic Tac Toe")

    def draw_window(self):
        self.window.fill(self.BACKGROUND)
        pygame.display.update()

    def draw_lines(self):
        pygame.draw.line(
            self.window,
            self.BLACK,
            (0, self.board_height + self.MARGIN),
            (self.width, self.board_height + self.MARGIN),
            self.LINE_WIDTH,
        )
        pygame.draw.line(
            self.window,
            self.BLACK,
            (0, (self.board_height + self.MARGIN) * 2),
            (self.width, (self.board_height + self.MARGIN) * 2),
            self.LINE_WIDTH,
        )

        pygame.draw.line(
            self.window,
            self.BLACK,
            (self.board_width + self.MARGIN, 0),
            (self.board_width + self.MARGIN, self.height),
            self.LINE_WIDTH,
        )
        pygame.draw.line(
            self.window,
            self.BLACK,
            ((self.board_width + self.MARGIN) * 2, 0),
            ((self.board_width + self.MARGIN) * 2, self.height),
            self.LINE_WIDTH,
        )

        pygame.display.flip()
