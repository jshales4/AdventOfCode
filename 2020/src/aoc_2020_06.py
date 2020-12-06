import typing

YEAR = 2020
DAY = 6


def is_start_of_new_group(row: str) -> bool:
    return row == "\n"


def add_passenger_to_group_set_any(passenger: str, group_set: typing.Set) -> typing.Set:
    return group_set | set(passenger.rstrip())


def add_passenger_to_group_set_all(passenger: str, is_new_group: bool, group_set: typing.Set) -> typing.Set:
    passenger_set: typing.Set[str] = set(passenger.rstrip())

    if is_new_group:
        group_set = passenger_set
    else:
        group_set = group_set.intersection(passenger_set)
    return group_set


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    any_answer_set: typing.Set[str] = set()
    all_answer_set: typing.Set[str] = set()
    total_yes_answers_any = total_yes_answers_all = 0
    is_new_group = True

    for row in data:
        if is_start_of_new_group(row):
            total_yes_answers_any += len(any_answer_set)
            total_yes_answers_all += len(all_answer_set)
            any_answer_set = set()
            all_answer_set = set()
            is_new_group = True
        else:
            any_answer_set = add_passenger_to_group_set_any(row, any_answer_set)
            all_answer_set = add_passenger_to_group_set_all(row, is_new_group, all_answer_set)
            is_new_group = False
    if len(any_answer_set) != 0:
        total_yes_answers_any += len(any_answer_set)
    if len(all_answer_set) != 0:
        total_yes_answers_all += len(all_answer_set)

    print(total_yes_answers_any, "is the answer to part 1.")
    print(total_yes_answers_all, "is the answer to part 2.")



if __name__ == "__main__":
    main()
