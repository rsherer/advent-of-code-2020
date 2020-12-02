from typing import List

with open("inputs/day01.txt") as f:
    inputs = [int(num) for num in f.readlines()]

example = [1721, 979, 366, 299, 675, 1456]

# part 1
def find_2020_product(receipts: List[int], year: int) -> int:
    for exp1 in receipts:
        for exp2 in receipts[1:]:
            if exp1 + exp2 == year:
                return exp1 * exp2


assert find_2020_product(example, 2020) == 514579

print(find_2020_product(inputs, 2020))

# part 2
def find_2020_product3(receipts: List[int], year: int) -> int:
    for exp1 in receipts:
        for exp2 in receipts[1:]:
            for exp3 in receipts[2:]:
                if exp1 + exp2 + exp3 == year:
                    return exp1 * exp2 * exp3


assert find_2020_product3(example, 2020) == 241861950

print(find_2020_product3(inputs, 2020))
