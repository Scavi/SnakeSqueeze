from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2022.Day6TuningTrouble import Day6TuningTrouble


class TestDay6TuningTrouble(TestCase):
    def test_preparation_1(self) -> None:
        processed = Day6TuningTrouble().solve("bvwbjplbgvbhsrlpgdmjqwftvncz", 4)
        self.assertEqual(5, processed)

    def test_solve_1(self) -> None:
        signal = FileHelper.read_file(Path("../../Input/2022/Day06.txt"))
        processed = Day6TuningTrouble().solve(signal[0], 4)
        self.assertEqual(1929, processed)

    def test_solve_2(self) -> None:
        signal = FileHelper.read_file(Path("../../Input/2022/Day06.txt"))
        processed = Day6TuningTrouble().solve(signal[0], 14)
        self.assertEqual(3298, processed)
