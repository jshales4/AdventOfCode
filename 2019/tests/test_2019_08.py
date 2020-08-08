import pytest
from aoc_2019_08 import validate_image


# Part 2 was visual so harder to test
def test_validate_image():
    assert validate_image("123456789012", 3, 2) == 1
    assert validate_image("100456782012", 3, 2) == 2
