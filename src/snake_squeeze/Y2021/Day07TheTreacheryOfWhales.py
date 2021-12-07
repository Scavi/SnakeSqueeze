import sys


class TheTreacheryOfWhales:
    @staticmethod
    def solve(data: str, crab_move=False) -> int:
        crab_alignment = list(map(int, data.split(",")))
        min_pos, max_pos = min(crab_alignment), max(crab_alignment)
        fuel = sys.maxsize
        for i in range(min_pos, max_pos):
            tmp = 0
            for crab_pos in crab_alignment:
                n = abs(i - crab_pos)
                tmp += n * (n + 1) // 2 if crab_move else n
            fuel = min(tmp, fuel)
        return fuel
