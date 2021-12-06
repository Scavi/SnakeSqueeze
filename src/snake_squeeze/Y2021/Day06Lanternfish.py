import numpy as np


class Lanternfish:
    @staticmethod
    def solve(data: str, days) -> int:
        fish = np.zeros(9)
        for v in list(map(int, data.split(","))):
            fish[v] += 1

        for _ in range(days):
            reproducing = fish[0]
            for i in range(8):
                fish[i] = fish[i + 1]
            fish[8] = reproducing
            fish[6] += reproducing
        return fish.sum()
