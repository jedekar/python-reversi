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

    def test_checkVertical(self):
        self.assertEqual(self.game.check_vertical(35), [19])
        self.assertEqual(self.game.check_vertical(28), [44])

    def test_checkUp(self):
        self.assertEqual(self.game.check_up(35), 19)
        self.assertEqual(self.game.check_up(28), None)
        self.assertEqual(self.game.check_up(27), None)
        self.assertEqual(self.game.check_up(36), 20)

    def test_checkDown(self):
        self.assertEqual(self.game.check_down(35), None)
        self.assertEqual(self.game.check_down(28), 44)
        self.assertEqual(self.game.check_down(27), 43)
        self.assertEqual(self.game.check_down(36), None)


class TestPlayer(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()