import pytest
from aoc_2019_06 import (
    count_children,
    build_orbit_log,
    find_distance,
    build_distance_map,
    find_shortest_distance,
)


def test_count_children():
    instructions = [
        "COM)B",
        "B)C",
        "C)D",
        "D)E",
        "E)F",
        "B)G",
        "G)H",
        "D)I",
        "E)J",
        "J)K",
        "K)L",
    ]
    orbit_log = build_orbit_log(instructions)
    assert count_children("COM", orbit_log, 0) == 42


def test_find_distance():
    instructions = [
        "COM)B",
        "B)C",
        "C)D",
        "D)E",
        "E)F",
        "B)G",
        "G)H",
        "D)I",
        "E)J",
        "J)K",
        "K)L",
    ]
    orbit_log = build_orbit_log(instructions)
    assert find_distance("D", orbit_log, "K") == 3
    assert find_distance("K", orbit_log, "D") is None
    distance_map = build_distance_map("L", "I", orbit_log, "COM")
    assert distance_map["D"] == (4, 1)
    assert find_shortest_distance(distance_map) == 5
