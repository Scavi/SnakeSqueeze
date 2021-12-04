from copy import deepcopy
from typing import List


class BinaryDiagnostic:
    def determine_power_consumption(self, diag_data: List[str]) -> int:
        analytics = self._create_analytics(diag_data, True)
        gamma_rate = ''.join([f'{x}' for x in analytics])
        epsilon_rate = ''.join(['1' if x == 0 else '0' for x in analytics])
        return int(gamma_rate, 2) * int(epsilon_rate, 2)

    def determine_life_supply(self, diag_data: List[str]) -> int:
        return self._diag(deepcopy(diag_data), True) * self._diag(deepcopy(diag_data), False)

    def _diag(self, diag_data: List[str], most_common: bool) -> int:
        for i in range(len(diag_data[0])):
            analytics = self._create_analytics(diag_data, most_common)
            for _ in range(len(diag_data)):
                diagnostic = diag_data.pop(0)
                if not diag_data or int(diagnostic[i]) == analytics[i]:
                    diag_data.append(diagnostic)
        return int(''.join(diag_data), 2)

    @staticmethod
    def _create_analytics(diag_data: List[str], most_common: bool) -> List[int]:
        analytics = [0] * len(diag_data[0])
        for diagnostic in diag_data:
            for i in range(len(diagnostic)):
                analytics[i] += -1 if diagnostic[i] == '0' else 1
        for i in range(len(analytics)):
            if analytics[i] > 0:
                analytics[i] = 1 if most_common else 0
            elif analytics[i] < 0:
                analytics[i] = 0 if most_common else 1
            else:
                analytics[i] = 1 if most_common else 0
        return analytics
