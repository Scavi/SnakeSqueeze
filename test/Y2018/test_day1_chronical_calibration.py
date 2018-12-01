from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2018.Day1ChronalCalibration import Day1ChronalCalibration


class TestDay1ChronalCalibration(TestCase):
    def test_part_1(self):
        puzzle_input = FileHelper.read_file(Path("../../Input/2018/Day1.txt"))
        chronal_calibration = Day1ChronalCalibration()
        self.assertEquals(454, chronal_calibration.solve1(puzzle_input))


    def test_part_2(self):
        puzzle_input = FileHelper.read_file(Path("../../Input/2018/Day1.txt"))
        chronal_calibration = Day1ChronalCalibration()
        self.assertEquals(566, chronal_calibration.solve2(puzzle_input))
