# AoC 2019 Day 2

from typing import List, Optional, Tuple
from intcode import Computer

YEAR = 2019
DAY = 2

def create_fresh_program(program_strs):
    program = [int(command) for command in program_strs]
    return program


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    program_strs = data[0].split(",")
    program = create_fresh_program(program_strs)
    computer = Computer(program, [])
    computer.program[1] = 12
    computer.program[2] = 2
    computer.execute_program()
    print(computer.program[0], "is the answer to part 1")
    desired_output = 19690720
    for i in range(100):
        for j in range(100):
            computer = Computer(program, [])
            computer.program[1] = i
            computer.program[2] = j
            computer.execute_program()
            if int(computer.program[0]) == desired_output:
                print(i*100+j, "is the answer to part 2")


if __name__ == "__main__":
    main()
