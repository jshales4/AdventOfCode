from aoc_2020_11 import find_final_seat_state, count_occupied_seats, render_seats


def test_count_seats():

    initial_rows = [
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL",
    ]
    initial_seats = [list(i) for i in initial_rows]

    seats = find_final_seat_state(initial_seats)
    render_seats(seats)
    assert count_occupied_seats(seats) == 37


def test_count_seats_pt2():

    initial_rows = [
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL",
    ]
    initial_seats = [list(i) for i in initial_rows]

    seats = find_final_seat_state(initial_seats)
    render_seats(seats)
    assert count_occupied_seats(seats) == 26
