from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2022.Day4CampCleanup import Day4CampCleanup


class TestDay4CampCleanup(TestCase):
    def test_preparation_1(self) -> None:
        sections = [
            "2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8"
        ]
        pair_count = Day4CampCleanup().solve(sections)
        self.assertEqual(2, pair_count)

    def test_preparation_2(self) -> None:
        sections = [
            "2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8"
        ]
        pair_count = Day4CampCleanup().solve(sections, True)
        self.assertEqual(4, pair_count)

    def test_solve_1(self) -> None:
        sections = FileHelper.read_file(Path("../../Input/2022/Day04.txt"))
        result = Day4CampCleanup().solve(sections)
        self.assertEqual(471, result)

    def test_solve_2(self) -> None:
        sections = FileHelper.read_file(Path("../../Input/2022/Day04.txt"))
        result = Day4CampCleanup().solve(sections, True)
        self.assertEqual(888, result)
