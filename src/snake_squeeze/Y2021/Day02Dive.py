from typing import List


class Dive:
    def __init__(self, with_aim=True) -> None:
        self.with_aim = with_aim

    def solve(self, data: List[str]) -> int:
        depth = horizontal = aim = 0
        for command in data:
            direction, distance = command.split(" ")
            if direction == "forward":
                horizontal += int(distance)
                if self.with_aim:
                    depth += int(distance) * aim
            elif direction == "down":
                if self.with_aim:
                    aim += int(distance)
                else:
                    depth += int(distance)
            elif direction == "up":
                if self.with_aim:
                    aim -= int(distance)
                else:
                    depth -= int(distance)
        return depth * horizontal
