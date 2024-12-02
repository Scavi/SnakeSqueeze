from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2024.Day01HistorianHysteria import HistorianHysteria


class TestHistorianHysteria(TestCase):
    def test_preparation_1(self) -> None:
        distance = HistorianHysteria().solve(self._get_puzzle_test_input())
        self.assertEqual(11, distance)

    def test_preparation_2(self) -> None:
        distance = HistorianHysteria().solve(
            self._get_puzzle_test_input(),
            use_similarity_score=True)
        self.assertEqual(31, distance)

    def test_solve_1(self) -> None:
        puzzle_input = FileHelper.read_file(Path("../../Input/2024/Day01.txt"))
        distance = HistorianHysteria().solve(puzzle_input)
        self.assertEqual(1765812, distance)

    def test_solve_2(self) -> None:
        puzzle_input = FileHelper.read_file(Path("../../Input/2024/Day01.txt"))
        distance = HistorianHysteria().solve(puzzle_input, use_similarity_score=True)
        self.assertEqual(20520794, distance)

    @staticmethod
    def _get_puzzle_test_input() -> list[str]:
        return [
            "3   4",
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3",
        ]
