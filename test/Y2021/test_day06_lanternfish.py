from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2021.Day06Lanternfish import Lanternfish


class TestLanternfish(TestCase):
    def test_preparation_1(self) -> None:
        result = Lanternfish().solve("3,4,3,1,2", 80)
        self.assertEqual(5934, result)

    def test_solve_1(self) -> None:
        data = FileHelper.read_file(Path("../../Input/2021/Day06.txt"))
        result = Lanternfish().solve(data[0], 80)
        self.assertEqual(389726, result)

    def test_solve_2(self) -> None:
        data = FileHelper.read_file(Path("../../Input/2021/Day06.txt"))
        result = Lanternfish().solve(data[0], 256)
        self.assertEqual(1743335992042, result)
