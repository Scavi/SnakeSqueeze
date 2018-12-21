from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2018.Day12SubterraneanSustainability import Day12SubterraneanSustainability


class TestDay12SubterraneanSustainability(TestCase):
    def test_preparation_1(self):
        subterranean = Day12SubterraneanSustainability()
        spread_table = [
            "...## => #",
            "..#.. => #",
            ".#... => #",
            ".#.#. => #",
            ".#.## => #",
            ".##.. => #",
            ".#### => #",
            "#.#.# => #",
            "#.### => #",
            "##.#. => #",
            "##.## => #",
            "###.. => #",
            "###.# => #",
            "####. => #"
        ]
        plant_containing_pots = subterranean.solve(initial_state="#..#.#..##......###...###",
                                                   spread_table=spread_table)
        self.assertEqual(325, plant_containing_pots)


    def test_solve_1(self):
        init_state = \
            "#.#.#..##.#....#.#.##..##.##..#..#...##....###..#......###.#..#.....#.###.#...#####.####...#####.#.#"
        subterranean = Day12SubterraneanSustainability()
        spread_table = FileHelper.read_file(Path("../../Input/2018/Day12.txt"))
        plant_containing_pots = subterranean.solve(
            initial_state=init_state,
            spread_table=spread_table)
        self.assertEqual(1917, plant_containing_pots)


    def test_solve_2(self):
        init_state = \
            "#.#.#..##.#....#.#.##..##.##..#..#...##....###..#......###.#..#.....#.###.#...#####.####...#####.#.#"
        subterranean = Day12SubterraneanSustainability(50000000000)
        spread_table = FileHelper.read_file(Path("../../Input/2018/Day12.txt"))
        plant_containing_pots = subterranean.solve(
            initial_state=init_state,
            spread_table=spread_table)
        self.assertEqual(1250000000991, plant_containing_pots)
