from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2018.Day9MarbleMania import Day9MarbleMania


class TestDay9MarbleMania(TestCase):

    def test_preparation_0(self):
        score = Day9MarbleMania("9 players; last marble is worth 25 points").solve()
        self.assertEqual(32, score)


    def test_preparation_1(self):
        inputs = [
            ("10 players; last marble is worth 1618 points", 8317),
            ("13 players; last marble is worth 7999 points", 146373),
            ("17 players; last marble is worth 1104 points", 2764),
            ("21 players; last marble is worth 6111 points", 54718),
            ("30 players; last marble is worth 5807 points", 37305)
        ]

        for game_data in inputs:
            score = Day9MarbleMania(game_data[0]).solve()
            self.assertEqual(game_data[1], score)


    def test_part_1(self):
        marble_input = FileHelper.read_file(Path("../../Input/2018/Day9.txt"))
        step_order = Day9MarbleMania(marble_input[0]).solve()
        self.assertEqual(386018, step_order)


    def test_part_2(self):
        marble_input = FileHelper.read_file(Path("../../Input/2018/Day9.txt"))
        step_order = Day9MarbleMania(marble_input[0], 100).solve()
        self.assertEqual(3085518618, step_order)
