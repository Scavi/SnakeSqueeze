from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2022.Day3RucksackReorganization import Day3RucksackReorganization


class TestDay3RucksackReorganization(TestCase):
    def test_preparation_1(self) -> None:
        rucksacks = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ]
        result = Day3RucksackReorganization().solve_1(rucksacks)
        self.assertEqual(157, result)

    def test_preparation_2(self) -> None:
        rucksacks = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ]
        result = Day3RucksackReorganization().solve_2(rucksacks)
        self.assertEqual(70, result)

    def test_solve_1(self) -> None:
        rucksacks = FileHelper.read_file(Path("../../Input/2022/Day03.txt"))
        result = Day3RucksackReorganization().solve_1(rucksacks)
        self.assertEqual(7872, result)

    def test_solve_2(self) -> None:
        rucksacks = FileHelper.read_file(Path("../../Input/2022/Day03.txt"))
        result = Day3RucksackReorganization().solve_2(rucksacks)
        self.assertEqual(2497, result)
