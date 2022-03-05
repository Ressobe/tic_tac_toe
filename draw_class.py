import pygame


class Game:
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

    BOARD = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))

        self.board_width = self.width // 3 - self.MARGIN
        self.board_height = self.height // 3 - self.MARGIN

        self.x = self.board_width // 2
        self.y = self.board_height // 2

        self.BOARD_POSITIONS = [
            [
                (
                    self.x,
                    self.y,
                ),
                (self.x + self.board_width + self.MARGIN + self.PADDING, self.y),
                (
                    self.x + ((self.board_width + self.MARGIN + self.PADDING) * 2),
                    self.y,
                ),
            ],
            [
                (
                    self.x,
                    self.y + self.board_height + self.MARGIN + self.PADDING,
                ),
                (
                    self.x + self.board_width + self.MARGIN + self.PADDING,
                    self.y + self.board_height + self.MARGIN + self.PADDING,
                ),
                (
                    self.x + ((self.board_width + self.MARGIN + self.PADDING) * 2),
                    self.y + self.board_height + self.MARGIN + self.PADDING,
                ),
            ],
            [
                (
                    self.x,
                    self.y + (self.board_height + self.MARGIN + self.PADDING) * 2,
                ),
                (
                    self.x + self.board_width + self.MARGIN + self.PADDING,
                    self.y + ((self.board_height + self.MARGIN + self.PADDING) * 2),
                ),
                (
                    self.x + ((self.board_width + self.MARGIN + self.PADDING) * 2),
                    self.y + ((self.board_height + self.MARGIN + self.PADDING) * 2),
                ),
            ],
        ]

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

    def start(self):
        self.draw_window()
        self.draw_lines()

    def draw_circle(self, row, col):
        self.row = row
        self.col = col

        circle = pygame.image.load("circle.png").convert_alpha()
        circle_rect = circle.get_rect()

        circle_rect.center = (
            self.BOARD_POSITIONS[row][col][0],
            self.BOARD_POSITIONS[row][col][1],
        )

        self.window.blit(circle, circle_rect)
        pygame.display.flip()

    def draw_cross(self, row, col):
        self.row = row
        self.col = col

        cross = pygame.image.load("cross.png").convert_alpha()
        cross_rect = cross.get_rect()

        cross_rect.center = (
            self.BOARD_POSITIONS[row][col][0],
            self.BOARD_POSITIONS[row][col][1],
        )

        self.window.blit(cross, cross_rect)
        pygame.display.flip()

    def change_board(self, row, col, player):
        self.BOARD[row][col] = player
        print(self.BOARD)

    def check_board(self, row, col):
        if self.BOARD[row][col] != 0:
            return False
        return True

    def check_win(self):
        cross_win = ["x", "x", "x"]
        circle_win = ["o", "o", "o"]

        for i in range(0, 3):
            if self.BOARD[i] == cross_win or self.BOARD == circle_win:
                return True

            column = []
            for j in range(0, 3):
                column.append(self.BOARD[j][i])

            if column == cross_win or column == circle_win:
                return True

        diagonal_1 = [self.BOARD[i][i] for i in range(0, 3)]
        if diagonal_1 == cross_win or diagonal_1 == circle_win:
            return True

        diagonal_2 = []
        for i in range(2, -1, -1):
            diagonal_2.append(self.BOARD[i][abs(i - 2)])

        if diagonal_2 == cross_win or diagonal_2 == circle_win:
            return True

        return False
