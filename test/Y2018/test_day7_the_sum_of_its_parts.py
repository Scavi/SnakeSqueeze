from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2018.Day7TheSumofItsParts import Day7TheSumOfItsParts


class TestDay7TheSumOfItsParts(TestCase):
    def test_preparation_1(self):
        steps = [
            "Step C must be finished before step A can begin.",
            "Step C must be finished before step F can begin.",
            "Step A must be finished before step B can begin.",
            "Step A must be finished before step D can begin.",
            "Step B must be finished before step E can begin.",
            "Step D must be finished before step E can begin.",
            "Step F must be finished before step E can begin."]
        step_order = Day7TheSumOfItsParts().solve1(steps)
        self.assertEqual("CABDFE", step_order)

    def test_preparation_2(self):
        steps = [
            "Step C must be finished before step A can begin.",
            "Step C must be finished before step F can begin.",
            "Step A must be finished before step B can begin.",
            "Step A must be finished before step D can begin.",
            "Step B must be finished before step E can begin.",
            "Step D must be finished before step E can begin.",
            "Step F must be finished before step E can begin."]
        step_order = Day7TheSumOfItsParts(2).solve2(steps)
        self.assertEqual(15, step_order)

    def test_part_1(self):
        steps = FileHelper.read_file(Path("../../Input/2018/Day7.txt"))
        step_order = Day7TheSumOfItsParts().solve1(steps)
        self.assertEqual("CHILFNMORYKGAQXUVBZPSJWDET", step_order)

    def test_part_2(self):
        steps = FileHelper.read_file(Path("../../Input/2018/Day7.txt"))
        step_order = Day7TheSumOfItsParts(5, 60).solve2(steps)
        self.assertEqual(892, step_order)

