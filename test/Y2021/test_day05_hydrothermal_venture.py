from pathlib import Path
from typing import List
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2021.Day05HydrothermalVenture import HydrothermalVenture


class TestHydrothermalVenture(TestCase):
    def test_preparation_1(self) -> None:
        result = HydrothermalVenture().solve(self._create_input())
        self.assertEqual(5, result)

    def test_solve_1(self) -> None:
        data = FileHelper.read_file(Path("../../Input/2021/Day05.txt"))
        result = HydrothermalVenture().solve(data)
        self.assertEqual(4993, result)

    def test_solve_2(self) -> None:
        data = FileHelper.read_file(Path("../../Input/2021/Day05.txt"))
        result = HydrothermalVenture(True).solve(data)
        self.assertEqual(21101, result)

    @staticmethod
    def _create_input() -> List[str]:
        return ["0,9 -> 5,9",
                "8,0 -> 0,8",
                "9,4 -> 3,4",
                "2,2 -> 2,1",
                "7,0 -> 7,4",
                "6,4 -> 2,0",
                "0,9 -> 2,9",
                "3,4 -> 1,4",
                "0,0 -> 8,8",
                "5,5 -> 8,2"]
