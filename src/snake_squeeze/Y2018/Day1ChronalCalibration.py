class Day1ChronalCalibration:
    @staticmethod
    def solve1(input_lines):
        frequency = 0
        for line in input_lines:
            frequency += int(line)
        return frequency


    @staticmethod
    def solve2(input_lines):
        frequency = 0
        repeat_value = None
        cache = set()
        while repeat_value is None:
            for line in input_lines:
                frequency += int(line)
                if frequency in cache:
                    return frequency
                cache.add(frequency)
