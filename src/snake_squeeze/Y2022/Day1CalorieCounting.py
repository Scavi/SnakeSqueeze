from itertools import groupby
from typing import List


class Day1CalorieCounting:
    @staticmethod
    def solve(calories: List[str], top_n=1) -> int:
        """
        https://adventofcode.com/2022/day/1

        Args:
            calories: A list with calories for all elfs grouped by empty lines
            top_n: The top n elfs to determine

        Returns:
            The sum of calories from the top n elfs
        """
        grouped_calories = [list(calorie) for _, calorie in groupby(calories, lambda calorie: calorie == "")]
        return sum(sorted([sum(map(int, elf)) for elf in grouped_calories if elf[0]], reverse=True)[0:top_n])
