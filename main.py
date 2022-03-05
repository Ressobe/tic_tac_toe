from draw_class import Game, pygame

pygame.init()


def main():
    run = True
    clock = pygame.time.Clock()
    player = "x"

    game = Game(600, 600)
    game.draw_window()
    game.draw_lines()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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

    pygame.quit()


if __name__ == "__main__":
    main()
