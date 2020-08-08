# AoC 2019 Day 6
from typing import Tuple, List, Dict, Any, Optional

YEAR = 2019
DAY = 6


def split_into_orbits(entry: str) -> Tuple[str, str]:
    orbits = entry.split(")")
    return orbits[0], orbits[1]


def build_orbit_log(data: List[str]) -> Dict[str,List[Any]]:
    orbit_log: Dict[str, List[Any]] = {}
    for entry in data:
        orbit_1, orbit_2 = split_into_orbits(entry)
        if orbit_1 not in orbit_log:
            orbit_log[orbit_1] = []
        if orbit_2 not in orbit_log:
            orbit_log[orbit_2] = []
        orbit_log[orbit_1].append(orbit_2)
    return orbit_log


# Part 1
def count_children(
    orbit_index: str, orbit_log: Dict[str, Any], num_parents: int
) -> int:
    orbits = orbit_log[orbit_index]
    orbits_beneath = 0
    for orbiter in orbits:
        if len(orbit_log[orbiter]) == 0:
            orbits_beneath += num_parents + 1
        else:
            orbits_beneath += count_children(orbiter, orbit_log, num_parents + 1)
    return orbits_beneath + num_parents


# Part 2
def find_distance(
    starting_orbit: str,
    orbit_log: Dict[str, Any],
    searched_orbit: str,
    distance: int = 0,
) -> Optional[int]:
    if searched_orbit in orbit_log[starting_orbit]:
        return distance + 1
    elif len(orbit_log[starting_orbit]) > 0:
        min_distance = None
        for orbit in orbit_log[starting_orbit]:
            new_distance = find_distance(orbit, orbit_log, searched_orbit, distance + 1)
            if new_distance and (not min_distance or new_distance < min_distance):
                min_distance = new_distance
        return min_distance
    else:
        return None


# Part 2
def build_distance_map(
    orbit_1, orbit_2, orbit_log, starting_point: str, distance_map=None
):
    if not distance_map:
        distance_map = {}
    distance_map[starting_point] = (
        find_distance(starting_point, orbit_log, orbit_1),
        find_distance(starting_point, orbit_log, orbit_2),
    )
    for orbit in orbit_log[starting_point]:
        distance_map = build_distance_map(
            orbit_1, orbit_2, orbit_log, orbit, distance_map
        )
    return distance_map


# Part 2
def find_shortest_distance(distance_map: Dict[str, Tuple[int, int]]) -> Optional[int]:
    min_dist = None
    for key in distance_map.keys():
        distances = distance_map[key]
        if None not in distances:
            distance = distance_map[key][0] + distance_map[key][1]
            if not min_dist or min_dist > distance:
                min_dist = distance
    return min_dist


# Part 2
def find_min_orbital_transfers(
    orbit_log, orbit_1, orbit_2, system_starting_point
) -> Optional[int]:
    dist_map = build_distance_map(orbit_1, orbit_2, orbit_log, system_starting_point)
    # Subtract 2 because the node we orbit is considered the starting point, not YOU or SAN
    shortest_distance = find_shortest_distance(dist_map)
    if shortest_distance:
        return shortest_distance - 2
    else:
        return None


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").read().splitlines()
    orbit_log = build_orbit_log(data)
    total_orbits = count_children("COM", orbit_log, 0)
    print(total_orbits, "is answer to part 1")
    min_distance = find_min_orbital_transfers(orbit_log, "YOU", "SAN", "COM")
    print(min_distance, "is answer to part 2")


if __name__ == "__main__":
    main()
