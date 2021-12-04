from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2021.Day04GiantSquid import GiantSquid


class TestGiantSquid(TestCase):
    def test_preparation_1(self) -> None:
        bingo_data = FileHelper.read_file(Path("../../Input/2021/Day04_1.txt"))
        self.assertEqual(4512, GiantSquid(bingo_data).solve(bingo_data[0].split(",")))

    def test_solve_1(self) -> None:
        bingo_data = FileHelper.read_file(Path("../../Input/2021/Day04_2.txt"))
        self.assertEqual(22680, GiantSquid(bingo_data).solve(bingo_data[0].split(",")))

    def test_preparation_2(self) -> None:
        bingo_data = FileHelper.read_file(Path("../../Input/2021/Day04_1.txt"))
        self.assertEqual(1924, GiantSquid(bingo_data, True).solve(bingo_data[0].split(",")))

    def test_solve_2(self) -> None:
        bingo_data = FileHelper.read_file(Path("../../Input/2021/Day04_2.txt"))
        self.assertEqual(16168, GiantSquid(bingo_data, True).solve(bingo_data[0].split(",")))
