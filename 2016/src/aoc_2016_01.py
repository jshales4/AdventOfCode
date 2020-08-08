# 2016 Day 1

import enum
from typing import Tuple, Dict

YEAR = 2016
DAY = 1


class Direction(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Position:

    x_pos: int
    y_pos: int
    direction: Direction

    def __init__(self, x_pos: int, y_pos: int, current_direction: Direction):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = current_direction

    def __str__(self):
        return f"The position is ({self.x_pos},{self.y_pos}) facing {self.direction}."

    def get_location_str(self) -> str:
        """represents the current x,y as a string to serve as a dictionary key."""
        return f"{self.x_pos}_{self.y_pos}"


def get_new_direction(current_position: Position, instruction: str) -> Position:
    assert instruction in ["L", "R"]
    if instruction == "L":
        direction_adjustment = -1
    else:
        direction_adjustment = 1
    current_position.direction = Direction(
        (current_position.direction.value + direction_adjustment) % 4
    )
    return current_position


def split_instruction(instruction: str) -> Tuple[str, int]:
    instruction_direction: str = instruction[0]
    instruction_magnitude: int = int(instruction[1:])
    return instruction_direction, instruction_magnitude


def take_steps(
    position: Position,
    number_of_steps: int,
    position_tracker: Dict[str, int],
    still_looking: bool,
) -> Tuple[Position, Dict[str, int], bool]:
    direction = position.direction
    x_change = 0
    y_change = 0
    if direction == Direction.NORTH:
        y_change = 1 * number_of_steps
    elif direction == Direction.EAST:
        x_change = 1 * number_of_steps
    elif direction == Direction.SOUTH:
        y_change = -1 * number_of_steps
    else:
        x_change = -1 * number_of_steps

    for x in range(abs(x_change)):
        position.x_pos += abs(x_change) / x_change
        position_tracker, still_looking = add_to_visited_locations(
            position, position_tracker, still_looking
        )
    for y in range(abs(y_change)):
        position.y_pos += abs(y_change) / y_change
        position_tracker, still_looking = add_to_visited_locations(
            position, position_tracker, still_looking
        )

    return position, position_tracker, still_looking


def add_to_visited_locations(position, position_tracker, still_looking):
    location = position.get_location_str()
    if position_tracker.get(location):
        if still_looking:
            print(
                f" The first location visited twice is {abs(position.x_pos) + abs(position.y_pos)} blocks away."
            )
            still_looking = False
        position_tracker[location] += 1
    else:
        position_tracker[location] = 1
    return position_tracker, still_looking


def main():
    current_position = Position(0, 0, Direction.NORTH)
    data = (
        open(f"../input_data/input_{YEAR}_{DAY:02d}.txt", "r")
        .readlines()[0]
        .split(", ")
    )
    position_tracker: Dict[str, int] = {current_position.get_location_str(): 0}
    still_looking = True
    for instruction in data:
        direction, magnitude = split_instruction(instruction)
        current_position = get_new_direction(current_position, direction)
        current_position, position_tracker, still_looking = take_steps(
            current_position, magnitude, position_tracker, still_looking
        )

    print(current_position)
    print(
        f"Answer to part 1 is {abs(current_position.x_pos) + abs(current_position.y_pos)}"
    )


if __name__ == "__main__":
    main()
