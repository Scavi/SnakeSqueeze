from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2024.Day05PrintQueue import PrintQueue


class TestPrintQueue(TestCase):
    def test_preparation_1(self) -> None:
        search_input = FileHelper.read_file(Path("../../Input/2024/Day05_1.txt"))
        print_queue = PrintQueue()
        result = print_queue.solve(search_input)
        self.assertEqual(143, result[0])

    def test_preparation_2(self) -> None:
        search_input = FileHelper.read_file(Path("../../Input/2024/Day05_1.txt"))
        print_queue = PrintQueue()
        result = print_queue.solve(search_input)
        self.assertEqual(123, result[1])

    def test_solve_1(self) -> None:
        search_input = FileHelper.read_file(Path("../../Input/2024/Day05_2.txt"))
        print_queue = PrintQueue()
        result = print_queue.solve(search_input)
        self.assertEqual(4872, result[0])

    def test_solve_2(self) -> None:
        search_input = FileHelper.read_file(Path("../../Input/2024/Day05_2.txt"))
        print_queue = PrintQueue()
        result = print_queue.solve(search_input)
        self.assertEqual(5564, result[1])

