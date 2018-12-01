class Day1ChronalCalibration:
    @staticmethod
    def solve1(input_lines):
        """
        Args:
            input_lines (list[str]): Each line contains either +<number> or -<number>

        Returns:
            int: The sum over all given frequencies
        """
        frequency = 0
        for line in input_lines:
            frequency += int(line)
        return frequency


    @staticmethod
    def solve2(input_lines):
        """
        Iterate over the given list of frequency over and over again to determine the first repetition.

        Args:
            input_lines (list[str]): Each line contains either +<number> or -<number>

        Returns:
            int: The first repeating frequency
        """
        frequency = 0
        repeat_value = None
        cache = set()
        while repeat_value is None:
            for line in input_lines:
                frequency += int(line)
                if frequency in cache:
                    repeat_value = frequency
                    break
                else:
                    cache.add(frequency)
        return frequency
