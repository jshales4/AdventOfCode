from typing import Optional, List
from operator import mul
from functools import reduce

YEAR = 2020
DAY = 3


def count_trees_in_path(x_delta: int, y_delta: int, rows: List[List[str]]) -> int:
    row_pos = 0
    column_pos = 0
    tree_counter = 0
    for row in rows:
        if row_pos % abs(y_delta) == 0:
            if row[column_pos] == "#":
                tree_counter += 1
            column_pos = (column_pos + x_delta) % (len(row) - 1)
        row_pos -= 1
    return tree_counter


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    slopes_to_try = [(1, -1), (3, -1), (5, -1), (7, -1), (1, -2)]
    trees_encountered: List[int] = []
    for slope in slopes_to_try:
        trees_encountered.append(count_trees_in_path(slope[0], slope[1], data))
    print(trees_encountered[1], "total trees in path for part 1.")
    print(reduce(mul, trees_encountered, 1), "total trees in path for part 2.")


if __name__ == "__main__":
    main()
