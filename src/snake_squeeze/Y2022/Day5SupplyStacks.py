import re
from collections import deque
from typing import List, Deque


class Day5SupplyStacks:
    def solve(self, instructions: List[str], move_at_once=False) -> str:
        idx = instructions.index("")
        stacks = self._create_stack(instructions[0:idx - 1], len(re.findall(r"(\d+)", instructions[idx - 1])))
        for instruction in instructions[idx + 1:]:
            count, move_from, move_to = map(int, re.findall(r"(\d+)", instruction))
            tmp = []
            [tmp.extend(stacks[move_from - 1].pop()) for _ in range(count)]
            tmp.reverse() if move_at_once else tmp
            stacks[move_to - 1].extend(tmp)
        return "".join([s.pop() for s in stacks])

    @staticmethod
    def _create_stack(instructions: List[str], stack_count: int) -> List[Deque]:
        stacks = [deque() for _ in range(stack_count)]
        for instruction in instructions:
            data = [instruction[i:i + 4] for i in range(0, len(instruction), 4)]
            [stacks[i].insert(0, re.findall(r"\w+", data[i])) for i in range(len(data)) if data[i].strip()]
        return stacks
