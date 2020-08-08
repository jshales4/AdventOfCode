import pytest
from math import atan2
from aoc_2019_10 import (
    find_nth_asteroid_destroyed,
    build_asteroid_position_list,
    count_visible_asteroids,
    build_relative_asteroid_map,
    find_asteroid_with_max_visibles,
)


def test_build_asteroid_position_list():
    assert build_asteroid_position_list([".#.", "...", "###"]) == [
        (1, 0),
        (0, 2),
        (1, 2),
        (2, 2),
    ]


@pytest.mark.parametrize(
    "asteroids,index,expected",
    (
        [
            ([".#..#", ".....", "#####", "....#", "...##"], 0, 7),
            ([".#..#", ".....", "#####", "....#", "...##"], 1, 7),
            ([".#..#", ".....", "#####", "....#", "...##"], 2, 6),
            ([".#..#", ".....", "#####", "....#", "...##"], 3, 7),
            ([".#..#", ".....", "#####", "....#", "...##"], 4, 7),
            ([".#..#", ".....", "#####", "....#", "...##"], 5, 7),
            ([".#..#", ".....", "#####", "....#", "...##"], 6, 5),
            ([".#..#", ".....", "#####", "....#", "...##"], 7, 7),
            ([".#..#", ".....", "#####", "....#", "...##"], 8, 8),
            ([".#..#", ".....", "#####", "....#", "...##"], 9, 7),
        ]
    ),
)
def test_count_visible_asteroids(asteroids, index, expected):
    asteroids = build_asteroid_position_list(asteroids)
    # print(asteroids)
    assert count_visible_asteroids(index, asteroids) == expected


@pytest.mark.parametrize("number,x,y", ([(1, 11, 12), (2, 12, 1),]))
def test_laser_betting(number, x, y):
    input = [
        ".#..##.###...#######",
        "##.############..##.",
        ".#.######.########.#",
        ".###.#######.####.#.",
        "#####.##.#.##.###.##",
        "..#####..#.#########",
        "####################",
        "#.####....###.#.#.##",
        "##.#################",
        "#####.##.###..####..",
        "..######..##.#######",
        "####.##.####...##..#",
        ".#####..#.######.###",
        "##...#.##########...",
        "#.##########.#######",
        ".####.#.###.###.#.##",
        "....##.##.###..#####",
        ".#.#.###########.###",
        "#.#.#.#####.####.###",
        "###.##.####.##.#..##",
    ]
    pos_list = build_asteroid_position_list(input)
    base_asteroid, max = find_asteroid_with_max_visibles(pos_list)
    assert max == 210
    assert pos_list[base_asteroid].x == 11
    assert pos_list[base_asteroid].y == 13
    nth_asteroid = find_nth_asteroid_destroyed(pos_list, base_asteroid, number)
    assert nth_asteroid.x == x
    assert nth_asteroid.y == y
