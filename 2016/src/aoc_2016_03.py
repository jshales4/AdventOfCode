# AoC 2016 Day 3

from typing import List

YEAR = 2016
DAY = 3


def is_valid_triangle(triangle: List[int]) -> bool:
    triangle = sorted(triangle)
    return triangle[0] + triangle[1] > triangle[2]


def main():
    data = open(f"../input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    triangles = [list(map(int, row.split())) for row in data]
    counter_part1, counter_part2 = 0, 0
    for index in range(len(triangles)):
        if is_valid_triangle(triangles[index]):
            counter_part1 += 1
        if index % 3 != 0:
            continue
        for i in range(3):
            counter_part2 += 1 * is_valid_triangle(
                [triangles[index][i], triangles[index + 1][i], triangles[index + 2][i]]
            )

    print(counter_part1, "is the answer to part 1")
    print(counter_part2, "is the answer to part 2")


if __name__ == "__main__":
    main()
