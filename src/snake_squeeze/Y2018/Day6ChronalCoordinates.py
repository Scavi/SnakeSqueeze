import sys
from collections import deque


class Day6ChronalCoordinates:

    def __init__(self, coordinates, max_distance=0):
        self._coordinates = coordinates
        self._max_distance = max_distance
        self._grid_points, self._max_x, self._max_y = self._calculate_grid_data()
        self._grid = [[False for _ in range(self._max_y)] for _ in range(self._max_x)]
        sys.setrecursionlimit(50000)

    def solve1(self):
        max_fields = 0
        for grid_point in self._grid_points:
            self._search_spot_environment(grid_point, grid_point.x, grid_point.y)
            max_fields = max(max_fields, grid_point.space)
        return max_fields

    def _try_add(self, q, point, x, y):
        if point.is_infinite or x < 0 or x >= self._max_x or y < 0 or y >= self._max_y or \
                self._grid[x][y]:
            return
        q.append((x, y))

    def _search_spot_environment(self, point, x, y):
        if point.is_infinite or x < 0 or x >= self._max_x or y < 0 or y >= self._max_y or \
                self._grid[x][y]:
            return
        closest_points = self._count_closest_points(self._grid_points, x, y)
        if len(closest_points) == 1 and closest_points[0].point_id == point.point_id:
            point.space += 1
            self._grid[x][y] = True
            self._search_spot_environment(point, x - 1, y)
            self._search_spot_environment(point, x + 1, y)
            self._search_spot_environment(point, x, y - 1)
            self._search_spot_environment(point, x, y + 1)

    def solve2(self):
        return self._find_region(int(self._max_x / 2), int(self._max_y / 2))

    def _find_region(self, x, y):
        if x < 0 or x > self._max_x or y < 0 or y > self._max_y or self._grid[x][y]:
            return 0
        count = 0
        if self._in_distance(x, y):
            count = 1
            self._grid[x][y] = True
            count += self._find_region(x - 1, y)
            count += self._find_region(x + 1, y)
            count += self._find_region(x, y - 1)
            count += self._find_region(x, y + 1)
        return count

    def _in_distance(self, current_x, current_y):
        i = 0
        remaining_distance = self._max_distance
        while i < len(self._grid_points) and remaining_distance >= 0:
            remaining_distance -= self._distance(self._grid_points[i], current_x, current_y)
            i += 1
        return remaining_distance > 0

    # TODO naive & slow
    def _calculate_grid_data(self):
        max_x = 0
        max_y = 0
        grid_points = list()
        point_id = 65
        for point in self._coordinates:
            tmp = point.split(",")
            x = int(tmp[0])
            y = int(tmp[1])
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            grid_points.append(_GridPoint(chr(point_id), x, y))
            point_id += 1

        # top grid side
        for x in range(0, max_x):
            closest_points = self._count_closest_points(grid_points, x, 0)
            if len(closest_points) == 1:
                closest_points[0].is_infinite = True
        # bottom grid side
        for x in range(0, max_x):
            closest_points = self._count_closest_points(grid_points, x, max_y)
            if len(closest_points) == 1:
                closest_points[0].is_infinite = True
        # left grid side
        for y in range(0, max_x):
            closest_points = self._count_closest_points(grid_points, 0, y)
            if len(closest_points) == 1:
                closest_points[0].is_infinite = True
        # right grid side
        for y in range(0, max_x):
            closest_points = self._count_closest_points(grid_points, max_x, y)
            if len(closest_points) == 1:
                closest_points[0].is_infinite = True
        return grid_points, max_x, max_y

    # TODO naive & slow
    def _count_closest_points(self, grid_points, x, y):
        closest_points = list()
        min_distance = 1000000
        for grid_point in grid_points:
            distance = self._distance(grid_point, x, y)
            if distance < min_distance:
                closest_points = list()
                closest_points.append(grid_point)
                min_distance = distance
            elif distance == min_distance:
                closest_points.append(grid_point)
        return closest_points

    @staticmethod
    def _distance(grid_point, x, y):
        return abs(grid_point.x - x) + abs(grid_point.y - y)


class _GridPoint:
    def __init__(self, point_id, x, y):
        self.point_id = point_id
        self.x = x
        self.y = y
        self.is_infinite = False
        self.space = 0

    def __repr__(self):
        return "{} [{}:{}] = {}".format(self.point_id, self.x, self.y, self.is_infinite)
