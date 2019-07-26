import pygame
import sys
import constants as const
import tile


def main():
    board = make_board(const.BOARD)
    print_board(board)

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

    game_tiles = []
    ts = []
    for line in lines:
        row = list(line)

        ts = []
        for char in row:

            if char == "T":
                ts.append(tile.GameTile())
            else:
                ts.append(tile.Tile())
        game_tiles.append(ts)

    return game_tiles


def print_board(board):
    for row in board:
        for t in row:
            print(t, end="")
        print()


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
