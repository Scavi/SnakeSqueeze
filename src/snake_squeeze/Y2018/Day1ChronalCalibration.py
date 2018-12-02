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
        found_result = False
        cache = set()
        while not found_result:
            for line in input_lines:
                frequency += int(line)
                if frequency in cache:
                    found_result = True
                    break
                else:
                    cache.add(frequency)
        return frequency
