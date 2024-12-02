import re
from typing import List

# https://adventofcode.com/2024/day/1
class HistorianHysteria:
    def solve(self, puzzle_input: List[str], use_similarity_score=False) -> int:
        left = list()
        right = list()
        right_number_count = dict()
        for value in puzzle_input:
            tokens = re.split("\\s+", value)
            left.append(int(tokens[0]))
            tmp = int(tokens[1])
            right.append(tmp)
            right_number_count[tmp] = right_number_count.get(tmp, 0) + 1

        left.sort()
        right.sort()
        distance = 0
        for l, r in zip(left, right):
            if use_similarity_score:
                distance += l * right_number_count.get(l, 0)
            else:
                distance += abs(l - r)
        return distance
