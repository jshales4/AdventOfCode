# 2018 Day 1

from typing import List, Tuple, Optional, Dict

YEAR = 2018
DAY = 1


def calculate_frequency(
    frequencies: List[str],
    starting_frequency: Optional[int] = None,
    already_visited_frequencies: Optional[List[int]] = None,
) -> Tuple[int, Optional[int]]:

    current_frequency: int = starting_frequency or 0
    visited_frequencies: List[int] = already_visited_frequencies or [current_frequency]
    double_passed_frequency: Optional[int] = None

    for frequency in frequencies:
        current_frequency += parse_frequency(frequency)
        if double_passed_frequency is None:
            if current_frequency in visited_frequencies:
                double_passed_frequency = current_frequency
            else:
                visited_frequencies.append(current_frequency)

    if double_passed_frequency is None:
        _, double_passed_frequency = calculate_frequency(
            frequencies,
            starting_frequency=current_frequency,
            already_visited_frequencies=visited_frequencies,
        )
    assert double_passed_frequency is not None
    return current_frequency, double_passed_frequency


def parse_frequency(frequency: str) -> int:
    if frequency in ["", "0"]:
        return 0
    elif frequency[0] == "-":
        return -1 * int(frequency[1:])
    else:
        return int(frequency[1:])


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    net_frequency, double_visited_frequency = calculate_frequency(data)
    print(net_frequency, "is the part 1 answer")
    print(double_visited_frequency, "is the part 2 answer")


if __name__ == "__main__":
    main()
