from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2018.Day3NoMatterHowYouSliceIt import Day3NoMatterHowYouSliceIt


class TestDay3NoMatterHowYouSliceIt(TestCase):

    def test_preparation_1(self):
        claims = [
            "# 1 @ 1,3: 4x4",
            "# 2 @ 3,1: 4x4",
            "# 3 @ 5,5: 2x2"]
        claim_overlap = Day3NoMatterHowYouSliceIt().solve1(claims)
        self.assertEqual(4, claim_overlap)

    def test_preparation_2(self):
        claims = [
            "# 1 @ 1,3: 4x4",
            "# 2 @ 3,1: 4x4",
            "# 3 @ 5,5: 2x2"]
        claim_overlap = Day3NoMatterHowYouSliceIt().solve2(claims)
        self.assertEqual(3, claim_overlap)

    def test_part_1(self):
        claims = FileHelper.read_file(Path("../../Input/2018/Day3.txt"))
        claim_overlap = Day3NoMatterHowYouSliceIt(1000).solve1(claims)
        self.assertEqual(110827, claim_overlap)

    def test_part_2(self):
        claims = FileHelper.read_file(Path("../../Input/2018/Day3.txt"))
        claim_overlap = Day3NoMatterHowYouSliceIt(1000).solve2(claims)
        self.assertEqual(116, claim_overlap)
