from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2022.Day5SupplyStacks import Day5SupplyStacks


class TestDay5SupplyStacks(TestCase):
    def test_preparation_1(self) -> None:
        instructions = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2"
        ]
        crates_on_top = Day5SupplyStacks().solve(instructions)
        self.assertEqual("CMZ", crates_on_top)

    def test_preparation_2(self) -> None:
        instructions = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2"
        ]
        crates_on_top = Day5SupplyStacks().solve(instructions, move_at_once=True)
        self.assertEqual("MCD", crates_on_top)

    def test_solve_1(self) -> None:
        instructions = FileHelper.read_file(Path("../../Input/2022/Day05.txt"))
        crates_on_top = Day5SupplyStacks().solve(instructions)
        self.assertEqual("JDTMRWCQJ", crates_on_top)

    def test_solve_2(self) -> None:
        instructions = FileHelper.read_file(Path("../../Input/2022/Day05.txt"))
        crates_on_top = Day5SupplyStacks().solve(instructions, move_at_once=True)
        self.assertEqual("VHJDDCWRD", crates_on_top)
