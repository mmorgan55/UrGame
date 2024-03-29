import pygame
import sys
import constants as const
import tile
import player_piece as pp


def main():
    board = make_board(const.BOARD)
    print_board(board)
    test_board(board)
    print_board(board)
    move_piece(3, 0, board, 1)
    print_board(board)
    move_piece(2, 0, board, 4)
    print_board(board)
    test_board(board)
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
    for line in lines:
        row = list(line)

        ts = []
        for char in row:

            if char == "T":
                ts.append(tile.GameTile())

        game_tiles.append(ts)

    return game_tiles


def print_board(board):
    for row in board:
        if len(row) == 1:
            for t in row:
                print(". " + str(t) + " .", end="")
        else:
            for t in row:
                print(str(t) + " ", end="")
        print()
    print()


def test_board(board):
    piece = pp.PlayerPiece(0)
    place_piece(piece, board)


def place_piece(piece, board):
    board[piece.row][piece.col].put_piece(piece)


def move_piece(row, col, board, num):
    piece = board[row][col].remove_piece()
    piece.move(num)
    place_piece(piece, board)


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
