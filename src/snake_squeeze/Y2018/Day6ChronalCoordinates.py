import sys


class Day6ChronalCoordinates:

    def __init__(self, coordinates, max_distance=0):
        self._coordinates = coordinates
        self._max_distance = max_distance
        sys.setrecursionlimit(50000)

    def solve1(self):
        max_fields = 0
        grid_points, max_x, max_y = self._determine_grid_data()
        for x in range(0, max_x):
            for y in range(0, max_y):
                closest_points = self._count_closest_points(grid_points, x, y)
                if len(closest_points) == 1 and not closest_points[0].is_infinite:
                    closest_points[0].closest_fields += 1
                    max_fields = max(closest_points[0].closest_fields, max_fields)
        return max_fields

    def solve2(self):
        grid_points, max_x, max_y = self._determine_grid_data()
        grid = [[False for _ in range(max_y)] for _ in range(max_x)]
        return self._find_region(grid, grid_points, int(max_x / 2), int(max_y / 2), max_x, max_y)

    def _find_region(self, grid, grid_points, current_x, current_y, max_x, max_y):
        if current_x < 0 or current_x > max_x or current_y < 0 or current_y > max_y or \
                grid[current_x][current_y]:
            return 0
        count = 0
        if self._in_distance(grid_points, current_x, current_y):
            count += 1
            grid[current_x][current_y] = True
            count += self._find_region(grid, grid_points, current_x - 1, current_y, max_x, max_y)
            count += self._find_region(grid, grid_points, current_x + 1, current_y, max_x, max_y)
            count += self._find_region(grid, grid_points, current_x, current_y - 1, max_x, max_y)
            count += self._find_region(grid, grid_points, current_x, current_y + 1, max_x, max_y)
        return count

    def _in_distance(self, grid_points, current_x, current_y):
        i = 0
        remaining_distance = self._max_distance
        while i < len(grid_points) and remaining_distance >= 0:
            remaining_distance -= self._distance(grid_points[i], current_x, current_y)
            i += 1
        return remaining_distance > 0

    # TODO naive & slow
    def _determine_grid_data(self):
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
        self.closest_fields = 0

    def __repr__(self):
        return "{} [{}:{}] = {}".format(self.point_id, self.x, self.y, self.is_infinite)
