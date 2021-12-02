from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2021.Day01SonarSweep import SonarSweep


class TestSonarSweep(TestCase):
    def test_preparation_1(self) -> None:
        data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        result = SonarSweep().solve(data, 1)
        self.assertEqual(7, result)

    def test_preparation_2(self) -> None:
        data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        result = SonarSweep().solve(data, 3)
        self.assertEqual(5, result)

    def test_solve_a(self) -> None:
        data = FileHelper.read_file_as_int(Path("../../Input/2021/Day1.txt"))
        result = SonarSweep().solve(data, 1)
        self.assertEqual(1466, result)

    def test_solve_b(self) -> None:
        data = FileHelper.read_file_as_int(Path("../../Input/2021/Day1.txt"))
        result = SonarSweep().solve(data, 3)
        self.assertEqual(1491, result)
