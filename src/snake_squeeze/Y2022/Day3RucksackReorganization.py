from itertools import zip_longest
from typing import List
from collections import Counter


class Day3RucksackReorganization:
    def solve_1(self, rucksacks: List[str]) -> int:
        priorities = 0
        for rucksack in rucksacks:
            compartment_1, compartment_2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
            priorities += sum([self.priority_of(item) for item in set(compartment_1).intersection(set(compartment_2))])
        return priorities

    def solve_2(self, rucksacks: List[str]) -> int:
        priorities = 0
        for group in zip_longest(*[iter(rucksacks)] * 3):
            counter = Counter(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))
            priorities += sum([self.priority_of(k) for k, v in counter.items() if v == 1])
        return priorities

    @staticmethod
    def priority_of(item: chr) -> int:
        return ord(item) - 96 if 97 <= ord(item) <= 122 else ord(item) - 38
