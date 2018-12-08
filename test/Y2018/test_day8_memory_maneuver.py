from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2018.Day8MemoryManeuver import Day8MemoryManeuver


class TestDay8MemoryManeuver(TestCase):
    def test_preparation_1(self):
        license_input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        meta = Day8MemoryManeuver().solve(license_input)
        self.assertEqual(138, meta)

    def test_preparation_2(self):
        license_input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        meta = Day8MemoryManeuver(True).solve(license_input)
        self.assertEqual(66, meta)

    def test_part_1(self):
        license_input = FileHelper.read_file(Path("../../Input/2018/Day8.txt"))
        step_order = Day8MemoryManeuver().solve(license_input[0])
        self.assertEqual(48155, step_order)

    def test_part_2(self):
        license_input = FileHelper.read_file(Path("../../Input/2018/Day8.txt"))
        step_order = Day8MemoryManeuver(True).solve(license_input[0])
        self.assertEqual(40292, step_order)
