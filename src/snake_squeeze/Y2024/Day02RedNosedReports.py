from typing import List

# https://adventofcode.com/2024/day/2
class RedNosedReports:
    def solve(self, reports: List[str], use_dampener: bool = False) -> int:
        safe_counter = 0
        for report in reports:
            levels = list(map(int, report.split(" ")))
            safe_counter += 1 if self._is_safe(levels, use_dampener) else 0
        return safe_counter

    def _is_safe(self, levels: List[int], use_dampener: bool) -> bool:
        increasing = False
        for i in range(1, len(levels)):
            if i == 1:
                increasing = levels[i] > levels[i - 1]
            if ((levels[i] == levels[i - 1] or increasing and levels[i] < levels[i - 1]) or
                    (increasing and levels[i] < levels[i - 1]) or
                    (not increasing and levels[i] > levels[i - 1]) or
                    (abs(levels[i] - levels[i - 1]) > 3)):
                if use_dampener:
                    return (self._is_safe(levels[:i] + levels[i + 1:], False) or
                            self._is_safe(levels[:i - 1] + levels[i:], False) or
                            (i > 1 and self._is_safe(levels[:i - 2] + levels[i - 1:], False)))
                else:
                    return False
        return True
