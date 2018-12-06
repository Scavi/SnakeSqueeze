from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2018.Day5AlchemicalReduction import Day5AlchemicalReduction


class TestDay5AlchemicalReduction(TestCase):
    def test_preparation_1(self):
        test = "dabAcCaCBAcCcaDA"
        output_len = Day5AlchemicalReduction().solve1(test)
        self.assertEqual(10, output_len)

    def test_preparation_2(self):
        test = "dabAcCaCBAcCcaDA"
        output_len = Day5AlchemicalReduction().solve2(test)
        self.assertEqual(4, output_len)

    def test_part_1(self):
        test = FileHelper.read_file(Path("../../Input/2018/Day5.txt"))
        output_len = Day5AlchemicalReduction().solve1(test[0])
        self.assertEqual(9704, output_len)

    def test_part_2(self):
        test = FileHelper.read_file(Path("../../Input/2018/Day5.txt"))
        output_len = Day5AlchemicalReduction().solve2(test[0])
        self.assertEqual(6942, output_len)
