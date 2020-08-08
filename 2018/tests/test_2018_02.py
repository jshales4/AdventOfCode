import pytest
from aoc_2018_02 import (
    count_letter,
    calculate_doubles_and_triples,
    get_possible_box_ids,
)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("abcdef", (False, False)),
        ("bababc", (True, True)),
        ("abbcde", (True, False)),
        ("abcccd", (False, True)),
        ("aabcdd", (True, False)),
        ("abcdee", (True, False)),
        ("ababab", (False, True)),
    ],
)
def test_count_letter(test_input, expected):
    assert count_letter(test_input) == expected


def test_calculate_doubles_and_triples():
    assert calculate_doubles_and_triples(
        (["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab",])
    ) == (4, 3)


def test_get_possible_box_ids():
    assert (
        get_possible_box_ids(
            ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
        )
        == "fgij"
    )
