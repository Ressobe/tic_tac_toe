from draw_class import Game, pygame
from time import sleep


pygame.init()


def main():
    font = pygame.font.SysFont("Monospace", 24)

    run = True
    pause = False
    player = "x"
    winner = None

    game = Game(600, 600)
    clock = pygame.time.Clock()
    game.start()

    while True:
        clock.tick(60)

        if run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        row = pos[1] // (game.width // 3)
                        col = pos[0] // (game.width // 3)

                        if game.check_board(row, col):

                            if player == "x":
                                game.draw_cross(row, col)
                                game.change_board(row, col, player)
                                player = "o"

                            elif player:
                                game.draw_circle(row, col)
                                game.change_board(row, col, player)
                                player = "x"

                            if game.check_space() == 9:
                                run = False

                            if game.check_win():
                                winner = None
                                if player == "o":
                                    winner = "x"
                                else:
                                    winner = "o"

                                run = False
                                pause = True
                                sleep(2)
                                game.draw_window()

        if pause:
            img = font.render(f"Winner: {winner}", True, (255, 255, 255))
            img2 = font.render("Press 'R' to restart", True, (255, 255, 255))
            rect = img.get_rect()
            rect2 = img2.get_rect()
            rect.center = (300, 300)
            rect2.center = (300, 400)

            pygame.draw.rect(img, (255, 0, 0), rect, 1)
            pygame.draw.rect(img2, (255, 0, 0), rect, 1)

            game.window.blit(img, rect)
            game.window.blit(img2, rect2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.reset_board()
                        pause = False
                        run = True
                        game.start()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
