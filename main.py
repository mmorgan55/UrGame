import pygame
import sys
import constants as const


def main():
    make_board(const.BOARD)
    # board = make_board(const.BOARD)
    # window = initialize()
    # game_loop(window, board)


def initialize():
    pygame.init()
    window = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    return window


def make_board(board_file):
    with open(board_file, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]

    board = []
    for line in lines:
        row = list(line)
        board.append(row)

    return board


def game_loop(window, board):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        draw(window, board)
        pygame.display.update()


def draw(window, board):
    for row, tiles in enumerate(board):
        for col, tile in enumerate(tiles):

            if tile == '.':
                color = const.TILE_COLOR
                rect = pygame.Rect(col * const.TILE_WIDTH, row * const.TILE_HEIGHT, const.TILE_WIDTH, const.TILE_HEIGHT)
                pygame.draw.rect(window, color, rect)

            else:
                color1 = (0, 0, 0)
                color2 = const.BOARD_TILE_COLOR

                rect1 = pygame.Rect(col * const.TILE_WIDTH, row * const.TILE_HEIGHT, const.TILE_WIDTH,
                                    const.TILE_HEIGHT)
                rect2 = pygame.Rect(col * const.TILE_WIDTH + 1, row * const.TILE_HEIGHT + 1, const.TILE_WIDTH - 2,
                                    const.TILE_HEIGHT - 2)
                pygame.draw.rect(window, color1, rect1)
                pygame.draw.rect(window, color2, rect2)


if __name__ == '__main__':
    main()
