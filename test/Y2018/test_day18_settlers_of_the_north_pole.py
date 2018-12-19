from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2018.Day18SettlersOfTheNorthPole import Day18SettlersOfTheNorthPole


class TestDay18SettlersOfTheNorthPole(TestCase):

    def test_preparation_1(self):
        acres = [".#.#...|#.",
                 ".....#|##|",
                 ".|..|...#.",
                 "..|#.....#",
                 "#.#|||#|#|",
                 "...#.||...",
                 ".|....|...",
                 "||...#|.#|",
                 "|.||||..|.",
                 "...#.|..|."]
        north_pole_acres = Day18SettlersOfTheNorthPole()
        resources = north_pole_acres.solve(acres)
        self.assertEqual(1147, resources)


    def test_solve_1(self):
        acres = FileHelper.read_file(Path("../../Input/2018/Day18.txt"))
        north_pole_acres = Day18SettlersOfTheNorthPole()
        resources = north_pole_acres.solve(acres)
        self.assertEqual(515496, resources)


    def test_solve_2(self):
        acres = FileHelper.read_file(Path("../../Input/2018/Day18.txt"))
        north_pole_acres = Day18SettlersOfTheNorthPole(1000000000)
        resources = north_pole_acres.solve(acres)
        self.assertEqual(233058, resources)
