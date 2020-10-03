import unittest

from reversi.reversi import Reversi


class TestReversi(unittest.TestCase):
    def setUp(self):
        self.game = Reversi()

    def test_flip_row(self):
        self.game.field[4][5] = 'b'
        self.game.flip_row((4, 5), (0, -1))
        self.assertEqual(self.game.field[4][4], 'b')
        self.game.field[5][3] = 'b'
        self.game.field[6][3] = 'w'
        self.game.flip_row((6, 3), (-1, 0))
        self.assertEqual(self.game.field[5][3], 'w')
        self.assertEqual(self.game.field[4][3], 'w')

    def test_get_coverage(self):
        self.assertEqual(self.game.get_coverage('b'),
                         {(2, 3): [(4, 3)],
                          (3, 2): [(3, 4)],
                          (4, 5): [(4, 3)],
                          (5, 4): [(3, 4)]})
        self.game.field[2][2] = 'w'
        self.game.field[2][1] = 'b'
        self.assertEqual(self.game.get_coverage('b'),
                         {(2, 3): [(2, 1), (4, 3)],
                          (3, 2): [(3, 4)],
                          (4, 5): [(4, 3)],
                          (5, 4): [(3, 4)]})


if __name__ == '__main__':
    unittest.main()