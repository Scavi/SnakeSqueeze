from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2021.Day03BinaryDiagnostic import BinaryDiagnostic


class TestBinaryDiagnostic(TestCase):

    def test_preparation_1(self) -> None:
        data = ["00100", "11110", "10110", "10111", "10101", "01111",
                "00111", "11100", "10000", "11001", "00010", "01010"]
        self.assertEqual(198, BinaryDiagnostic().determine_power_consumption(data))

    def test_preparation_2(self) -> None:
        data = ["00100", "11110", "10110", "10111", "10101", "01111",
                "00111", "11100", "10000", "11001", "00010", "01010"]
        self.assertEqual(230, BinaryDiagnostic().determine_life_supply(data))

    def test_solve_a(self) -> None:
        data = FileHelper.read_file(Path("../../Input/2021/Day03.txt"))
        result = BinaryDiagnostic().determine_power_consumption(data)
        #
        self.assertEqual(3912944, result)

    def test_solve_b(self) -> None:
        data = FileHelper.read_file(Path("../../Input/2021/Day03.txt"))
        result = BinaryDiagnostic().determine_life_supply(data)
        self.assertEqual(4996233, result)
