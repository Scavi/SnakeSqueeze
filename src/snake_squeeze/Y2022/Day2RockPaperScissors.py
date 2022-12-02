from enum import Enum
from typing import List


class Result(int, Enum):
    Win = 6
    Draw = 3
    Lose = 0

    @staticmethod
    def value_of(value: str) -> 'Result':
        if value == "X":
            return Result.Lose
        elif value == "Y":
            return Result.Draw
        elif value == "Z":
            return Result.Win
        else:
            raise ValueError(f"Unsupported value: '{value}'")


class Hand(int, Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

    @staticmethod
    def value_of(value: str) -> 'Hand':
        if value == "A" or value == "X":
            return Hand.Rock
        elif value == "B" or value == "Y":
            return Hand.Paper
        elif value == "C" or value == "Z":
            return Hand.Scissors
        else:
            raise ValueError(f"Unsupported value: '{value}'")

    def choose_hand(self, result: Result) -> 'Hand':
        hands = [e for e in Hand]
        offset = 0 if result == Result.Draw else 1 if result == Result.Win else -1
        return hands[(int(self) - 1 + offset) % len(hands)]


class Day2RockPaperScissors:
    @staticmethod
    def solve(strategies: List[str], strategically=False) -> int:
        """
        https://adventofcode.com/2022/day/2

        Args:
            strategies: The puzzle input which contains the provided strategies from the elf
            strategically: True: play how the elf initially meant to be, False: How we understood

        Returns:
            The score
        """
        points = 0
        for strategy in strategies:
            hands = strategy.split(" ")
            if strategically:
                elf_hand = Hand.value_of(hands[0])
                my_hand = elf_hand.choose_hand(Result.value_of(hands[1]))
            else:
                elf_hand, my_hand = Hand.value_of(hands[0]), Hand.value_of(hands[1])
            points += (3 if my_hand == elf_hand else 6 if my_hand.choose_hand(Result.Win) != elf_hand else 0) + my_hand
        return points
