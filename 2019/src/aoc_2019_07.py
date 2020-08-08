# AoC 2019 Day 7
from aoc_2019_02 import create_fresh_program
from aoc_2019_05 import step_through_program
from intcode import Computer
from typing import Tuple, List
from itertools import permutations

YEAR = 2019
DAY = 7


def get_settings_ranges(min_setting: int, max_setting:int) -> List[Tuple[int, ...]]:
    return list(permutations(range(min_setting, max_setting + 1)))


def get_output_for_setting(
    instructions: List[int], phase_setting_sequence: Tuple[int, ...]
) -> int:
    new_input = 0
    for i in phase_setting_sequence:
        computer = Computer(program=instructions, inputs=[i, new_input])
        output = computer.execute_program()
        new_input = output[0]
    return new_input


def highest_possible_feedback_mode(
    instructions: List[int], phase_setting_sequence: Tuple[int, ...]
):
    new_input = 0
    finished = False
    computers = [Computer(instructions, []) for i in range(5)]
    # each_program: List[List[int]] = []
    # for i in range(5):
    #     each_program.append(instructions.copy())
    # states_of_each_program = [0, 0, 0, 0, 0]
    for i, phase in enumerate(phase_setting_sequence):
        print(new_input)
        computer = computers[i]
        computer.inputs = [phase, new_input]
        new_input = computer.execute_program()
    while not computers[4].halted:
        print(new_input)
        for i in phase_setting_sequence:
            computer = computers[i]
            if computer.paused:
                computer.paused = False
            assert computer.inputs == []
            computer.inputs = [new_input]
            new_input = computer.execute_program()
    print(new_input, "new input")
        # for i in phase_setting_sequence:
        #     new_inputs, finished, index = step_through_program(
        #         each_program[i - 5],
        #         [new_input],
        #         noisy=False,
        #         feedback_loop_mode=True,
        #         index=states_of_each_program[i - 5],
        #     )
        #     states_of_each_program[i - 5] = index
        #     new_input = new_inputs[0]
    return new_input


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    program_strs = data[0].split(",")
    program = create_fresh_program(program_strs)
    all_possible_phase_settings = get_settings_ranges(0, 4)
    current_max = 0
    for setting in all_possible_phase_settings:
        output = get_output_for_setting(program, setting)
        if output > current_max:
            current_max = output
    print(current_max, "is answer to part 1")
    program = create_fresh_program(program_strs)
    all_possible_phase_settings = get_settings_ranges(5, 9)
    current_max = 0
    for setting in all_possible_phase_settings:
        output = highest_possible_feedback_mode(program, setting)
        if output > current_max:
            current_max = output
    print(current_max, "is answer to part 2")


if __name__ == "__main__":
    main()
