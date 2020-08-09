from aoc_2016_02 import parse_position_on_keypad, determine_numpad_position

def test_parse_keypad():
   assert parse_position_on_keypad(11) == 5
   assert parse_position_on_keypad(21) == 8
   assert parse_position_on_keypad(1) == 2
   assert parse_position_on_keypad(0) == 1
   assert parse_position_on_keypad(22) == 9



def test_determine_numpad_position():
    # cases where they moved
    assert determine_numpad_position(11, "L") == 10
    assert determine_numpad_position(11, "R") == 12
    assert determine_numpad_position(11, "D") == 21
    assert determine_numpad_position(11, "U") == 1

    # cases where on edge
    assert determine_numpad_position(0, "L") == 0
    assert determine_numpad_position(12, "R") == 12
    assert determine_numpad_position(21, "D") == 21
    assert determine_numpad_position(1, "U") == 1



