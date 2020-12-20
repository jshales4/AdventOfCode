from typing import List, Optional

YEAR = 2020
DAY = 8


class ProgramState:
    accumulator: int
    is_working_program: bool

    def __init__(self, accumulator, is_working_program):
        self.accumulator = accumulator
        self.is_working_program = is_working_program


def parse_command(command_str: str) -> (str, int):
    command, magnitude = command_str.split(" ")
    return command, int(magnitude)


def run_program(
    commands: List[str], index_to_flip: Optional[int] = None
) -> ProgramState:
    command_index = 0
    accumulator = 0
    visited_indexes: List[int] = [command_index]
    while True:
        try:
            command, magnitude = parse_command(commands[command_index])
        except IndexError:
            return ProgramState(accumulator, True)
        if command_index == index_to_flip:
            if command == "jmp":
                command = "nop"
            elif command == "nop":
                command = "jmp"
            else:
                pass
        if command == "acc":
            accumulator += magnitude
            command_index += 1
        elif command == "jmp":
            command_index += magnitude
        else:
            assert command == "nop"
            command_index += 1
        if command_index in visited_indexes:
            return ProgramState(accumulator, False)
        else:
            visited_indexes.append(command_index)


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    print(run_program(data).accumulator, "is the answer to part 1.")
    for index in range(len(data)):
        state = run_program(data, index)
        if state.is_working_program:
            print(state.accumulator, "is the answer to part 2.")
            break


if __name__ == "__main__":
    main()
