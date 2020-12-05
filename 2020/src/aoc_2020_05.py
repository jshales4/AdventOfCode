from typing import Optional, List

YEAR = 2020
DAY = 5
MAX_ROW_POSSIBLE = 127
MAX_COLUMN_POSSIBLE = 7


class SeatRange:
    min_val: int
    max_val: int

    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val

    def get_current_size(self):
        return self.max_val - self.min_val + 1  # because it is based at 0

    def get_final_value(self):
        assert self.min_val == self.max_val
        return self.min_val


def break_boarding_pass_row_column(boarding_pass: str) -> [str, str]:
    boarding_pass = boarding_pass.rstrip()
    assert len(boarding_pass) == 10, len(boarding_pass)
    return boarding_pass[:7], boarding_pass[7:]


def find_missing_seat(occupied_seats: List[int]) -> Optional[int]:
    prior_seat_if_empty: Optional[int] = None
    prior_prior_seat_if_empty: Optional[int] = None
    for i in range(MAX_ROW_POSSIBLE + 1):
        for j in range(MAX_COLUMN_POSSIBLE + 1):
            possible_seat = get_seat_id(i, j)
            if possible_seat in occupied_seats:
                if prior_seat_if_empty and not prior_prior_seat_if_empty:
                    return prior_seat_if_empty
                prior_prior_seat_if_empty = prior_seat_if_empty
                prior_seat_if_empty = None
            else:
                prior_prior_seat_if_empty = prior_seat_if_empty
                prior_seat_if_empty = possible_seat


def get_seat_id(row_number: int, column_number: int) -> int:
    return row_number * 8 + column_number


def parse_row_character(half: str, sr: SeatRange) -> SeatRange:
    assert half in ("F", "B", "L", "R")
    if half in ["F", "L"]:
        sr.max_val -= sr.get_current_size() // 2
    else:
        sr.min_val += sr.get_current_size() // 2

    return sr


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()

    highest_seat_id: Optional[int] = None
    found_seat_ids: List[int] = []

    for boarding_pass in data:
        row_str, column_str = break_boarding_pass_row_column(boarding_pass)
        max_row = MAX_ROW_POSSIBLE
        max_column = MAX_COLUMN_POSSIBLE

        sr_row: SeatRange = SeatRange(0, max_row)
        sr_column: SeatRange = SeatRange(0, max_column)
        for char in row_str:
            sr_row = parse_row_character(char, sr_row)

        for char in column_str:
            sr_column = parse_row_character(char, sr_column)

        seat_id = get_seat_id(sr_row.get_final_value(), sr_column.get_final_value())

        found_seat_ids.append(seat_id)

        if not highest_seat_id or highest_seat_id < seat_id:
            highest_seat_id = seat_id

    print(highest_seat_id, "is the answer to part 1.")
    print(find_missing_seat(found_seat_ids), "is the answer to part 2.")


if __name__ == "__main__":
    main()
