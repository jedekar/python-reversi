import pygame as pg

from reversi.reversi import FIELD_WIDTH, BLACK, WHITE


def create_piece(radius, color):
    piece = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
    pg.draw.circle(piece, color, (radius, radius), radius - 1)
    return piece


def create_black(radius):
    black = pg.Color(22, 24, 42)
    return create_piece(radius, black)


def create_white(radius):
    white = pg.Color(248, 40, 56)
    return create_piece(radius, white)


class Board(pg.Surface):
    def __init__(self, width, pos):
        super().__init__((width, width))
        self.color = pg.Color(56, 105, 44)
        self.pos = pos
        self.fill(self.color)
        self.black = create_black(width // FIELD_WIDTH // 2)
        self.white = create_white(width // FIELD_WIDTH // 2)

    def update(self, game):
        self.fill(self.color)
        for i in range(FIELD_WIDTH):
            for j in range(FIELD_WIDTH):
                piece = None
                if game.field[i][j] == BLACK:
                    piece = self.black
                if game.field[i][j] == WHITE:
                    piece = self.white
                if piece:
                    self.blit(piece, (j * self.black.get_width(),
                                      i * self.black.get_height()))


class PygameView:
    def __init__(self, window_size=(800, 600)):
        pg.init()

        board_width = min(*window_size) // 1.25
        board_pos = ((window_size[0] - board_width) // 2,
                     (window_size[1] - board_width) // 2)

        self.board = Board(board_width, board_pos)
        self.score = None

        self.color = pg.Color(28, 28, 29)
        self.font = pg.font.Font(pg.font.get_default_font(), int(min(*window_size) // 10 / 1.5))

        self.window_size = window_size
        self.blit_sequence = [(self.board, board_pos)]
        self.screen = pg.display.set_mode(window_size)
        self.screen.fill(self.color)
        pg.display.set_caption("Reversi")

    def pos_to_cell_idx(self, pos):
        cell_size = self.board.get_width() // FIELD_WIDTH
        x = int(pos[0] - self.board.pos[0]) // cell_size
        y = int(pos[1] - self.board.pos[1]) // cell_size
        return y, x

    def add_score(self, game):
        score = game.calculate_score()
        self.score = self.font.render(f"{score[0]} : {score[1]}", True, pg.Color('goldenrod'))
        score_pos = ((self.window_size[0] - self.score.get_width()) // 2, min(*self.window_size) // 60)
        self.blit_sequence.append((self.score, score_pos))

    def update(self, game):
        self.board.update(game)
        self.screen.fill(self.color)
        if (not self.score) and game.is_finished():
            self.add_score(game)
            self.screen.blits(self.blit_sequence)
            self.score = None
            self.blit_sequence = self.blit_sequence[:-1]
        else:
            self.screen.blits(self.blit_sequence)
        pg.display.update()
