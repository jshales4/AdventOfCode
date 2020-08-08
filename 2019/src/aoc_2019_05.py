# AoC Day 5
from typing import List, Optional, Tuple
from enum import Enum
from intcode import Computer

YEAR = 2019
DAY = 5


class Mode(Enum):
    IMMEDIATE_MODE = "IMMEDIATE_MODE"
    POSITION_MODE = "POSITION_MODE"


def determine_parameter_type(type: int) -> Mode:
    if type == 0:
        return Mode.POSITION_MODE
    else:
        assert type == 1
        return Mode.IMMEDIATE_MODE


def determine_parameter_mode(parameter: int) -> Tuple[int, List[Mode]]:
    instruction = parameter % 100
    parameter = parameter // 100
    modes: List[Mode] = []
    for _ in range(3):
        modes.append(determine_parameter_type(parameter % 10))
        parameter = parameter // 10
    return instruction, modes


def step_through_program(
    commands: List[int], input_instructions: List[int], noisy:bool = True, feedback_loop_mode=False, index=0
) -> Tuple[List[Optional[int]], bool, int]:
    displayed_values: List[int] = []
    while True:
        instruction, modes_for_program = determine_parameter_mode(commands[index])
        if instruction == 1:
            parameter_1, parameter_2 = pull_values_based_on_mode(
                commands, index, modes_for_program
            )
            commands[commands[index + 3]] = parameter_1 + parameter_2
            index += 4
        elif instruction == 2:
            parameter_1, parameter_2 = pull_values_based_on_mode(
                commands, index, modes_for_program
            )
            commands[commands[index + 3]] = parameter_1 * parameter_2
            index += 4
        elif instruction == 3:
            input_instruction = input_instructions.pop(0)
            if modes_for_program[0] == Mode.IMMEDIATE_MODE:
                commands[index + 1] = input_instruction
            else:
                commands[commands[index + 1]] = input_instruction
            index += 2
        elif instruction == 4:
            if modes_for_program[0] == Mode.IMMEDIATE_MODE:
                value = commands[index + 1]
            else:
                value = commands[commands[index + 1]]
            if noisy:
                print(value)
            displayed_values.append(value)
            if feedback_loop_mode:
                program_finished = False
                return displayed_values, program_finished, index+2
            index += 2
        elif instruction == 5:
            parameter_1, parameter_2 = pull_values_based_on_mode(
                commands, index, modes_for_program
            )
            if parameter_1 != 0:
                index = parameter_2
            else:
                index += 3
        elif instruction == 6:
            parameter_1, parameter_2 = pull_values_based_on_mode(
                commands, index, modes_for_program
            )
            if parameter_1 == 0:
                index = parameter_2

            else:
                index += 3

        elif instruction == 7:
            parameter_1, parameter_2 = pull_values_based_on_mode(
                commands, index, modes_for_program
            )
            if parameter_1 < parameter_2:
                commands[commands[index + 3]] = 1
            else:
                commands[commands[index + 3]] = 0
            index += 4
        elif instruction == 8:
            parameter_1, parameter_2 = pull_values_based_on_mode(
                commands, index, modes_for_program
            )
            if parameter_1 == parameter_2:
                commands[commands[index + 3]] = 1
            else:
                commands[commands[index + 3]] = 0
            index += 4

        else:
            assert instruction == 99
            program_finished = True
            if feedback_loop_mode:
                return input_instructions, program_finished, 0
            else:
                return displayed_values, program_finished, 0


def pull_values_based_on_mode(commands, index, modes_for_program):
    if modes_for_program[0] == Mode.IMMEDIATE_MODE:
        parameter_1 = commands[index + 1]
    else:
        parameter_1 = commands[commands[index + 1]]
    if modes_for_program[1] == Mode.IMMEDIATE_MODE:
        parameter_2 = commands[index + 2]
    else:
        parameter_2 = commands[commands[index + 2]]
    assert modes_for_program[2] == Mode.POSITION_MODE
    return parameter_1, parameter_2


def create_fresh_program(program_strs):
    program = [int(command) for command in program_strs]
    return program


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    program_strs = data[0].split(",")
    program = create_fresh_program(program_strs)
    computer = Computer(program=program, inputs=[1])
    output = computer.execute_program()
    print(output, "is the answer to part 1")
    computer = Computer(program=program, inputs=[5])
    output = computer.execute_program()
    print(output, "is the answer to part 2")
    # displayed_values = step_through_program(program, input_instructions=[1], noisy=False)
    # print(displayed_values[0][len(displayed_values[0]) - 1], "is answer to part 1")
    # program = create_fresh_program(program_strs)
    # displayed_values = step_through_program(program, input_instructions=[5], noisy=False)
    # print(displayed_values[0][0], "is answer to part 2")



if __name__ == "__main__":
    main()
