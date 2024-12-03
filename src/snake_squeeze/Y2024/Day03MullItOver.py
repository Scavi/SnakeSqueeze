import re
from typing import List

class MullItOver:
    @staticmethod
    def solve(dumps: List[str]) -> int:
        return sum([int(num1) * int(num2) for num1, num2 in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", ''.join(dumps))])

    @staticmethod
    def solve2(dumps: List[str]) -> int:
        result = 0
        instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", ''.join(dumps))
        valid = True
        for instruction in instructions:
            if instruction == "do()":
                valid = True
            elif instruction == "don't()":
                valid = False
            elif valid:
                result += sum([int(num1) * int(num2) for num1, num2 in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", instruction)])
        return result
