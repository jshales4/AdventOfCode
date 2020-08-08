# AoC 2019 Day 11
from typing import List, Tuple
from enum import Enum

YEAR = 2019
DAY = 11


class Direction(Enum):
    NORTH = (0, 1)
    WEST = (-1, 0)
    EAST = (1, 0)
    SOUTH = (0, -1)


def determine_new_robot_position(
    current_pos: Tuple[int, int], movement: Tuple[int, int]
) -> Tuple[int, int]:
    return current_pos[0] + movement[0], current_pos[1] + movement[1]


def enact_robot_instruction(
    map: List[List[bool]],
    current_pos: Tuple[int, int],
    current_direction: Direction,
    movement_instruction: int,
    should_paint_white: bool,
) -> Tuple[List[List[bool]], Direction, Tuple[int, int], bool]:
    new_direction = determine_new_facing_direction(
        current_direction, movement_instruction
    )
    new_pos = determine_new_robot_position(
        current_pos=current_pos, movement=new_direction.value
    )
    map[current_pos[0]][current_pos[1]] = should_paint_white
    return (
        map,
        new_direction,
        new_pos,
        map[new_pos[0]][new_pos[1]],
    )


def determine_new_facing_direction(direction: Direction, instruction: int) -> Direction:
    directions = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
    position = directions.index(direction)
    if instruction == 0:
        position -= 1
    else:
        assert instruction == 1
        position = (position + 1) % len(directions)
    return directions[position]


def build_paintable_grid() -> List[List[bool]]:
    """Bool represents isWhite"""
    columns = []
    for p in range(100):
        columns.append([])
    for column in columns:
        for p in range(100):
            column.append(False)
    columns[50][50] = True
    return columns


def render_painted_surface(surface: List[List[bool]]) -> None:
    for row in surface:
        row_string = ""
        for column in row:
            if column:
                row_string += " "
            else:
                row_string += "█"
        print(row_string)


def main():
    from aoc_2019_09 import parse_intcode_program

    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()

    returned_values = parse_intcode_program(
        data, program_input=1, painting_mode=True, noisy=False
    )
    print(returned_values)


if __name__ == "__main__":
    main()
