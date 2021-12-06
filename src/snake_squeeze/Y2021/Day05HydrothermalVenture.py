import re
from typing import List


class HydrothermalVenture:
    def __init__(self, supports_diagonal=False) -> None:
        self.supports_diagonal = supports_diagonal

    def solve(self, all_coordinates: List[str]) -> int:
        grid = {}
        for coordinates in all_coordinates:
            x1, y1 = map(int, re.split("^(\\d+),(\\d+)", coordinates)[1:3])
            x2, y2 = map(int, re.split("(\\d+),(\\d+)$", coordinates)[1:3])
            if x1 == x2 or y1 == y2 or self.supports_diagonal:
                norm = max(abs(x1 - x2), abs(y1 - y2))
                dx, dy = (((x2 - x1) / norm), ((y2 - y1) / norm))
                current = (x1, y1)
                while current != (x2 + dx, y2 + dy):
                    grid[current] = grid.get(current, 0) + 1
                    current = (current[0] + dx, current[1] + dy)
        return sum([1 for x in grid.values() if x > 1])
