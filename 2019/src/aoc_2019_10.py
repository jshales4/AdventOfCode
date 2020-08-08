# AoC 2019 Day 10

from typing import List, Tuple, Dict, Optional, Any, NamedTuple
from decimal import Decimal
from math import atan2, pi
import collections

YEAR = 2019
DAY = 10


class Asteroid(NamedTuple):
    x: int
    y: int


class RelativeAsteroid(NamedTuple):
    absolute_distance: int
    asteroid: Asteroid


def build_asteroid_position_list(rows: List[str]) -> List[Asteroid]:
    asteroid_pos_list: List[Asteroid] = []
    for row_num, row in enumerate(rows):
        for column_num, char in enumerate(row):
            if char == "#":
                asteroid_pos_list.append(Asteroid(y=row_num, x=column_num))
    return asteroid_pos_list


def count_visible_asteroids(
    asteroid_index: int, asteroid_pos_list: List[Asteroid]
) -> int:
    relative_ast_positions = build_relative_asteroid_map(
        asteroid_index, asteroid_pos_list
    )
    return len(set(relative_ast_positions.keys()))


def build_relative_asteroid_map(asteroid_index: int, asteroid_pos_list: List[Asteroid]) -> Dict[float, List]:
    asteroid = asteroid_pos_list[asteroid_index]
    relative_ast_positions = collections.defaultdict(list)

    for neighbor_asteroid in asteroid_pos_list:
        if not (
            neighbor_asteroid.x == asteroid.x and neighbor_asteroid.y == asteroid.y
        ):
            ra = RelativeAsteroid(
                absolute_distance=abs(neighbor_asteroid.x - asteroid.x)
                + abs((neighbor_asteroid.y - asteroid.y)),
                asteroid=neighbor_asteroid,
            )
            relative_ast_positions[
                atan2(
                    neighbor_asteroid.y - asteroid.y, neighbor_asteroid.x - asteroid.x,
                )
            ].append(ra)
    return relative_ast_positions



def find_nth_asteroid_destroyed(
    asteroid_pos_list: List[Asteroid], asteroid_to_base_laser_from: int, nth_asteroid_to_look_for: int
):
    counter = 0
    relative_asteroid_map = build_relative_asteroid_map(
        asteroid_to_base_laser_from, asteroid_pos_list
    )
    spin_order = sorted(relative_asteroid_map.keys())
    starting_point = -pi / 2
    angle_index = 0
    for index, value in enumerate(spin_order):
        if value == starting_point:
            angle_index = index
    while True:
        if len(relative_asteroid_map[spin_order[angle_index]]) != 0:
            counter += 1
        remaining_asteroids = sorted(
            relative_asteroid_map[spin_order[angle_index]],
            key=lambda asteroid: asteroid.absolute_distance,
            reverse=True,
        )
        removed = remaining_asteroids.pop()
        relative_asteroid_map[spin_order[angle_index]] = set(remaining_asteroids)
        if counter == nth_asteroid_to_look_for:
            return removed.asteroid
        else:
            angle_index += 1
            if angle_index >= len(spin_order):
                angle_index = 0


def find_asteroid_with_max_visibles(asteroid_pos_list: List[Asteroid]):
    max = 0
    asteroid_to_base_laser_from = None
    for asteroid in range(len(asteroid_pos_list)):
        visible_asteroids = count_visible_asteroids(asteroid, asteroid_pos_list)
        if visible_asteroids > max:
            max = visible_asteroids
            asteroid_to_base_laser_from: Optional[int] = asteroid
    return asteroid_to_base_laser_from, max

def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    asteroid_pos_list = build_asteroid_position_list(data)
    asteroid_to_base_laser_from, max = find_asteroid_with_max_visibles(
        asteroid_pos_list
    )
    print(max, "is answer to part 1")
    nth_asteroid_to_look_for = 200
    nth_asteroid = find_nth_asteroid_destroyed(
        asteroid_pos_list, asteroid_to_base_laser_from, nth_asteroid_to_look_for
    )
    print(nth_asteroid, "is answer to part 2")

if __name__ == "__main__":
    main()
