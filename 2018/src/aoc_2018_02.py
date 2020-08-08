# AoC Template

from typing import Tuple, Dict, List, Optional

YEAR = 2018
DAY = 2
SALT = "$%^&"


# Part 1
def count_letter(word: str) -> Tuple[bool, bool]:
    letters: Dict[str, int] = {}
    double: bool = False
    triple: bool = False
    for char in word:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    for key in letters:
        if letters[key] == 2:
            double = True
        elif letters[key] == 3:
            triple = True
    return double, triple


# Part 1
def calculate_doubles_and_triples(words: List[str]) -> Tuple[int, int]:
    double_counts = 0
    triple_counts = 0
    for entry in words:
        double, triple = count_letter(entry)
        double_counts += double * 1
        triple_counts += triple * 1
    return double_counts, triple_counts


# Part 2
def get_possible_box_ids(words: List[str]) -> Optional[str]:
    box_ids: List[str] = []
    for word in words:
        for i in range(len(word)):
            new_id = word[:i] + SALT + word[i + 1 :]
            if new_id not in box_ids:
                box_ids.append(new_id)
            else:
                return new_id.replace(SALT, "")
    return None


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    doubles, triples = calculate_doubles_and_triples(data)
    print(doubles * triples, "answer to part 1")
    print(get_possible_box_ids(data), "answer to part 2")


if __name__ == "__main__":
    main()
