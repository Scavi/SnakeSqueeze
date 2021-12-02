from typing import List


class SonarSweep:
    @staticmethod
    def solve(data: List[int], size: int) -> int:
        return len([i for i in range(size, len(data)) if
                    sum(data[i - size: i]) > sum(data[i - size - 1: i - 1])])

    # Note: numpy solution
    # @staticmethod
    # def solve(data: List[int], size: int) -> int:
    #     slices = sliding_window_view(np.array(data), size)
    #     return len([i for i in range(1, len(slices)) if sum(slices[i]) > sum(slices[i - 1])])
