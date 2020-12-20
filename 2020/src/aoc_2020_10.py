from typing import Optional, List, Tuple, Dict, Any

YEAR = 2020
DAY = 10


def count_adapter_options(adapters: List[int]) -> int:
    adapters.sort()
    for adapter in range(len(adapters)):
        # foo
        return 0


def main():
    data = [
        int(i) for i in open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    ]
    data.sort()
    print(data)
    delta_1 = delta_3 = 0
    for adapter in range(len(data)):
        if adapter == 0:
            diff = data[adapter] - 0
        else:
            diff = data[adapter] - data[adapter - 1]
        if diff == 1:
            delta_1 += 1
        else:
            assert diff == 3
            delta_3 += 1

    delta_3 += 1  # to go to the wall
    print(delta_1 * (delta_3), "is the answer to part 1.")


if __name__ == "__main__":
    main()
