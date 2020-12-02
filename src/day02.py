# advent of code 2020 day 2
# part 1
from typing import List

with open("day02.txt") as f:
    passwords = [line.strip().split() for line in f]

example = [
    ["1-3", "a:", "abcde"],
    ["1-3", "b:", "cdefg"],
    ["2-9", "c:", "ccccccccc"],
]


def in_range(lo: str, hi: str, letter: str, pwd: str) -> bool:
    counts = pwd.count(letter)
    return int(lo) <= counts <= int(hi)


assert in_range("1", "3", "a", "abcde") == True
assert in_range("1", "3", "b", "cdefg") == False


def count_valid_passwords(pwds: List[List[str]]) -> int:
    total = 0
    for line in pwds:
        lo, hi = line[0].split("-")
        letter = line[1][0]
        password = line[2]
        if in_range(lo, hi, letter, password):
            total += 1
    return total


assert count_valid_passwords(example) == 2, count_valid_passwords(example)

print(count_valid_passwords(passwords))

# part 2


def count_valid_passwords2(pwds: List[List["str"]]) -> int:
    total = 0
    for line in pwds:
        lo, hi = line[0].split("-")
        letter = line[1][0]
        password = line[2]
        if sum([password[int(lo) - 1] == letter, password[int(hi) - 1] == letter]) == 1:
            total += 1
    return total


assert count_valid_passwords2(example) == 1

print(count_valid_passwords2(passwords))
