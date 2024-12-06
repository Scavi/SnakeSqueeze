import re
from functools import cmp_to_key
from typing import List, Tuple


class PrintQueue:
    def solve(self, puzzle_input: List[str]) -> Tuple[int, int]:
        def compare(a: str, b: str):
            return -1 if f"{a}|{b}" in rules else 0

        def sorted_manuals(manual: List[int]):
            return sorted(manual, key=cmp_to_key(compare))

        split_idx = next(i for i, j in enumerate(puzzle_input) if j == "")
        rules = set(puzzle_input[:split_idx])
        manuals = [
            [int(i) for i in re.findall("\d+", line)]
            for line in puzzle_input[split_idx + 1:]
        ]
        part1 = sum(m[len(m) // 2] for m in manuals if sorted(m, key=cmp_to_key(compare)) == m)
        part2 = sum(m[len(m) // 2] for m in map(sorted_manuals, manuals)) - part1
        return part1, part2
