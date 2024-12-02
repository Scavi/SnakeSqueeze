from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2024.Day02RedNosedReports import RedNosedReports


class TestRedNosedReports(TestCase):
    def test_preparation_1(self) -> None:
        red_nose_report = RedNosedReports()
        safe_counter = red_nose_report.solve(self.create_report())
        self.assertEqual(2, safe_counter)

    def test_preparation_2(self) -> None:
        red_nose_report = RedNosedReports()
        safe_counter = red_nose_report.solve(self.create_report(), use_dampener=True)
        self.assertEqual(4, safe_counter)

    def test_solve_1(self) -> None:
        puzzle_input = FileHelper.read_file(Path("../../Input/2024/Day02.txt"))
        red_nose_report = RedNosedReports()
        safe_counter = red_nose_report.solve(puzzle_input)
        self.assertEqual(326, safe_counter)

    def test_solve_2(self) -> None:
        puzzle_input = FileHelper.read_file(Path("../../Input/2024/Day02.txt"))
        red_nose_report = RedNosedReports()
        safe_counter = red_nose_report.solve(puzzle_input, use_dampener=True)
        self.assertEqual(381, safe_counter)

    @staticmethod
    def create_report():
        return [
            "7 6 4 2 1",
            "1 2 7 8 9",
            "9 7 6 2 1",
            "1 3 2 4 5",
            "8 6 4 4 1",
            "1 3 6 7 9"
        ]
