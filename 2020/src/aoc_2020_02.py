YEAR = 2020
DAY = 2


def is_valid_password_part1(rule: str, password: str):
    count_rule, character = rule.split(" ")
    count_min, count_max = [int(i) for i in count_rule.split("-")]
    if count_min <= password.count(character) <= count_max:
        return True
    else:
        return False


def is_valid_password_part2(rule: str, password: str):
    count_rule, character = rule.split(" ")
    position1, position2 = [int(i) for i in count_rule.split("-")]
    return (password[position1 - 1] == character) != (
        password[position2 - 1] == character
    )


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    valid_counter_part1 = 0
    valid_counter_part2 = 0
    for row in data:
        rule, password = row.split(": ")
        if is_valid_password_part1(rule, password):
            valid_counter_part1 += 1
        if is_valid_password_part2(rule, password):
            valid_counter_part2 += 1
    print(valid_counter_part1, "is the answer to part 1.")
    print(valid_counter_part2, "is the answer to part 2.")


if __name__ == "__main__":
    main()
