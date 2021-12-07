from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2021.Day07TheTreacheryOfWhales import TheTreacheryOfWhales


class TestTheTreacheryOfWhales(TestCase):
    def test_preparation_1(self) -> None:
        result = TheTreacheryOfWhales().solve("16,1,2,0,4,2,7,1,2,14")
        self.assertEqual(37, result)

    def test_solve_1(self) -> None:
        data = FileHelper.read_file(Path("../../Input/2021/Day07.txt"))
        result = TheTreacheryOfWhales().solve(data[0])
        self.assertEqual(340056, result)

    def test_preparation_2(self) -> None:
        result = TheTreacheryOfWhales().solve("16,1,2,0,4,2,7,1,2,14", True)
        self.assertEqual(168, result)

    def test_solve_2(self) -> None:
        data = FileHelper.read_file(Path("../../Input/2021/Day07.txt"))
        result = TheTreacheryOfWhales().solve(data[0], True)
        self.assertEqual(96592275, result)
