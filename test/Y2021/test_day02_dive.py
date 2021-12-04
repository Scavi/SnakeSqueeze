from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2021.Day02Dive import Dive


class TestDive(TestCase):
    def test_preparation_1(self) -> None:
        data = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
        ]
        spot = Dive(False).solve(data)
        self.assertEqual(150, spot)

    def test_preparation_2(self) -> None:
        data = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
        ]
        spot = Dive(True).solve(data)
        self.assertEqual(900, spot)

    def test_solve_a(self) -> None:
        data = FileHelper.read_file(Path("../../Input/2021/Day02.txt"))
        result = Dive(False).solve(data)
        self.assertEqual(2073315, result)

    def test_solve_b(self) -> None:
        data = FileHelper.read_file(Path("../../Input/2021/Day02.txt"))
        result = Dive(True).solve(data)
        self.assertEqual(1840311528, result)
