YEAR = 2019
DAY = 1


# Part 1
def calculate_fuel_for_mass(mass: int) -> int:
    return mass // 3 - 2


# Part 2
def calculate_fuel_for_mass_recursive(mass: int) -> int:
    if mass // 3 - 2 <= 0:
        return 0
    else:
        cost = mass // 3 - 2
        return cost + calculate_fuel_for_mass_recursive(cost)


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    total_mass_part_one = 0
    total_mass_part_two = 0
    for entry in data:
        total_mass_part_one += calculate_fuel_for_mass(int(entry))
        total_mass_part_two += calculate_fuel_for_mass_recursive(int(entry))
    print(total_mass_part_one, "answer for Part 1")
    print(total_mass_part_two, "answer for Part 2")


if __name__ == "__main__":
    main()
