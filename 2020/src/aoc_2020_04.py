from typing import Dict
import re

YEAR = 2020
DAY = 4


def parse_line(line: str, current_details: Dict[str, str]) -> Dict[str, str]:
    new_details = line.split(" ")
    for detail in new_details:
        detail_split = detail.split(":")
        assert len(detail_split) == 2, detail_split
        current_details[detail_split[0]] = detail_split[1]
    return current_details


def is_valid_op(f):
    """a simple decorator to stop having to check for ValueErrors everywhere"""

    def wrapper(*args, **kwargs):
        try:
            args = [arg.rstrip() if isinstance(arg, str) else arg for arg in args]
            result = f(*args, **kwargs)
            return result
        except ValueError or AssertionError:
            return False

    return wrapper


def is_end_of_record(line: str) -> bool:
    return line == "\n"


@is_valid_op
def is_valid_number(number: str, length: int, min: int, max: int) -> bool:
    return len(str(number)) == length and (min <= int(number) <= max)


@is_valid_op
def is_valid_height(height: str) -> bool:
    dimension = height[-2:]
    if dimension == "cm":
        return 150 <= int(height[:3]) <= 193
    elif dimension == "in":
        return 59 <= int(height[:2]) <= 76
    else:
        return False


@is_valid_op
def is_valid_haircolor(haircolor: str) -> bool:
    return bool(
        re.search(
            "^#[a-f0-9]{6}$",
            haircolor,
        )
    )


@is_valid_op
def is_valid_eyecolor(eyecolor: str) -> bool:
    return eyecolor in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid_passport(details: Dict[str, str]) -> bool:
    needed_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return set(needed_fields).issubset(details.keys())


def check_field_validity(details: Dict[str, str]) -> bool:
    result = (
        is_valid_number(details["byr"], 4, 1920, 2002)
        and is_valid_number(details["iyr"], 4, 2010, 2020)
        and is_valid_number(details["eyr"], 4, 2020, 2030)
        and is_valid_height(details["hgt"])
        and is_valid_haircolor(details["hcl"])
        and is_valid_eyecolor(details["ecl"])
        and is_valid_number(details["pid"], 9, 0, 999999999)
    )
    return result


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    current_details = {}
    valid_passport_counter = 0
    valid_fields_passport = 0
    total_passport_counter = 0
    for row in data:
        if is_end_of_record(row):
            total_passport_counter += 1
            if is_valid_passport(current_details):
                valid_passport_counter += 1
                if check_field_validity(current_details):
                    valid_fields_passport += 1
            current_details = {}
        else:
            current_details = parse_line(row, current_details)
    # No newline at end of file, so check the last one
    total_passport_counter += 1
    if is_valid_passport(current_details):
        valid_passport_counter += 1
        if check_field_validity(current_details):
            valid_fields_passport += 1
    print(valid_passport_counter, "is the answer to part 1.")
    print(valid_fields_passport, "is the answer to part 2.")


if __name__ == "__main__":
    main()
