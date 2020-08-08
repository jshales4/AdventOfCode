from typing import Dict, List, Tuple, Optional


class Computer:
    def __init__(self, program, inputs):
        self.program: Dict[int, int] = dict(zip(range(len(program)), program))
        self.inputs: List[int] = inputs
        self.outputted_values: List[int] = []
        self.index = 0
        self.paused = False
        self.halted = False
        self.base = 0

    def execute_program(self):
        while not self.halted and not self.paused:
            self.parse_opcode()
        return self.outputted_values

    def seperate_modes_from_opcode(self, full_opcode) -> List[int]:
        opcode_and_modes = [int(i) for i in list(str(full_opcode).rjust(5, "0"))]
        return opcode_and_modes

    def parse_opcode(self) -> List[Optional[int]]:
        (full_opcode, location1, location2, location3) = [
            self.program.get(i, 0) for i in range(self.index, self.index + 4)
        ]
        mode3, mode2, mode1, opcode1, opcode2 = self.seperate_modes_from_opcode(full_opcode)
        opcode = opcode1 * 10 + opcode2
        param1 = self.get_param(mode1, location1)
        param2 = self.get_param(mode2, location2)
        param3 = self.set_param(mode3, location3)
        if opcode == 1:
            self.program[param3] = param1 + param2
            self.move_through_program(4)
        elif opcode == 2:
            self.program[param3] = param1 * param2
            self.move_through_program(4)
        elif opcode == 3:
            if len(self.inputs) > 0:
                instruction = self.inputs.pop(0)
                self.program[location1] = instruction
                self.move_through_program(2)
            else:
                self.paused = True
                return self.outputted_values
        elif opcode == 4:
            outputted_value = param1
            self.outputted_values.append(outputted_value)
            self.move_through_program(2)
        elif opcode == 5:
            if param1 != 0:
                self.index = param2
            else:
                self.move_through_program(3)
        elif opcode == 6:
            if param1 == 0:
                self.index = param2
            else:
                self.move_through_program(3)
        elif opcode == 7:
            if param1 < param2:
                self.program[param3] = 1
            else:
                self.program[param3] = 0
            self.move_through_program(4)
        elif opcode == 8:
            if param1 == param2:
                self.program[param3] = 1
            else:
                self.program[param3] = 0
            self.move_through_program(4)
        else:
            assert opcode == 99
            self.halted = True
            return self.outputted_values

    def move_through_program(self, movement: int) -> None:
        self.index += movement

    def get_param(self, mode, location):
        if mode == 0:
            return self.program.get(location)
        elif mode == 1:
            return location
        else:
            assert None

    def set_param(self, mode, value):
        """Returns the location to set the value"""
        if mode == 0:
            return value
        else:
            assert False
