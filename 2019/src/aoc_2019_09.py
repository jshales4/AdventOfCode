# AoC 2019 Day 9
from typing import List, Optional, Tuple, Set, Dict
from aoc_2019_11 import (
    enact_robot_instruction,
    Direction,
    build_paintable_grid,
    render_painted_surface,
)
from enum import Enum
import collections

YEAR = 2019
DAY = 9


class Mode(Enum):
    IMMEDIATE_MODE = "IMMEDIATE_MODE"
    POSITION_MODE = "POSITION_MODE"
    RELATIVE_MODE = "RELATIVE_MODE"


def determine_parameter_type(param_type: int) -> Mode:
    if param_type == 0:
        return Mode.POSITION_MODE
    elif param_type == 2:
        return Mode.RELATIVE_MODE
    else:
        assert param_type == 1
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
    commands: Dict[int, int],
    input_instructions: List[int],
    noisy: bool = True,
    feedback_loop_mode=False,
    index=0,
    painting_mode=False,
) -> Tuple[List[Optional[int]], bool, int]:
    displayed_values: List[int] = []
    relative_base = 0
    while True:
        instruction, modes_for_program = determine_parameter_mode(commands[index])
        if instruction == 1:
            parameter_1, parameter_2 = pull_values_based_on_mode(
                commands, index, modes_for_program, relative_base
            )
            if modes_for_program[2] == Mode.RELATIVE_MODE:
                commands[commands[index + 3] + relative_base] = (
                    parameter_1 + parameter_2
                )
            else:
                assert modes_for_program[2] == Mode.POSITION_MODE
                commands[commands[index + 3]] = parameter_1 + parameter_2
            index += 4
        elif instruction == 2:
            parameter_1, parameter_2 = pull_values_based_on_mode(
                commands, index, modes_for_program, relative_base
            )
            if modes_for_program[2] == Mode.RELATIVE_MODE:
                commands[commands[index + 3] + relative_base] = (
                    parameter_1 * parameter_2
                )
            else:
                assert modes_for_program[2] == Mode.POSITION_MODE
                commands[commands[index + 3]] = parameter_1 * parameter_2
            index += 4
        elif instruction == 3:
            input_instruction = input_instructions.pop(0)
            if modes_for_program[0] == Mode.IMMEDIATE_MODE:
                commands[index + 1] = input_instruction
            elif modes_for_program[0] == Mode.RELATIVE_MODE:
                commands[commands[index + 1] + relative_base] = input_instruction
            else:
                assert modes_for_program[0] == Mode.POSITION_MODE
                commands[commands[index + 1]] = input_instruction
            index += 2
        elif instruction == 4:
            if modes_for_program[0] == Mode.IMMEDIATE_MODE:
                outputted_value = commands[index + 1]
            elif modes_for_program[0] == Mode.RELATIVE_MODE:
                outputted_value = commands[commands[index + 1] + relative_base]
            else:
                assert modes_for_program[0] == Mode.POSITION_MODE
                outputted_value = commands[commands[index + 1]]
            if noisy:
                print(outputted_value)
            displayed_values.append(outputted_value)
            if feedback_loop_mode:
                program_finished = False
                return displayed_values, program_finished, index + 2
            elif painting_mode:
                if len(displayed_values) > 1:
                    program_finished = False
                    return displayed_values, program_finished, index + 2
            index += 2
        elif instruction == 5:
            parameter_1, parameter_2 = pull_values_based_on_mode(
                commands, index, modes_for_program, relative_base
            )
            if parameter_1 != 0:
                index = parameter_2
            else:
                index += 3
        elif instruction == 6:
            parameter_1, parameter_2 = pull_values_based_on_mode(
                commands, index, modes_for_program, relative_base
            )
            if parameter_1 == 0:
                index = parameter_2

            else:
                index += 3

        elif instruction == 7:
            parameter_1, parameter_2 = pull_values_based_on_mode(
                commands, index, modes_for_program, relative_base
            )
            if parameter_1 < parameter_2:
                if modes_for_program[2] == Mode.RELATIVE_MODE:
                    commands[commands[index + 3] + relative_base] = 1
                else:
                    assert modes_for_program[2] == Mode.POSITION_MODE
                    commands[commands[index + 3]] = 1
            else:
                if modes_for_program[2] == Mode.RELATIVE_MODE:
                    commands[commands[index + 3] + relative_base] = 0
                else:
                    assert modes_for_program[2] == Mode.POSITION_MODE
                    commands[commands[index + 3]] = 0
            index += 4
        elif instruction == 8:
            parameter_1, parameter_2 = pull_values_based_on_mode(
                commands, index, modes_for_program, relative_base
            )
            if parameter_1 == parameter_2:
                if modes_for_program[2] == Mode.RELATIVE_MODE:
                    commands[commands[index + 3] + relative_base] = 1
                else:
                    assert modes_for_program[2] == Mode.POSITION_MODE
                    commands[commands[index + 3]] = 1
            else:
                if modes_for_program[2] == Mode.RELATIVE_MODE:
                    commands[commands[index + 3] + relative_base] = 0
                else:
                    assert modes_for_program[2] == Mode.POSITION_MODE
                    commands[commands[index + 3]] = 0
            index += 4

        elif instruction == 9:
            if modes_for_program[0] == Mode.IMMEDIATE_MODE:
                additional_base = commands[index + 1]
            elif modes_for_program[0] == Mode.RELATIVE_MODE:
                additional_base = commands[commands[index + 1] + relative_base]
            else:
                assert modes_for_program[0] == Mode.POSITION_MODE
                additional_base = commands[commands[index + 1]]
            relative_base += additional_base
            index += 2
        else:
            assert instruction == 99
            program_finished = True
            if feedback_loop_mode:
                return input_instructions, program_finished, 0
            else:
                return displayed_values, program_finished, 0


def pull_values_based_on_mode(commands, index, modes_for_program, relative_base):
    if modes_for_program[0] == Mode.IMMEDIATE_MODE:
        parameter_1 = commands[index + 1]
    elif modes_for_program[0] == Mode.RELATIVE_MODE:
        parameter_1 = commands[commands[index + 1] + relative_base]
    else:
        parameter_1 = commands[commands[index + 1]]
        assert modes_for_program[0] == Mode.POSITION_MODE
    if modes_for_program[1] == Mode.IMMEDIATE_MODE:
        parameter_2 = commands[index + 2]
    elif modes_for_program[1] == Mode.RELATIVE_MODE:
        parameter_2 = commands[commands[index + 2] + relative_base]
    else:
        parameter_2 = commands[commands[index + 2]]
        assert modes_for_program[1] == Mode.POSITION_MODE
    return parameter_1, parameter_2


def create_fresh_program(program_strs: List[str]) -> Dict[int, int]:
    program = collections.defaultdict(int)
    for k, v in enumerate([int(command) for command in program_strs]):
        program[k] = v
    return program


def parse_intcode_program(
    data_file: List[str],
    program_input: int,
    noisy: bool,
    feedback_loop_mode: bool = False,
    painting_mode=False,
) -> List[Optional[int]]:
    """Takes an intcode program as an input, formats it, and returns a list of everything output."""
    program_strs = data_file[0].split(",")
    program = create_fresh_program(program_strs)
    outputed_values = []
    if feedback_loop_mode:
        displayed_values, finished, index = step_through_program(
            program,
            input_instructions=[program_input],
            noisy=noisy,
            feedback_loop_mode=feedback_loop_mode,
            painting_mode=painting_mode,
        )
        outputed_values.append(displayed_values[0])
    elif painting_mode:
        is_finished = False
        paintable_surface = build_paintable_grid()
        set_of_visited_squares: List[Tuple[int, int]] = []
        current_direction = Direction.NORTH  # part of the spec
        current_position = (50, 50)
        index = 0
        while not is_finished:
            print(index)
            print(program)
            print(program[index])
            displayed_values, is_finished, index = step_through_program(
                program,
                input_instructions=[program_input],
                noisy=noisy,
                feedback_loop_mode=False,
                painting_mode=True,
                index=index,
            )
            if not is_finished:
                set_of_visited_squares.append(current_position)
                assert len(displayed_values) == 2
                should_paint_white, movement_instruction = displayed_values
                (
                    paintable_surface,
                    current_direction,
                    current_position,
                    current_position_color,
                ) = enact_robot_instruction(
                    map=paintable_surface,
                    current_pos=current_position,
                    current_direction=Direction(current_direction),
                    movement_instruction=movement_instruction,
                    should_paint_white=bool(should_paint_white),
                )
                if current_position_color:
                    program_input = 1
                else:
                    program_input = 0
        print(len(set(set_of_visited_squares)))
        render_painted_surface(paintable_surface)
    else:
        displayed_values, _, _ = step_through_program(
            program,
            input_instructions=[program_input],
            noisy=noisy,
            feedback_loop_mode=False,
            painting_mode=False,
        )
        outputed_values.extend(displayed_values)

    return outputed_values


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    displayed_values = parse_intcode_program(data, program_input=1, noisy=False)
    print(displayed_values[0], "is the answer to part 1")
    displayed_values = parse_intcode_program(data, program_input=2, noisy=False)
    print(displayed_values[0], "is the answer to part 2")


if __name__ == "__main__":
    main()
