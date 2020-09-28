import unittest

from reversi.reversi import Reversi


class TestReversi(unittest.TestCase):
    def setUp(self):
        self.game = Reversi()

    def test_gameStarted_isNotFinished(self):
        self.assertEqual(self.game.free_cells, 60)
        self.assertFalse(self.game.is_finished)

    def test_afterFirstTurn_fiftyNineCells(self):
        self.game.turn()
        self.assertEqual(self.game.free_cells, 59)


class TestPlayer(unittest.TestCase):
    pass
if __name__ == '__main__':
    unittest.main()