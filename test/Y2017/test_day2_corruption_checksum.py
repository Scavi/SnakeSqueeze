from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2017.Day2CorruptionChecksum import Day2CorruptionChecksum


class TestDay2CorruptionChecksum(TestCase):

    def test_1(self):
        corruption_checksum = Day2CorruptionChecksum()
        puzzle_input = FileHelper.read_file(Path("../../Input/2017/Day2.txt"))
        result = corruption_checksum.solve_a(puzzle_input)
        self.assertEquals(42299, result)


    def test_1(self):
        corruption_checksum = Day2CorruptionChecksum()
        puzzle_input = FileHelper.read_file(Path("../../Input/2017/Day2.txt"))
        result = corruption_checksum.solve_b(puzzle_input)
        self.assertEquals(277, result)
