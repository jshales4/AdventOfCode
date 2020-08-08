import pytest
from aoc_2019_04 import check_password_for_validity, check_password_for_validity_part2


@pytest.mark.parametrize(
    "test_input,expected", [(111111, True), [223450, False], [123789, False]]
)
def test_check_password_for_validity(test_input, expected):
    assert check_password_for_validity(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected", [(112233, True), [123444, False], [111122, True]]
)
def test_check_password_for_validity_part2(test_input, expected):
    assert check_password_for_validity_part2(test_input) == expected
