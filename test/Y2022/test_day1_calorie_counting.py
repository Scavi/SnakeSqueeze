from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2022.Day1CalorieCounting import Day1CalorieCounting


class TestDay1CalorieCounting(TestCase):
    def test_preparation_1(self) -> None:
        calories = [
            "1000",
            "2000",
            "3000",
            "",
            "4000",
            "",
            "5000",
            "6000",
            "",
            "7000",
            "8000",
            "9000",
            "",
            "10000"
        ]
        result = Day1CalorieCounting().solve(calories)
        self.assertEqual(24000, result)

    def test_solve_1(self) -> None:
        calories = FileHelper.read_file(Path("../../Input/2022/Day01.txt"))
        result = Day1CalorieCounting().solve(calories)
        self.assertEqual(69626, result)

    def test_solve_2(self) -> None:
        calories = FileHelper.read_file(Path("../../Input/2022/Day01.txt"))
        result = Day1CalorieCounting().solve(calories, 3)
        self.assertEqual(206780, result)
