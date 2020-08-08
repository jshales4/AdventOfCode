# AoC 2019 Day 4

from typing import Tuple, List

YEAR = 2019
DAY = 4

# Part 1
def are_two_adjacent_numbers_same(password_split: List[str]) -> bool:
    for p in range(0, len(password_split) - 1):
        if password_split[p] == password_split[p + 1]:
            return True
    return False


# Part 2
def are_two_adjacent_numbers_same_part2(password_split: List[str]) -> bool:
    for p in range(0, len(password_split) - 1):
        if password_split[p] == password_split[p + 1]:
            if not (
                p > 0
                and password_split[p - 1] == password_split[p]
                or (
                    p < len(password_split) - 2
                    and password_split[p + 2] == password_split[p + 1]
                )
            ):
                return True
    return False


def are_digits_increasing(password_split: List[str]) -> bool:
    for i in range(0, len(password_split) - 1):
        if password_split[i] > password_split[i + 1]:
            return False
    return True


# Part 1
def check_password_for_validity(password: int) -> bool:
    password_split = [i for i in str(password)]
    return not (
        password < 100000
        or password > 999999
        or not are_two_adjacent_numbers_same(password_split)
        or not are_digits_increasing(password_split)
    )


# Part 2
def check_password_for_validity_part2(password: int) -> bool:
    password_split = [i for i in str(password)]
    return not (
        password < 100000
        or password > 999999
        or not are_two_adjacent_numbers_same_part2(password_split)
        or not are_digits_increasing(password_split)
    )


def split_range_into_parts(range: str) -> Tuple[int, int]:
    low, high = range.split("-")
    return int(low), int(high)


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    low, high = split_range_into_parts(data[0])
    potential_passwords = 0
    potential_passwords_part2 = 0
    for password in range(low, high + 1):
        if check_password_for_validity(password):
            potential_passwords += 1
        if check_password_for_validity_part2(password):
            potential_passwords_part2 += 1
    print(potential_passwords, "is the answer to Part 1")
    print(potential_passwords_part2, "is the answer to Part 2")


if __name__ == "__main__":
    main()
