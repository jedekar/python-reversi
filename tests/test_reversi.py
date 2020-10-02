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

    def test_checkHorizontal(self):
        self.assertEqual(self.game.check_horizontal(28), [26])
        self.assertEqual(self.game.check_horizontal(35), [37])

    def test_checkLeft(self):
        self.assertEqual(self.game.check_left(28), 26)
        self.assertEqual(self.game.check_left(35), None)
        self.game.field[0] = "b"
        self.assertEqual(self.game.check_left(0), None)

    def test_checkRight(self):
        self.assertEqual(self.game.check_right(28), None)
        self.assertEqual(self.game.check_right(35), 37)
        self.game.field[23] = "b"
        self.assertEqual(self.game.check_right(23), None)


if __name__ == '__main__':
    unittest.main()