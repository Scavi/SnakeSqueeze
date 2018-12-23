import numpy

CAVE_MOD = 20183


class Day22ModeMaze:
    def __init__(self, depth):
        self._depth = depth


    def solve_1(self, target_point):
        cave_map = self._create_cave_map(target_point)
        risk_level = 0
        for y in range(target_point[0] + 1):
            for x in range(target_point[1] + 1):
                risk_level += cave_map[y][x] % 3
        return risk_level


    def _create_cave_map(self, target_point):
        cave_map = numpy.zeros(shape=(target_point[0] + 1, target_point[1] + 1))
        cave_map[0][0] = self._depth

        for i in range(1, len(cave_map)):
            cave_map[i][0] = ((i * 16807) + self._depth) % CAVE_MOD
        for i in range(1, len(cave_map[0])):
            cave_map[0][i] = ((i * 48271) + self._depth) % CAVE_MOD

        for y in range(1, len(cave_map)):
            for x in range(1, len(cave_map[0])):
                if target_point[1] == x and target_point[0] == y:
                    cave_map[y][x] = int(self._depth % CAVE_MOD)
                else:
                    top = cave_map[y - 1][x]
                    left = cave_map[y][x - 1]
                    cave_map[y][x] = (left * top + self._depth) % CAVE_MOD
        return cave_map
