from typing import List, Optional

YEAR = 2020
DAY = 1


def _find_sum_to_value(
    value: int, numbers: List[int], num_addends: int, current_sum=0
) -> Optional[List[int]]:
    if num_addends == 1:
        for number in numbers:
            if current_sum + number == value:
                return [number]
        return None
    else:
        for number in range(len(numbers)):
            sums = _find_sum_to_value(
                value,
                numbers[number + 1 :],
                num_addends - 1,
                current_sum + numbers[number],
            )
            if sums:
                sums.append(numbers[number])
                sums.sort()
                return sums


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    expenses = [int(x) for x in data]
    num1, num2 = _find_sum_to_value(2020, expenses, 2)
    print(num1 * num2, "is the answer to part 1.")
    num1, num2, num3 = _find_sum_to_value(2020, expenses, 3)
    print(num1 * num2 * num3, "is the answer to part 2.")


if __name__ == "__main__":
    main()
