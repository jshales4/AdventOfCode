from typing import List

YEAR = 2020
DAY = 9


def is_number_sum_of_priors(priors: List[int], number: int) -> bool:
    for i in range(len(priors)):
        for j in range(i, len(priors)):
            if priors[i] + priors[j] == number:
                return True
    else:
        return False


def find_sum_range(searched_number: int, data: List[int]) -> List[int]:
    for i in range(len(data)):
        number = data[i]
        index_offset = 1
        while number < searched_number:
            number += data[i + index_offset]
            if number == searched_number:
                return data[i : i + index_offset + 1]
            index_offset += 1


def find_smallest_and_largest_in_range_then_sum(addends: List[int]) -> int:
    return min(addends) + max(addends)


def main():
    data = [
        int(i) for i in open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    ]
    PREAMBLE_SIZE = 25
    SEARCHED_NUMBER = 1504371145
    for i in range(len(data)):
        if i < PREAMBLE_SIZE:
            continue
        if not is_number_sum_of_priors(data[(i - PREAMBLE_SIZE) : i], data[i]):
            print(data[i])

    continguous_sum = find_sum_range(SEARCHED_NUMBER, data)

    print(
        find_smallest_and_largest_in_range_then_sum(continguous_sum),
        "is the answer to part 2.",
    )


if __name__ == "__main__":
    main()
