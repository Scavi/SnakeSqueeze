from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2018.Day4ReposeRecord import Day4ReposeRecord


class TestDay4ReposeRecord(TestCase):
    def test_preparation_1(self):
        max_sleep, _ = Day4ReposeRecord().solve(self._get_guard_records())
        self.assertEqual(240, max_sleep)

    def test_preparation_2(self):
        _, predictable_sleep = Day4ReposeRecord().solve(self._get_guard_records())
        self.assertEqual(4455, predictable_sleep)

    def test_part_1(self):
        guard_records = FileHelper.read_file(Path("../../Input/2018/Day4.txt"))
        max_sleep, _ = Day4ReposeRecord().solve(guard_records)
        self.assertEqual(71748, max_sleep)

    def test_part_2(self):
        guard_records = FileHelper.read_file(Path("../../Input/2018/Day4.txt"))
        _, predictable_sleep = Day4ReposeRecord().solve(guard_records)
        self.assertEqual(106850, predictable_sleep)

    @staticmethod
    def _get_guard_records():
        return [
            "[1518-11-01 00:00] Guard #10 begins shift",
            "[1518-11-01 00:05] falls asleep",
            "[1518-11-01 00:25] wakes up",
            "[1518-11-01 00:30] falls asleep",
            "[1518-11-01 00:55] wakes up",
            "[1518-11-01 23:58] Guard #99 begins shift",
            "[1518-11-02 00:40] falls asleep",
            "[1518-11-02 00:50] wakes up",
            "[1518-11-03 00:05] Guard #10 begins shift",
            "[1518-11-03 00:24] falls asleep",
            "[1518-11-03 00:29] wakes up",
            "[1518-11-04 00:02] Guard #99 begins shift",
            "[1518-11-04 00:36] falls asleep",
            "[1518-11-04 00:46] wakes up",
            "[1518-11-05 00:03] Guard #99 begins shift",
            "[1518-11-05 00:45] falls asleep",
            "[1518-11-05 00:55] wakes up"
        ]
