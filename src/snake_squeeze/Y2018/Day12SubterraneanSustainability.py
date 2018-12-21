from snake_squeeze.Y2018.Helper import Cache

PLANT = "#"
EMPTY_POT = "."


class Day12SubterraneanSustainability:
    def __init__(self, generations=20):
        self._generations = generations


    def solve(self, initial_state, spread_table):
        """
        Args:
            initial_state (str): The initial state of the pots
            spread_table ([str]):

        Returns:
            int: the count of pots containing plants
        """
        pots = []
        for i in range(0, len(initial_state)):
            pots.append((i, initial_state[i]))

        terran_cache = Cache()
        pot_spread_pattern = self._create_pattern_correlation(spread_table)
        for i in range(self._generations):
            pots = self._prepare_pot_list(pots)
            pots_pattern = self._cache_pattern(pots)

            # reuse calculated result
            if terran_cache.has(pots_pattern):
                current_pot_sum = self._generation_sum(pots)
                last_pots = terran_cache.order[i - 2]
                diff = current_pot_sum - self._generation_sum(last_pots)
                rest = (self._generations - i)
                return current_pot_sum + (diff * rest)
            else:
                plant_pattern = ""
                new_pot_generation = list()
                for pot in pots:
                    plant_pattern += pot[1]
                    if len(plant_pattern) > 4:
                        new_pot_generation.append((pot[0] - 2, pot_spread_pattern.get(plant_pattern, EMPTY_POT)))
                        plant_pattern = plant_pattern[1:]
                # cache input pattern to the generated output list
                terran_cache.add(pots_pattern, new_pot_generation)
                pots = new_pot_generation
        return self._generation_sum(pots)


    @staticmethod
    def _cache_pattern(pots):
        pattern = ""
        for pot in pots:
            pattern += pot[1]
        return pattern


    @staticmethod
    def _generation_sum(pots):
        result = 0
        for pot in pots:
            if pot[1] == PLANT:
                result += pot[0]
        return result


    @staticmethod
    def _create_pattern_correlation(spread_table):
        spread_pattern = dict()
        for spread_input in spread_table:
            spread_pattern[spread_input[0:5]] = spread_input[9:10]
        return spread_pattern


    @staticmethod
    def _prepare_pot_list(pots):
        # at least 4 dots are required at the left side to make sure that all pattern will be recognized
        # (usually only 3 with the given pattern). Makes sure that the required amount of dots are on the left side
        s = 0
        while pots[s][1] == EMPTY_POT:
            s += 1
        for i in range(s, 4):
            pots.insert(0, (pots[0][0] - 1, EMPTY_POT))
        # similar for the end of the list. Make sure that at least 4 dots are at the end
        e = len(pots) - 1
        while pots[e][1] == EMPTY_POT:
            e -= 1
        for i in range(len(pots) - e - 1, 4):
            pots.append((pots[len(pots) - 1][0] + 1, EMPTY_POT))
        return pots
