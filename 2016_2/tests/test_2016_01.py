from aoc_2016_01 import get_new_direction, Direction, Position

def test_directions():
    position = Position(0,0,Direction.NORTH)
    assert get_new_direction(position, "L").direction == Direction.WEST
    position = Position(0,0,Direction.NORTH)
    assert get_new_direction(position, "R").direction == Direction.EAST


