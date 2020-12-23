import random
import pygame as pg

from reversi.reversi import WHITE, BLACK

PASS = 'pass'
RESTART = 'restart'

LETTERS = 'abcdefgh'
NUMBERS = '12345678'


class HumanController:
    def __init__(self, color, view):
        self.color = color
        self.view = view

    def get_input(self, game):
        coverage = game.get_coverage(self.color)
        while True:
            events = pg.event.get()

            for e in events:
                if e.type == pg.MOUSEBUTTONDOWN:
                    move = self.view.pos_to_cell_idx(e.pos)
                    if move in coverage.keys():
                        return move
                elif e.type == pg.QUIT:
                    quit(0)
                elif e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                    quit(0)
                elif e.type == pg.KEYDOWN and e.key == pg.K_r:
                    return RESTART
                elif e.type == pg.KEYDOWN and e.key == pg.K_SPACE and len(coverage) == 0:
                    return PASS


class BotController:
    def __init__(self, color):
        self.color = color

    def get_input(self, game):
        pg.time.wait(470)
        coverage = game.get_coverage(self.color)
        if len(coverage) != 0:
            return random.choice(list(coverage.keys()))
        else:
            return PASS


def prepare(view):
    return HumanController(BLACK, view), BotController(WHITE)
