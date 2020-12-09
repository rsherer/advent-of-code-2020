# Advent of Code 2020

# day 9, find the first number which isn't the sum of 2 of the 25
# previous in the list

from typing import List, Union


def has_sum_to_target(sequence: List[int], target: int) -> bool:
    ordered = sorted(sequence)
    front, back = 0, len(ordered) - 1

    while front < back:
        if (ordered[front] + ordered[back] == target) and (
            ordered[front] != ordered[back]
        ):
            return True
        elif ordered[front] + ordered[back] < target:
            front += 1
        else:
            back -= 1
    return False


assert has_sum_to_target([35, 20, 15, 25, 47], 40) == True
assert has_sum_to_target([95, 102, 117, 150, 182], 127) == False


def is_invalid_preamble(sequence: List[int], preamble_length: int) -> int:
    for i, seq in enumerate(sequence):
        if not has_sum_to_target(
            sequence[i : preamble_length + i], sequence[preamble_length + i]
        ):
            return sequence[preamble_length + i], preamble_length + i


assert is_invalid_preamble(
        [
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576,
        ],
        5,
    ) == (127, 14)


with open('../inputs/day09.txt') as f:
    XMAS = [int(line.strip()) for line in f.readlines()]

print(is_invalid_preamble(XMAS, 25)) # 14144619

# part 2, find two numbers in contiguous set which equal the invalid preamble
# return the sum of the min and max

def sum_max_min(sequence: List[int], target: int) -> int:
    for i in range(len(sequence)):
        for j in range(2, len(sequence) + 1):
            if sum(sequence[i:j]) == target:
                return sum([min(sequence[i:j]), max(sequence[i:j])])

assert sum_max_min([
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576,
        ], 127) == 62

print(sum_max_min(XMAS, 14144619))