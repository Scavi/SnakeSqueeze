from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2024.Day07BridgeRepair import BridgeRepair, Operators


class TestBridgeRepair(TestCase):
    def test_preparation_1(self) -> None:
        equations = FileHelper.read_file(Path("../../Input/2024/Day07_1.txt"))
        bridge_repair = BridgeRepair()
        calibration_result = bridge_repair.solve(equations, [Operators.PLUS, Operators.MUL])
        self.assertEqual(3749, calibration_result)

    def test_solve_1(self) -> None:
        equations = FileHelper.read_file(Path("../../Input/2024/Day07_2.txt"))
        bridge_repair = BridgeRepair()
        calibration_result = bridge_repair.solve(equations, [Operators.PLUS, Operators.MUL])
        self.assertEqual(5702958180383, calibration_result)

    def test_preparation_2(self) -> None:
        equations = FileHelper.read_file(Path("../../Input/2024/Day07_1.txt"))
        bridge_repair = BridgeRepair()
        calibration_result = bridge_repair.solve(equations, [o.value for o in Operators])
        self.assertEqual(11387, calibration_result)

    def test_solve_2(self) -> None:
        equations = FileHelper.read_file(Path("../../Input/2024/Day07_2.txt"))
        bridge_repair = BridgeRepair()
        calibration_result = bridge_repair.solve(equations,  [o.value for o in Operators])
        self.assertEqual(92612386119138, calibration_result)
