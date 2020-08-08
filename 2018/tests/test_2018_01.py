import pytest
from aoc_2018_01 import parse_frequency, calculate_frequency


@pytest.mark.parametrize("test_input,expected", [("0", 0), ("+1", 1), ("-2", -2)])
def test_parse_frequency(test_input, expected):
    assert parse_frequency(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["+1", "-1"], 0),
        (["+3", "+3", "+4", "-2", "-4"], 10),
        (["-6", "+3", "+8", "+5", "-6"], 5),
        (["+7", "+7", "-2", "-7", "-4"], 14),
        (["+7", "+7", "-2", "-7", "-4", ""], 14),
    ],
)
def test_calculate_frequency(test_input, expected):
    assert calculate_frequency(test_input)[1] == expected
