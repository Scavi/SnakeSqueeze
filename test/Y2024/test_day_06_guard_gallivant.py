from pathlib import Path
from typing import List
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2024.Day06GuardGallivant import GuardGallivant


class TestGuardGallivant(TestCase):
    def test_preparation_1(self) -> None:
        guard_gallivant = GuardGallivant()
        distinct_positions = guard_gallivant.solve(self._create_map())
        self.assertEqual(41, distinct_positions[0])

    def test_solve_1(self) -> None:
        map_input = FileHelper.read_file(Path("../../Input/2024/Day06.txt"))
        guard_gallivant = GuardGallivant()
        distinct_positions = guard_gallivant.solve(map_input)
        self.assertEqual(5079, distinct_positions[0])

    def test_preparation_2(self) -> None:
        guard_gallivant = GuardGallivant()
        distinct_positions = guard_gallivant.solve(self._create_map())
        self.assertEqual(6, distinct_positions[1])

    def test_solve_2(self) -> None:
        map_input = FileHelper.read_file(Path("../../Input/2024/Day06.txt"))
        guard_gallivant = GuardGallivant()
        distinct_positions = guard_gallivant.solve(map_input)
        self.assertEqual(1919, distinct_positions[1])

    @staticmethod
    def _create_map() -> List[str]:
        return [
            "....#.....",
            ".........#",
            "..........",
            "..#.......",
            ".......#..",
            "..........",
            ".#..^.....",
            "........#.",
            "#.........",
            "......#..."
        ]
