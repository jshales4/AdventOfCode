# AoC 2016 Day 4
import re
from typing import List, Dict

YEAR = 2016
DAY = 4


def seperate_out_code(instruction: List[str]) -> (str, int, str):
    encrypted_name = instruction[:-1]
    digit_and_hash = instruction[-1]
    name_concatenated = " ".join(encrypted_name)
    digit = int(re.findall(r"\d+", digit_and_hash)[0])
    hash_code = digit_and_hash[digit_and_hash.find("[") + 1 : digit_and_hash.find("]")]
    return name_concatenated, digit, hash_code


def build_character_counter(encrypted_name: str) -> Dict[str, int]:
    character_counter: Dict[str, int] = {}
    for char in encrypted_name:
        if char == " ":
            continue
        if character_counter.get(char):
            character_counter[char] += 1
        else:
            character_counter[char] = 1
    return character_counter


def is_true_room(encrypted_name, hash_code) -> bool:
    character_counter = build_character_counter(encrypted_name)
    sorted_dict = {
        k: v
        for k, v in sorted(
            character_counter.items(), key=lambda item: (-item[1], item[0])
        )
    }
    most_frequent = list(sorted_dict.keys())
    correct_hash = True
    for i in range(5):
        if most_frequent[i] not in hash_code:
            return False
    if correct_hash:
        return True


def cycle_room_name(room_name: str, digit: int) -> None:
    LETTER_Z = 122
    decoded_string = []
    rolled_digit = digit % 26
    for char in room_name:
        if char == " ":
            decoded_string.append(" ")
        elif ord(char) + rolled_digit > LETTER_Z:
            decoded_string.append(chr(ord(char) + rolled_digit - 26))
        else:
            decoded_string.append(chr(ord(char) + rolled_digit))
    if "northpole" in "".join(decoded_string):
        print("Room", "".join(decoded_string), ": Sector:", digit, "(answer to part 2)")


def main():
    data = open(f"../input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    counter = 0
    for line in data:
        encrypted_name, digit, hash_code = seperate_out_code(line.split("-"))
        if is_true_room(encrypted_name, hash_code):
            counter += digit
            cycle_room_name(encrypted_name, digit)
    print(counter, "is the answer to part 1")


if __name__ == "__main__":
    main()
