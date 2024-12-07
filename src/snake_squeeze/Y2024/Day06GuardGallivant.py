from enum import Enum
from typing import List, Tuple, Set


class Direction(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

class Guard:
    def __init__(self, direction: Direction, location: Tuple[int, int]) -> None:
        self._initial_direction = direction
        self._start_location = location
        self._direction = self._initial_direction
        self.location =  self._start_location
        self.on_duty = True
        self.is_looping = False
        self._memory = set()

    def move(self, input_map: List[str], obstacles: Set[Tuple[int, int]]):
        next_direction = None
        next_location = None
        while not next_direction:
            x, y = self.location
            dx, dy = self._direction.value
            next_location = (x + dx, y + dy)
            if next_location not in obstacles:
                next_direction = self._direction
            else:
                self._direction = self.turn()
        self.location = next_location
        lookup = f"{next_direction}_{next_location}"
        if lookup in self._memory:
            self.is_looping = True
        self._memory.add(lookup)
        self.on_duty = 0 <= self.location[0] < len(input_map[0]) and 0 <= self.location[1] < len(input_map)

    def turn(self) -> Direction:
        match self._direction:
            case Direction.NORTH:
                return Direction.EAST
            case Direction.EAST:
                return Direction.SOUTH
            case Direction.SOUTH:
                return Direction.WEST
            case Direction.WEST:
                return Direction.NORTH


class GuardGallivant:
    def solve(self, input_map: List[str]) -> Tuple[int, int]:
        obstacles = self._find_obstacles(input_map)
        guard_route = self._predict_guard_route(input_map, obstacles)
        different_obstruction = self._determine_different_obstruction(input_map, obstacles, guard_route)
        return len(guard_route), len(different_obstruction)

    @staticmethod
    def _determine_different_obstruction(
            input_map: List[str],
            obstacles: Set[Tuple[int, int]],
            guard_route: Set[Tuple[int, int]]
    ) -> Set[Tuple[int, int]]:
        different_obstruction = set()
        for route_location in guard_route:
            if route_location not in obstacles:
                start = [(y, x) for x, s in enumerate(input_map) for y, c in enumerate(s) if c == "^"][0]
                guard = Guard(Direction.NORTH, start)
                obstacles.add(route_location)
                while guard.on_duty and not guard.is_looping:
                    guard.move(input_map, obstacles)
                    if guard.is_looping:
                        different_obstruction.add(route_location)
                        break
                obstacles.remove(route_location)
        return different_obstruction

    @staticmethod
    def _predict_guard_route(input_map: List[str], obstacles: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        guard = Guard(Direction.NORTH, [(y, x) for x, s in enumerate(input_map) for y, c in enumerate(s) if c == "^"][0])
        path = set()
        while guard.on_duty:
            guard.move(input_map, obstacles)
            if guard.on_duty:
                path.add(guard.location)
        return path

    @staticmethod
    def _find_obstacles(input_map: List[str]) -> Set[Tuple[int, int]]:
        obstacles = set()
        for y in range(len(input_map)):
            for x in range(len(input_map[0])):
                if input_map[y][x] == "#":
                    obstacles.add((x, y))
        return obstacles
