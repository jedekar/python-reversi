import unittest

from reversi.reversi import Reversi


class TestReversi(unittest.TestCase):
    def setUp(self):
        self.game = Reversi()

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