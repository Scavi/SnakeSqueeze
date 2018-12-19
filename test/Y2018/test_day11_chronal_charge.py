from unittest import TestCase

from snake_squeeze.Y2018.Day11ChronalCharge import Day11ChronalCharge


class TestDay11ChronalCharge(TestCase):

    def test_preparation_1(self):
        chronal_charge = Day11ChronalCharge()
        result = chronal_charge.solve(42)[0]
        self.assertEqual("21,61", result)


    def test_part_1(self):
        chronal_charge = Day11ChronalCharge()
        result = chronal_charge.solve(2187)[0]
        self.assertEqual("235,85", result)


    def test_preparation_2_1(self):
        chronal_charge = Day11ChronalCharge(square_size=None)
        result = chronal_charge.solve(18)[1]
        self.assertEqual("90,269,16", result)


    def test_preparation_2_2(self):
        chronal_charge = Day11ChronalCharge(square_size=None)
        result = chronal_charge.solve(42)[1]
        self.assertEqual("232,251,12", result)


    def test_part_2(self):
        chronal_charge = Day11ChronalCharge(square_size=None)
        result = chronal_charge.solve(2187)[1]
        self.assertEqual("233,40,13", result)
