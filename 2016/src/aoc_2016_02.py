# AoC 2016 Day 2

YEAR = 2016
DAY = 2


def parse_position_on_keypad(position: int) -> int:
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert position in [0, 1, 2, 10, 11, 12, 20, 21, 22]
    second_index = position % 10
    first_index = (position - second_index) // 10
    return keypad[first_index][second_index]


def determine_numpad_position(current_position, instruction) -> int:
    if instruction == "L":
        current_position = max(current_position - 1, round(current_position / 10) * 10)
    elif instruction == "R":
        current_position = min(
            current_position + 1, round(current_position / 10) * 10 + 2
        )
    elif instruction == "U":
        current_position = max(current_position - 10, current_position % 10)
    else:
        assert instruction != "D"
        current_position = min(current_position + 10, (current_position % 10) + 20)
    return current_position



def main():
    current_position = 11
    data = open(f"../input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    for line in data:
        line = line.rstrip()
        for instruction in line:
            current_position = determine_numpad_position(current_position, instruction)

        print(parse_position_on_keypad(current_position))


if __name__ == "__main__":
    main()
