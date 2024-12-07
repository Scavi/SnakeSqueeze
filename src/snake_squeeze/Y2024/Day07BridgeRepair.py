import re
from enum import Enum
from typing import List

class Operators(str, Enum):
    PLUS = "+"
    MUL = "*"
    CONCAT = "||"


class BridgeRepair:
    def solve(self, equations: List[str], all_ops: List[Operators]) -> int:
        res = 0
        for equation in equations:
            test, *numbers = [int(i) for i in re.findall(r"\d+", equation)]
            if self._find_calibration(test, numbers, all_ops, 1, numbers[0]):
                res += test
        return res

    def _find_calibration(self, expected: int, numbers: List[int], all_ops: List[Operators], pos: int, calc: int) -> bool:
        if pos == len(numbers):
            return expected == calc
        found_match = False
        for operator in all_ops:
            match operator:
                case '*':
                    found_match = self._find_calibration(expected, numbers, all_ops, pos + 1, calc * numbers[pos])
                case '+':
                    found_match = self._find_calibration(expected, numbers, all_ops, pos + 1, calc + numbers[pos])
                case '||':
                    found_match = self._find_calibration(expected, numbers, all_ops, pos + 1, int(f"{calc}{numbers[pos]}"))
            if found_match:
                return True
        return False
