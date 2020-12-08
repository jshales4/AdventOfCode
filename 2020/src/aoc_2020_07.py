from typing import Dict, Any, List, Optional

YEAR = 2020
DAY = 7


class Bag:
    num: int
    type: str

    def __init__(self, num, type):
        self.num = num
        self.type = type

    def __repr__(self):
        return f"{self.num} {self.type}"


def create_bag(bag_str: str) -> Optional[Bag]:
    bag_parts = bag_str.split(" ")
    if bag_parts[0] == "no":
        return
    else:
        number = int(bag_parts[0])
    bag_type = " ".join(bag_parts[1:3])
    bag = Bag(number, bag_type)
    return bag


def parse_contained_bags(contained_bags: str) -> List[Bag]:
    contained_bag_split = contained_bags.split(", ")
    bag_list = []
    for bag in contained_bag_split:
        bag = create_bag(bag)
        if bag:
            bag_list.append(bag)
    return bag_list


def build_bag_dict(rules: List[str]) -> Dict[str, List[Bag]]:
    bag_dict = {}
    for rule in rules:
        outer_bag_split = rule.split(" contain ")
        outer_bag = outer_bag_split[0].replace(" bags", "")
        interior_bags = parse_contained_bags(outer_bag_split[1])
        bag_dict[outer_bag] = interior_bags
    return bag_dict


def is_inside_bag(searched_type, current_type, bag_dict) -> bool:
    if len(bag_dict[current_type]) > 0 and searched_type in [
        bag.type for bag in bag_dict[current_type]
    ]:
        return True
    else:
        for bag in bag_dict[current_type]:
            if is_inside_bag(searched_type, bag.type, bag_dict):
                return True
        return False


def count_contained_bags(current_type, bag_dict) -> int:
    count = 0
    for bag in bag_dict[current_type]:
        count += bag.num + bag.num * count_contained_bags(bag.type, bag_dict)
    return count


def count_can_contain_by_type(type: str, bag_dict) -> int:
    count = 0
    for key in bag_dict.keys():
        if is_inside_bag(type, key, bag_dict):
            count += 1
    return count


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()

    bag_dict = build_bag_dict(data)
    count = count_can_contain_by_type("shiny gold", bag_dict)
    print(count, "is the total for part 1.")

    count_contained = count_contained_bags("shiny gold", bag_dict)
    print(count_contained, "is the total for part 2.")


if __name__ == "__main__":
    main()
