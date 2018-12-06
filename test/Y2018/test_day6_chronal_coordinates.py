from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2018.Day6ChronalCoordinates import Day6ChronalCoordinates


class TestDay6ChronalCoordinates(TestCase):
    def test_preparation_1(self):
        coordinates = ["1, 1",
                       "1, 6",
                       "8, 3",
                       "3, 4",
                       "5, 5",
                       "8, 9"]
        largest_area = Day6ChronalCoordinates(coordinates).solve1()
        self.assertEqual(17, largest_area)

    def test_preparation_2(self):
        coordinates = ["1, 1",
                       "1, 6",
                       "8, 3",
                       "3, 4",
                       "5, 5",
                       "8, 9"]
        largest_area = Day6ChronalCoordinates(coordinates, 32).solve2()
        self.assertEqual(16, largest_area)

    def test_part_1(self):
        coordinates = FileHelper.read_file(Path("../../Input/2018/Day6.txt"))
        largest_area = Day6ChronalCoordinates(coordinates).solve1()
        self.assertEqual(5532, largest_area)

    def test_part_2(self):
        coordinates = FileHelper.read_file(Path("../../Input/2018/Day6.txt"))
        largest_area = Day6ChronalCoordinates(coordinates, 10000).solve2()
        self.assertEqual(36216, largest_area)
