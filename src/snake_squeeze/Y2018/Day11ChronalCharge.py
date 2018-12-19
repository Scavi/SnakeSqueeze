import sys


class Day11ChronalCharge:
    def __init__(self, square_size=3):
        self._size = 300
        self._square_size = square_size


    def solve(self, serial_number):
        """
        Returns:
            (tuple): x,y of the start or x,y,size
        """
        power_grid = self._setup_grid(serial_number)
        aux = self._create_cache(power_grid)
        max_sum = -sys.maxsize - 1
        top_x = top_y = size = 0
        for y in range(self._size):
            for x in range(self._size):
                size_lookup = self._calc_size(x, y)
                for s in range(1, size_lookup):
                    if not self._square_size or (y + s < self._size and x + s < self._size):
                        current_sum = self._calc_sum(aux, x, y, x + s, y + s)
                        if current_sum > max_sum:
                            top_x = x
                            top_y = y
                            size = s
                            max_sum = current_sum
        return "{},{}".format(top_x + 1, top_y + 1), "{},{},{}".format(top_x + 1, top_y + 1, size + 1)


    def _calc_size(self, x, y):
        return self._square_size if self._square_size else self._size - max(x, y)


    @staticmethod
    def _calc_sum(grid_cache, x_top, y_top, x_bottom, y_bottom):
        """
        Computes the sum of the given cache between *_top and *_bottom. The given two dimensional array contains already
        the precomputed values. The cache
        """
        result = grid_cache[y_bottom][x_bottom]
        # removes all elements between (0, 0) and (y_top - 1, x_bottom)
        if y_top > 0:
            result = result - grid_cache[y_top - 1][x_bottom]
        # removes all elements between (0, 0) and (y_bottom, x_top - 1)
        if x_top > 0:
            result = result - grid_cache[y_bottom][x_top - 1]
        if y_top > 0 and x_top > 0:
            result = result + grid_cache[y_top - 1][x_top - 1]
        return result


    @staticmethod
    def _create_cache(power_grid):
        """
        Sums up all values between (0,0) and (x,y)

        Args:
            power_grid (int[][]): The power grid

        Returns:
            int[][]: The grid cache
        """
        grid_cache = [[0 for _ in range(len(power_grid[0]))] for _ in range(len(power_grid))]

        # fill first row
        for x in range(len(power_grid[0])):
            grid_cache[0][x] = power_grid[0][x]

        # sum up the columns
        for y in range(1, len(power_grid)):
            for x in range(len(power_grid[0])):
                grid_cache[y][x] = power_grid[y][x] + grid_cache[y - 1][x]

        # sum up the rows
        for y in range(len(power_grid)):
            for x in range(1, len(power_grid[0])):
                grid_cache[y][x] += grid_cache[y][x - 1]

        return grid_cache


    def _setup_grid(self, serial_number):
        power_grid = [[0 for _ in range(0, self._size)] for _ in range(0, self._size)]
        for y in range(self._size):
            for x in range(self._size):
                power_grid[y][x] = self._power_level(serial_number, x, y)
        return power_grid


    @staticmethod
    def _power_level(serial_number, x, y):
        x += 1
        y += 1
        rack_id = x + 10
        power_level = ((rack_id * y) + serial_number) * rack_id
        hundreds_digit = int(power_level % 1000 / 100)
        return hundreds_digit - 5
