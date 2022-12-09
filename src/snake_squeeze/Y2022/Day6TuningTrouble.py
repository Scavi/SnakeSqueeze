from collections import Counter


class Day6TuningTrouble:
    @staticmethod
    def solve(signal: str, marker: int) -> int:
        return [i for i in range(marker, len(signal)) if max(Counter(signal[i - marker:i]).values()) == 1][0]
