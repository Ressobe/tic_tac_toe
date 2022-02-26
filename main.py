from draw_class import Draw, pygame

pygame.init()


def main():
    board = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]

    run = True
    clock = pygame.time.Clock()
    window = Draw(600, 600)

    window.draw_window()
    window.draw_lines()
    window.draw_cross()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    row = pos[1] // (window.width // 3)
                    col = pos[0] // (window.width // 3)

    pygame.quit()


if __name__ == "__main__":
    main()
