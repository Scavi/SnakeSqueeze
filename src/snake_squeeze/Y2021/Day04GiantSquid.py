import re
from functools import reduce
from operator import add, and_
from typing import List


class BingoField:
    def __init__(self, field_data: List[str]) -> None:
        if len(field_data) != 5:
            raise ValueError(f"Illegal field input: {field_data}. Expected 5 columns!")
        self._dim = len(field_data)
        self._field = []
        self._check = []
        self._is_complete = False
        for data in field_data:
            tmp = re.split("\\s+", data.strip())
            if len(tmp) != 5:
                raise ValueError(f"Illegal row input: {data}. Expected 5 rows!")
            self._field.append(tmp)
            self._check.append([False] * len(tmp))

    def flag(self, number: str) -> bool:
        for y in range(self._dim):
            for x in range(self._dim):
                if self._field[y][x] == number:
                    self._check[y][x] = True
                    if self._is_bingo(x, y):
                        self._is_complete = True
        return self._is_complete

    def _is_bingo(self, x: int, y: int) -> bool:
        tmp_x = [self._check[y][i] for i in range(self._dim)]
        tmp_y = [self._check[i][x] for i in range(self._dim)]
        return reduce(and_, tmp_x) or reduce(and_, tmp_y)

    def board_sum(self) -> int:
        not_checked = [[int(self._field[y][x]) for y in range(self._dim) if not self._check[y][x]]
                       for x in range(self._dim)]
        return reduce(add, reduce(add, not_checked))

    @property
    def is_complete(self):
        return self._is_complete


class BingoController:
    def __init__(self) -> None:
        self._bingo_fields = []

    def add_field(self, field_data: List[str]) -> None:
        self._bingo_fields.append(BingoField(field_data))

    def remove_field(self, field_index) -> None:
        self._bingo_fields.remove(self._bingo_fields[field_index])

    def play(self, number: str) -> List[int]:
        finished_board_index = []
        for i in range(len(self._bingo_fields)):
            if not self._bingo_fields[i].is_complete and self._bingo_fields[i].flag(number):
                finished_board_index.append(i)
        return finished_board_index

    @property
    def fields(self) -> List[BingoField]:
        return self._bingo_fields


class GiantSquid:
    def __init__(self, bingo_input: List[str], let_wookiee_win=False) -> None:
        self._controller = BingoController()
        self._let_wookiee_win = let_wookiee_win  # aeehh, squid of course ;)
        i = 2
        while i < len(bingo_input):
            self._controller.add_field(bingo_input[i: i + 5])
            i += 6

    def solve(self, bingo_numbers: List[str]) -> int:
        results = []
        for number in bingo_numbers:
            field_index = self._controller.play(number)
            for idx in field_index:
                results.append(self._controller.fields[idx].board_sum() * int(number))
        return results[len(results) - 1] if self._let_wookiee_win else results[0]
