from pathlib import Path
from unittest import TestCase

from snake_squeeze.Util.FileHelper import FileHelper
from snake_squeeze.Y2018.Day2InventoryManagementSystem import Day2InventoryManagementSystem


class TestInventoryManagementSystem(TestCase):

    def test_preparation_1(self):
        ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        inventory_management_system = Day2InventoryManagementSystem()
        checksum = inventory_management_system.solve1(ids)
        self.assertEqual(12, checksum)

    def test_preparation_2(self):
        ids = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
        inventory_management_system = Day2InventoryManagementSystem()
        common_id_letters = inventory_management_system.solve2(ids)
        self.assertEqual("fgij", common_id_letters)

    def test_part_1(self):
        ids = FileHelper.read_file(Path("../../Input/2018/Day2.txt"))
        inventory_management_system = Day2InventoryManagementSystem()
        checksum = inventory_management_system.solve1(ids)
        self.assertEqual(6723, checksum)

    def test_part_2(self):
        ids = FileHelper.read_file(Path("../../Input/2018/Day2.txt"))
        inventory_management_system = Day2InventoryManagementSystem()
        common_id_letters = inventory_management_system.solve2(ids)
        self.assertEqual("prtkqyluiusocwvaezjmhmfgx", common_id_letters)
