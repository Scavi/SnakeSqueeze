from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2018.Day16ChronalClassification import Day16ChronalClassification


class TestDay16ChronalClassification(TestCase):

    def test_preparation_1(self):
        instructions = ["Before: [3, 2, 1, 1]",
                        "9 2 1 2",
                        "After:  [3, 2, 2, 1]"]
        chronal = Day16ChronalClassification()
        high_matches, _ = chronal.solve_1(instructions)
        self.assertEqual(1, high_matches)


    def test_solve(self):
        instructions = FileHelper.read_file(Path("../../Input/2018/Day16_1.txt"))
        chronal = Day16ChronalClassification()
        high_matches, op_code_correlations = chronal.solve_1(instructions)
        self.assertEqual(493, high_matches)

        instructions = FileHelper.read_file(Path("../../Input/2018/Day16_2.txt"))
        result = chronal.solve_2(instructions, op_code_correlations)
        self.assertEquals(1, result)
