from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2024.Day03MullItOver import MullItOver

# https://adventofcode.com/2024/day/3
class TestMullItOver(TestCase):
    def test_preparation_1(self) -> None:
        dump = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
        mull_it_over = MullItOver()
        result = mull_it_over.solve(dump)
        self.assertEqual(161, result)

    def test_preparation_2(self) -> None:
        dump = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
        mull_it_over = MullItOver()
        result = mull_it_over.solve2(dump)
        self.assertEqual(48, result)

    def test_solve_1(self) -> None:
        dumps = FileHelper.read_file(Path("../../Input/2024/Day03.txt"))
        mull_it_over = MullItOver()
        result = mull_it_over.solve(dumps)
        self.assertEqual(173517243, result)

    def test_solve_2(self) -> None:
        dumps = FileHelper.read_file(Path("../../Input/2024/Day03.txt"))
        mull_it_over = MullItOver()
        result = mull_it_over.solve2(dumps)
        self.assertEqual(100450138, result)
