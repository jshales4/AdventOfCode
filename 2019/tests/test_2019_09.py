import pytest
from aoc_2019_09 import step_through_program, create_fresh_program


# Part 2 was visual so harder to test
@pytest.mark.parametrize(
    "program_strs,output",
    (
        [
            ([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]),
            ([104,1125899906842624,99], [1125899906842624]),
            ([1102,34915192,34915192,7,4,7,99,0], [1219070632396864]),
        ]
    ),
)
def test_program_features(program_strs, output):
    program = create_fresh_program(program_strs)
    assert (output, True, 0) == step_through_program(program, [], noisy=False)

