# AoC 2016 Day 3

from typing import List

YEAR = 2016
DAY = 3


def main():
    data = open(f"../input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    data = [list(map(int, row.split())) for row in data]
    counter = 0
    for triangle in data:
        if is_valid_triangle(triangle):
            counter += 1
    print(counter, "is answer to part 1")

    counter = 0
    print(len(data) % 3)
    for index in range(len(data)):
        if index % 3 != 0:
            continue
        for i in range(3):
            counter += 1 * is_valid_triangle([data[index][i], data[index+1][i], data[index+2][i]])

    print(counter, "is the answer to part 2")

    
def is_valid_triangle(triangle: List[int])->bool:
    triangle = sorted(triangle)
    return triangle[0] + triangle[1] > triangle[2]


if __name__ == "__main__":
    main()
