class Day11ChronalCharge:
    def __init__(self, grid_size):
        self._size = grid_size  # grid starts with 1,1 at array pos 0,0
        self._square_size = 3


    def solve(self, serial_number):
        power_grid = [[0 for _ in range(0, self._size)] for _ in range(0, self._size)]
        for y in range(self._size):
            for x in range(self._size):
                power_grid[y][x] = self._power_level(serial_number, x, y)
        target_x, target_y, result_sum = self._naive(power_grid)

        # cache = self._create_cache(power_grid)
        # target_x, target_y, result_sum = self._search_grid(power_grid, cache)
        # # tmp = [[1, 1, 1, 1, 1],
        # #        [2, 2, 2, 2, 2],
        # #        [3, 8, 6, 7, 3],
        # #        [4, 4, 4, 4, 4],
        # #        [5, 5, 5, 5, 5]]
        # # r = self.test_it(tmp)
        #

        #
        # tmp = [[-2, -4, 4, 4, 4],
        #        [-4, 4, 4, 4, -5],
        #        [4, 3, 3, 4, -4],
        #        [1, 1, 2, 4, -3],
        #        [1, 0, 2, -5, 2]]
        # r = self.test_it(tmp)

        # <class 'list'>: [ 3,-3,  3, 0,-2,-3,-2, 0, 3,-3, 2,-1,-3,-4,-4,-2, 1,-5, 0,-4, 4, 3, 3, 4,-4, 0,-5, 1,-1, -3, -3, -2, 0, 4, -1, -5, 2, 0, 0, 1, 3, -4, 0, -4, 3, 1, 0, 1, 3, -4, 0, -5, 2, 0, -1, -1, 1, 4, -2, 3, -1, -3, -4, -4, -3, 0, 4, -1, -5, 2, 1, 1, 2, 4, -3, 2, -2, -5, 4, 3, 4, -4, -1, 4, 0, -3, -5, 4, -5, -3, 0, 4, -1, -4, 4, 3, 3, -5, -2, 2, -3, 3, 1, 0, 0, 1, 4, -2, 3, -1, -4, -5, -5, -4, -2, 2, -3, 3, 0, -2, -2, -1, 1, 4, -2, 4, 1, -1, -1, -1, 1, 4, -2, 4, 1, -1, -2, -2, 0, 3, -3, 2, -2, -4, -5, -5, -4, -1, 3, -2, 4, 1, 0, 0, 1, 3, -3, 2, -2, -5, 3, 3, 4, -4, -1, 4, 0, -3, -5, 4, -5, -3, 0, 4, -1, -4, 4, 3, 4, -5, -2, 2, -3, 4, 2, 1, 1, 2, -5, -1, 4, 0, -3, -4, -4, -3, -1, 3, -2, 4, 1, -1, -1, 0, 2, -5, 0, -4, 3, 1, 0, 1, 3, -4, 0, -4, 3, 1, 0, 0, 2, -5, -1, 4, 0, -2, -3, -3, -1, 1, -5, 0, -4, 4, 3, 3, 4, -4, 0, -5, 1, -2, -4, -4, -3, -1, 2, -3, 3, 0, -2, -3, -2, 0, 3, -3, 3, 0, -2, -3, -3, -1, 2, -4, 1, -2, -4, -5, -5, -4, -1, 3, -2, 4, 1, 0, 0, 1, 4, -3, 2, -2, -5, 4, 4, -5, -3, 0, -5, 1, -2, -4, -5, -4, -2, 1, -5, 1, -2, -4]
        # <class 'list'>: [ 4,-1, -5, 2, 0, 0, 1, 3,-4, 1,-3, 4, 2, 2, 3,-5,-2, 2,-2,-5, 3, 3, 4,-4,-1, 3,-1,-4, 4, 3, 4, -4, -1, 3, -1, -4, 4, 3, 4, -4, -1, 3, -2, -5, 3, 2, 3, -5, -2, 2, -3, 4, 2, 1, 1, 3, -4, 0, -5, 2, 0, -1, -1, 1, 4, -2, 3, -1, -3, -4, -4, -2, 1, -5, 0, -4, 4, 3, 3, 4, -3, 1, -4, 2, 0, -1, -1, 0, 3, -3, 2, -2, -5, 4, 4, -5, -2, 2, -3, 3, 0, -1, -1, 0, 2, -4, 1, -3, 4, 3, 3, 4, -4, 0, -5, 1, -2, -4, -4, -3, -1, 3, -2, 4, 1, -1, -1, 0, 2, -5, 0, -4, 3, 1, 1, 2, 4, -3, 2, -2, -5, 3, 2, 3, -5, -2, 3, -1, -4, 4, 3, 4, -4, -1, 3, -1, -4, 4, 3, 4, -4, -1, 3, -1, -4, 4, 3, 3, -5, -2, 2, -2, -5, 3, 2, 2, 4, -3, 1, -4, 3, 1, 0, 0, 2, -5, -1, 4, 1, -1, -2, -2, -1, 2, -4, 1, -2, -4, -5, -5, -4, -1, 3, -2, 4, 2, 1, 1, 2, -5, -1, 4, 0, -2, -3, -3, -2, 0, 4, -1, -5, 3, 2, 2, 3, -5, -1, 4, 0, -3, -4, -4, -3, -1, 3, -2, 4, 1, 0, 0, 1, 3, -4, 1, -3, 4, 3, 3, 4, -4, -1, 4, 0, -3, -5, -5, -4, -2, 1, -4, 2, -1, -3, -3, -2, 0, 3, -3, 3, 0, -2, -2, -1, 1, 4, -2, 4, 1, -1, -2, -1, 1, 4, -2, 4, 1, -1, -2, -1, 1, 4, -2, 3, 0, -2, -3, -2, 0, 3, -3]
        # <class 'list'>: [-5, 0, -4, 4, 3, 3, 4,-4, 0,-5, 1,-1,-3,-3,-1, 1,-5, 0,-3, 4, 3, 3, 4,-3, 1,-4, 3, 0,-1, -1, 1, 3, -3, 3, -1, -3, -4, -4, -2, 1, -5, 0, -4, 4, 3, 4, -5, -2, 2, -2, 4, 2, 1, 2, 4, -3, 1, -4, 3, 1, 0, 1, 2, -5, 0, -5, 2, 0, 0, 0, 2, -5, -1, -5, 2, 0, 0, 0, 2, -5, 0, -5, 2, 1, 0, 1, 3, -4, 1, -3, 4, 2, 1, 2, 4, -2, 2, -2, -5, 4, 3, 4, -4, 0, -5, 1, -2, -4, -4, -3, -1, 3, -3, 3, 1, -1, -1, 0, 3, -4, 1, -3, 4, 3, 3, 4, -3, 0, -5, 1, -1, -3, -3, -1, 1, -5, 0, -4, 4, 3, 3, 4, -4, 0, -5, 2, -1, -2, -2, 0, 2, -4, 1, -2, -4, -5, -5, -4, -1, 3, -2, -5, 2, 1, 2, 3, -4, 0, -4, 2, 0, -1, -1, 1, 4, -2, 4, 0, -2, -3, -2, -1, 2, -3, 2, -1, -3, -4, -3, -1, 2, -4, 1, -2, -4, -4, -4, -2, 1, -4, 1, -2, -4, -4, -3, -1, 2, -4, 2, -1, -3, -3, -3, -1, 3, -3, 3, 0, -1, -2, -1, 1, 4, -1, -5, 2, 1, 0, 1, 3, -3, 1, -3, -5, 3, 3, 4, -4, 0, -5, 1, -2, -4, -4, -3, 0, 3, -2, 4, 2, 0, 0, 1, 4, -2, 3, -1, -4, -5, -5, -4, -1, 2, -3, 4, 1, 0, 0, 2, 4, -2, 3, -1, -3, -4, -4, -2, 0, 4, -1, -4, 3, 2, 3, 4, -3, 1, -4, 3, 1, 0, 0, 1, 4, -2, 4, 0, -2, -3, -2]

        # print("{} {} {}".format(grid[45 - 1][33 - 1], grid[45 - 1][34 - 1], grid[45 - 1][35 - 1]))
        # print("{} {} {}".format(grid[46 - 1][33 - 1], grid[46 - 1][34 - 1], grid[46 - 1][35 - 1]))
        # print("{} {} {}".format(grid[47 - 1][33 - 1], grid[47 - 1][34 - 1], grid[47 - 1][35 - 1]))
        # print("--------------------------------------")
        # print("{} {} {}".format(grid[33 - 1][45 - 1], grid[34 - 1][45 - 1], grid[35 - 1][45 - 1]))
        # print("{} {} {}".format(grid[33 - 1][46 - 1], grid[34 - 1][46 - 1], grid[35 - 1][46 - 1]))
        # print("{} {} {}".format(grid[33 - 1][47 - 1], grid[34 - 1][47 - 1], grid[35 - 1][47 - 1]))

        return power_grid, target_x, target_y, result_sum

    def _naive(self, power_grid):
        max_sum = 0
        target_x = 0
        target_y = 0
        for y in range(self._size - self._square_size):
            for x in range(self._size - self._square_size):
                tmp = 0
                for i in range(self._square_size):
                    for j in range(self._square_size):
                        tmp += power_grid[y + i][x + j]
                if tmp > max_sum:
                    max_sum = tmp
                    target_x = x
                    target_y = y
        return target_x, target_y, max_sum

    def _create_cache(self, power_grid):
        cache = [[0 for _ in range(0, self._size)] for _ in range(0, self._size)]
        for x in range(self._size):
            tmp = 0
            for y in range(self._square_size):
                tmp += power_grid[y][x]
            cache[0][x] = tmp
            for y in range(1, self._size - self._square_size + 1):
                tmp += (power_grid[y + self._square_size - 1][x] - power_grid[y - 1][x])
                cache[y][x] = tmp
        return cache


    def _search_grid(self, power_grid, cache):
        target_x = 0
        target_y = 0
        max_sum = 0
        for y in range(self._size - self._square_size + 1):
            tmp = 0
            for x in range(self._square_size):
                tmp = cache[y][x]

            if tmp > max_sum:
                max_sum = tmp
                target_x = 0
                target_y = y

            for x in range(1, self._size - self._square_size + 1):
                tmp += cache[y][x + self._square_size - 1] - cache[y][x - 1]
                if tmp > max_sum:
                    max_sum = tmp
                    target_x = x
                    target_y = y

        target_y += 1
        result_sum = 0
        for y in range(target_y, self._square_size + target_y):
            for x in range(target_x, self._square_size + target_x):
                result_sum += power_grid[y][x]
                print(power_grid[y][x])
        return target_x, target_y, result_sum


    @staticmethod
    def _power_level(serial_number, x, y):
        x += 1
        y += 1
        rack_id = x + 10
        power_level = ((rack_id * y) + serial_number) * rack_id
        hundreds_digit = int(power_level % 1000 / 100)
        return hundreds_digit - 5
