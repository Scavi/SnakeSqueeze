from snake_squeeze.Y2018.Helper import Cache

TREES = "|"
LUMBERYARD = "#"
OPEN_GROUND = "."


class Day18SettlersOfTheNorthPole:
    MOVES = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


    def __init__(self, minutes=10):
        self._minutes = minutes


    def solve(self, acre_input):
        acres = self._create_acre(acre_input)
        acres_cache = Cache()
        i = 0
        while i < self._minutes:
            acres_finger_print = self._create_finger_print(acres)
            if acres_cache.has(acres_finger_print):
                rest = (self._minutes - i)
                start_pos = acres_cache.pos_of(acres)
                repeat_loop_size = len(acres_cache.order) - 1 - start_pos
                lookup = (rest % repeat_loop_size) + start_pos
                return self._calc_result(acres_cache.order[lookup])
            else:
                new_acres = [[' ' for _ in range(len(acres))] for _ in range(len(acres))]
                for y in range(len(acres)):
                    for x in range(len(acres)):
                        current = acres[y][x]
                        if current == LUMBERYARD:
                            new_acres[y][x] = LUMBERYARD if self._stays_lumberyard(acres, x, y) else OPEN_GROUND
                        elif current == TREES:
                            new_acres[y][x] = LUMBERYARD if self._is_space_change(acres, LUMBERYARD, x, y) else current
                        elif current == OPEN_GROUND:
                            new_acres[y][x] = TREES if self._is_space_change(acres, TREES, x, y) else current
                acres = new_acres
                acres_cache.add(acres_finger_print, acres)
            i += 1
        return self._calc_result(acres)


    @staticmethod
    def _create_finger_print(acres):
        fp = ""
        for y in range(len(acres)):
            for x in range(len(acres)):
                fp += acres[y][x]
        return fp


    @staticmethod
    def _stays_lumberyard(acre, x, y):
        has_adj_lumberyard = False
        has_adj_tree = False
        for m in Day18SettlersOfTheNorthPole.MOVES:
            c_x = x + m[0]
            c_y = y + m[1]
            if 0 <= c_x < len(acre) and 0 <= c_y < len(acre):
                if acre[c_y][c_x] == TREES:
                    has_adj_tree = True
                if acre[c_y][c_x] == LUMBERYARD:
                    has_adj_lumberyard = True
                if has_adj_tree and has_adj_lumberyard:
                    break
        return has_adj_tree and has_adj_lumberyard


    @staticmethod
    def _is_space_change(acre, lookup, x, y):
        found_count = 0
        for m in Day18SettlersOfTheNorthPole.MOVES:
            c_x = x + m[0]
            c_y = y + m[1]
            if 0 <= c_x < len(acre) and 0 <= c_y < len(acre) and acre[c_y][c_x] == lookup:
                found_count += 1
                if found_count >= 3:
                    break
        return found_count >= 3


    @staticmethod
    def _calc_result(acres):
        lumber_count = 0
        tree_count = 0
        for row in acres:
            for place in row:
                if place == TREES:
                    tree_count += 1
                elif place == LUMBERYARD:
                    lumber_count += 1
        return lumber_count * tree_count


    @staticmethod
    def _create_acre(acre_input):
        acre = []
        for a in acre_input:
            acre.append(list(a))
        return acre
