from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2022.Day8TreetopTreeHouse import Day8TreetopTreeHouse


class TestDay8TreetopTreeHouse(TestCase):
    def test_preparation_1(self) -> None:
        trees = [
            "30373",
            "25512",
            "65332",
            "33549",
            "35390",
        ]
        visible_trees = Day8TreetopTreeHouse().solve_1(trees)
        self.assertEqual(21, visible_trees)

    def test_preparation_2(self) -> None:
        trees = [
            "30373",
            "25512",
            "65332",
            "33549",
            "35390",
        ]
        visible_trees = Day8TreetopTreeHouse().solve_2(trees)
        self.assertEqual(8, visible_trees)

    def test_solve_1(self) -> None:
        trees = FileHelper.read_file(Path("../../Input/2022/Day08.txt"))
        processed = Day8TreetopTreeHouse().solve_1(trees)
        self.assertEqual(1733, processed)

    def test_solve_2(self) -> None:
        trees = FileHelper.read_file(Path("../../Input/2022/Day08.txt"))
        processed = Day8TreetopTreeHouse().solve_2(trees)
        self.assertEqual(284648, processed)
