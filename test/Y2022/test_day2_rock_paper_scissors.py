from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2022.Day2RockPaperScissors import Day2RockPaperScissors


class TestDay2RockPaperScissors(TestCase):
    def test_preparation_1(self) -> None:
        strategies = ["A Y", "B X", "C Z"]
        score = Day2RockPaperScissors().solve(strategies)
        self.assertEqual(15, score)

    def test_preparation_2(self) -> None:
        strategies = ["A Y", "B X", "C Z"]
        score = Day2RockPaperScissors().solve(strategies, True)
        self.assertEqual(12, score)

    def test_solve_1(self) -> None:
        strategies = FileHelper.read_file(Path("../../Input/2022/Day02.txt"))
        result = Day2RockPaperScissors().solve(strategies)
        self.assertEqual(15572, result)

    def test_solve_2(self) -> None:
        strategies = FileHelper.read_file(Path("../../Input/2022/Day02.txt"))
        result = Day2RockPaperScissors().solve(strategies, True)
        self.assertEqual(16098, result)
