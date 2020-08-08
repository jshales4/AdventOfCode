# AoC 2019 Day 3
from typing import Tuple, Optional, Dict

YEAR = 2019
DAY = 3


def interpret_direction(direction: str) -> Tuple[int, int]:
    if direction == "U":
        return 0, 1
    elif direction == "D":
        return 0, -1
    elif direction == "R":
        return 1, 0
    elif direction == "L":
        return -1, 0
    else:
        assert False


def split_direction(direction: str) -> Tuple[str, int]:
    return direction[0], int(direction[1:])


def parse_coords_attended(wire_path: str) -> Dict[str, int]:
    visited_positions: Dict[str, int] = {}
    current_pos = (0, 0)
    steps_made = 0
    directions = wire_path.split(",")
    for entry in directions:
        direction, magnitude = split_direction(entry)
        x_change, y_change = interpret_direction(direction)
        for i in range(magnitude):
            current_pos = (current_pos[0] + x_change, current_pos[1] + y_change)
            steps_made += 1
            if current_pos not in visited_positions:
                visited_positions[
                    str(current_pos[0]) + "_" + str(current_pos[1])
                ] = steps_made
    return visited_positions


# Part 1
def find_min_distance_of_intersect(data):
    wire_1_positions = set(parse_coords_attended(data[0]).keys())
    wire_2_positions = set(parse_coords_attended(data[1]).keys())
    intersections = wire_1_positions & wire_2_positions
    min_distance: Optional[int] = None
    for intersection in intersections:
        x, y = map(int, intersection.split("_"))
        abs_distance = abs(x) + abs(y)
        if not min_distance or abs_distance < min_distance:
            min_distance = abs_distance

    return min_distance


# Part 2
def find_min_distance_traveled_to_intersect(data):
    wire_1_dict = parse_coords_attended(data[0])
    wire_2_dict = parse_coords_attended(data[1])
    wire_1_positions = set(wire_1_dict.keys())
    wire_2_positions = set(wire_2_dict.keys())
    intersections = wire_1_positions & wire_2_positions
    min_combined_distance: Optional[int] = None
    for intersection in intersections:
        total_distance_traveled = wire_1_dict[intersection] + wire_2_dict[intersection]
        if not min_combined_distance or total_distance_traveled < min_combined_distance:
            min_combined_distance = total_distance_traveled
    return min_combined_distance


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    print(find_min_distance_of_intersect(data), "is answer to Part 1")
    print(find_min_distance_traveled_to_intersect(data), "is answer to Part 2")


if __name__ == "__main__":
    main()
