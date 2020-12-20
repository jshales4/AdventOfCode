from typing import Optional, List, Tuple, Dict, Any
import copy

YEAR = 2020
DAY = 11
part_2 = False


def is_seat_available(x: int, y: int, seats: List[List[str]]) -> bool:
    try:
        if x < 0 or y < 0:
            return True
        seat = seats[x][y]
        return seat in ["L", "."]
    except IndexError:
        return True


def count_free_adjacent_seats_to_square(x: int, y: int, seats: List[List[str]]) -> int:
    counter = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                # while seats[x + i][y + j] == ".":
                #     if (
                #         i != 0 and 0 <= x + i + int((i ** 0) * abs(i) / i) < len(seats)
                #     ) or (
                #         j != 0
                #         and 0 <= y + j + int(j ** 0 * abs(j) / j) < len(seats[x])
                #     ):
                #         break
                #     if i != 0:
                #         i += int((i ** 0) * abs(i) / i)
                #     if j != 0:
                #         j += int(j ** 0 * abs(j) / j)
                counter += is_seat_available(x + i, y + j, seats)
    return counter


def propose_new_assignment_for_seat(
    x: int, y: int, seats: List[List[str]]
) -> Optional[str]:

    free_adjacent_seats: int = count_free_adjacent_seats_to_square(x, y, seats)

    if free_adjacent_seats == 8 and seats[x][y] not in [
        ".",
        "#",
    ]:
        return "#"
    elif free_adjacent_seats <= 4 and seats[x][y] not in [
        ".",
        "L",
    ]:
        return "L"
    else:
        return


def create_new_seat_assignment(old_seats: List[List[str]]) -> Optional[List[List[str]]]:
    new_seats = copy.deepcopy(old_seats)
    seat_has_changed = False
    new_seat_count = 0
    for row in range(len(old_seats)):
        for column in range(len(old_seats[row])):
            new_seat = propose_new_assignment_for_seat(row, column, old_seats)
            if new_seat:
                seat_has_changed = True
                new_seat_count += 1
                new_seats[row][column] = new_seat
    if seat_has_changed:
        print(render_seats(new_seats))
        return new_seats
    else:
        return


def count_occupied_seats(seats: List[List[str]]) -> int:
    counter = 0
    for row in range(len(seats)):
        for seat in range(len(seats[row])):
            if not is_seat_available(row, seat, seats):
                counter += 1
    return counter


def main():
    seats = [
        list(i.rstrip())
        for i in open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    ]
    seats_part1 = find_final_seat_state(seats)

    print(count_occupied_seats(seats_part1), "is the answer to part 1.")

    seats_part2 = find_final_seat_state(seats)

    print(count_occupied_seats(seats_part2), "is the answer to part 2.")


def render_seats(seats) -> None:
    for seat in seats:
        print(seat)


def find_final_seat_state(seats):
    seat_has_changed = True
    while seat_has_changed:
        new_seats = create_new_seat_assignment(seats)
        if not new_seats:
            seat_has_changed = False
        else:
            seats = new_seats
    return seats


if __name__ == "__main__":
    main()
