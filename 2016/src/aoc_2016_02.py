# AoC 2016 Day 2
from typing import List, Union

YEAR = 2016
DAY = 2


def parse_position_on_keypad(position: int, keypad: List[List[Union[str, int]]]) -> int:
    second_index = position % 10
    first_index = (position - second_index) // 10
    return keypad[first_index][second_index]


def move_if_possible(
    current_position: int,
    delta: int,
    acceptable_keypad_positions: List[Union[str, int]],
) -> int:
    if current_position + delta in acceptable_keypad_positions:
        return current_position + delta
    else:
        return current_position


def parse_instruction(
    current_position: int, instruction: str, acceptable_positions: List[Union[str, int]]
) -> int:
    if instruction == "L":
        delta = -1
    elif instruction == "R":
        delta = 1
    elif instruction == "U":
        delta = -10
    else:
        assert instruction == "D"
        delta = 10
    return move_if_possible(current_position, delta, acceptable_positions)


def main():
    current_position = 11
    data = open(f"../input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    code: List[int] = []
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for line in data:
        line = line.rstrip()
        for instruction in line:
            current_position = parse_instruction(
                current_position, instruction, [0, 1, 2, 10, 11, 12, 20, 21, 22]
            )

        code.append(parse_position_on_keypad(current_position, keypad))
    print("Answer to part 1:", code)

    # part 2
    print("begin part 2")
    current_position = 11
    code: List[Union[str, int]] = []
    for line in data:
        line = line.rstrip()
        for instruction in line:
            current_position = parse_instruction(
                current_position,
                instruction,
                [2, 11, 12, 13, 20, 21, 22, 23, 24, 31, 32, 33, 42],
            )
        code.append(
            parse_position_on_keypad(
                current_position,
                keypad=[
                    [0, 0, 1, 0, 0],
                    [0, 2, 3, 4, 0],
                    [5, 6, 7, 8, 9],
                    [0, "A", "B", "C", 0],
                    [0, 0, "D", 0, 0],
                ],
            )
        )
    print("Answer to part 2:", code)


if __name__ == "__main__":
    main()
