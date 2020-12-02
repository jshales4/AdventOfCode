from aoc_2020_02 import is_valid_password_part1, is_valid_password_part2


def test_password_valid_part1():
    assert is_valid_password_part1("1-3 a", "abcde")
    assert not is_valid_password_part1("1-3 b", "cdefg")
    assert is_valid_password_part1("2-9 c", "ccccccccc")


def test_password_valid_part2():
    assert is_valid_password_part2("1-3 a", "abcde")
    assert not is_valid_password_part2("1-3 b", "cdefg")
    assert not is_valid_password_part2("2-9 c", "ccccccccc")
