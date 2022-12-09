from typing import List


class Day8TreetopTreeHouse:
    def solve_1(self, trees: List[str]) -> int:
        cache = [[False] * (len(trees[0])) for _ in range(len(trees))]
        return (self._count_vis(trees, cache, 0, len(trees[0]), 1, False) +
                self._count_vis(trees, cache, len(trees[0]) - 1, 0, -1, False) +
                self._count_vis(trees, cache, 0, len(trees[0]), 1, True) +
                self._count_vis(trees, cache, len(trees[0]) - 1, 0, -1, True))

    def solve_2(self, trees: List[str]) -> int:
        sight_count = 1
        for y in range(0, len(trees)):
            for x in range(0, len(trees[0])):
                sight_count = max(sight_count, self._count_sight(trees, x, y))
        return sight_count

    @staticmethod
    def _count_sight(trees: List[str], sx: int, sy: int) -> int:
        sight_count = 1
        for direction in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            x, y = sx, sy
            current_sight = 0
            while True:
                x, y = (x + direction[0]), (y + direction[1])
                if x < 0 or x >= len(trees[0]) or y < 0 or y >= len(trees):
                    break
                current_sight += 1
                if trees[sy][sx] <= trees[y][x]:
                    break
            sight_count *= current_sight
        return sight_count

    @staticmethod
    def _count_vis(trees: List[str], cache: List[List[bool]], start: int, stop: int, step: int, toggle: bool) -> int:
        visible_count = 0
        for y in range(0, len(trees)):
            highest = '0'
            for x in range(start, stop, step):
                lx, ly = (y, x) if toggle else (x, y)
                if not cache[ly][lx]:
                    if lx == 0 or ly == 0 or ly == len(trees) - 1 or lx == len(trees[0]) - 1 or highest < trees[ly][lx]:
                        cache[ly][lx] = True
                        visible_count += 1
                highest = highest if highest > trees[ly][lx] else trees[ly][lx]
        return visible_count
