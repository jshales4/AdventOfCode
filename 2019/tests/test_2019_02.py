import pytest
from intcode import Computer


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
            {
                0: 3500,
                1: 9,
                2: 10,
                3: 70,
                4: 2,
                5: 3,
                6: 11,
                7: 0,
                8: 99,
                9: 30,
                10: 40,
                11: 50,
            },
        ),
        ([1, 0, 0, 0, 99], {0: 2, 1: 0, 2: 0, 3: 0, 4: 99}),
        ([2, 3, 0, 3, 99], {0: 2, 1: 3, 2: 0, 3: 6, 4: 99}),
        ([2, 4, 4, 5, 99, 0], {0: 2, 1: 4, 2: 4, 3: 5, 4: 99, 5: 9801}),
        (
            [1, 1, 1, 4, 99, 5, 6, 0, 99],
            {0: 30, 1: 1, 2: 1, 3: 4, 4: 2, 5: 5, 6: 6, 7: 0, 8: 99},
        ),
    ],
)
def test_step_through_program(test_input, expected):
    computer = Computer(test_input, [])
    computer.execute_program()
    assert computer.program == expected
