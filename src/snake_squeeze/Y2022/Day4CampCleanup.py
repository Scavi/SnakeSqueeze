import re
from typing import List


class Day4CampCleanup:

    @staticmethod
    def solve(sections: List[str], has_intersection=False) -> int:
        count = 0
        for section in sections:
            groups = list(map(int, re.split("[-,]", section)))
            elf_1, elf_2 = (groups[0], groups[1]), (groups[2], groups[3])
            if has_intersection:
                count += 1 if ((elf_1[0] <= elf_2[0] <= elf_1[1] or elf_1[0] <= elf_2[1] <= elf_1[1]) or
                               (elf_2[0] <= elf_1[0] <= elf_2[1] or elf_2[0] <= elf_1[1] <= elf_2[1])) else 0
            else:
                count += 1 if ((elf_1[0] <= elf_2[0] <= elf_1[1] and elf_1[0] <= elf_2[1] <= elf_1[1]) or
                               (elf_2[0] <= elf_1[0] <= elf_2[1] and elf_2[0] <= elf_1[1] <= elf_2[1])) else 0
        return count
