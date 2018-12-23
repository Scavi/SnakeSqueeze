from unittest import TestCase

from snake_squeeze.Y2018.Day22ModeMaze import Day22ModeMaze


class TestDay22ModeMaze(TestCase):
    def test_prepare_1(self):
        mode_maze = Day22ModeMaze(510)
        risk_level = mode_maze.solve_1((10, 10))
        self.assertEqual(114, risk_level)


    def test_solve_1(self):
        mode_maze = Day22ModeMaze(7305)
        risk_level = mode_maze.solve_1((13, 734))
        self.assertEqual(10204, risk_level)
