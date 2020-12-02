from aoc_2020_01 import _find_sum_to_value


def test_find_numbers_sum_to_n():
    assert _find_sum_to_value(5, [2, 1, 7, 3], 2) == [2, 3]
    assert _find_sum_to_value(6, [2, 1, 7, 3], 3) == [1, 2, 3]



