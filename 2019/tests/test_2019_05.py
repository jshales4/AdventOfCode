import pytest
from intcode import Computer
from aoc_2019_05 import determine_parameter_mode, step_through_program, Mode


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (1002, (2, [Mode.POSITION_MODE, Mode.IMMEDIATE_MODE, Mode.POSITION_MODE])),
        (2, (2, [Mode.POSITION_MODE, Mode.POSITION_MODE, Mode.POSITION_MODE])),
    ],
)
def test_determine_parameter_mode(test_input, expected):
    assert determine_parameter_mode(test_input) == expected


@pytest.mark.parametrize(
    "test_instructions,program_input,expected_output",
    [
        ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8, 1),
        ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 7, 0),
        ([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 9, 0),
        ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 7, 1),
        ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 8, 0),
        ([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 9, 0),
        ([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8, 1),
        ([3, 3, 1108, -1, 8, 3, 4, 3, 99], 7, 0),
        ([3, 3, 1108, -1, 8, 3, 4, 3, 99], 9, 0),
        ([3, 3, 1107, -1, 8, 3, 4, 3, 99], 7, 1),
        ([3, 3, 1107, -1, 8, 3, 4, 3, 99], 8, 0),
        ([3, 3, 1107, -1, 8, 3, 4, 3, 99], 9, 0),
        ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 1, 1),
        ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 0, 0),
        ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 1, 1),
        ([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 0, 0),
    ],
)
def test_stepping_through_program_skip_aheads(
    test_instructions, program_input, expected_output
):
    computer = Computer(program=test_instructions, inputs=[program_input])
    assert computer.execute_program() == [expected_output]
