# advent of code 2020 day 2
# part 1
from collections import Counter
from typing import List

with open('day02.txt') as f:
    inputs = [line.strip().split() for line in f]

example = [
    ['1-3', 'a:', 'abcde'],
    ['1-3', 'b:', 'cdefg'],
    ['2-9', 'c:', 'ccccccccc'],
]

def has_letter(letter: str, pwd: str) -> bool:
    return letter in pwd

assert has_letter('a', 'abcde') == True
assert has_letter('b', 'cdefg') == False

def in_range(lo: str, hi: str, letter: str, pwd: str) -> bool:
    counts = Counter(pwd)
    return int(lo) <= counts[letter] <= int(hi)

assert in_range('1', '3', 'a', 'abcde') == True
assert in_range('1', '3', 'b', 'cdefg') == False

def count_valid_passwords(pwds: List[str]) -> int:
    total = 0
    for line in pwds:
            lo, hi = line[0].split('-')
            letter = line[1][0]
            password = line[2]
            if sum([has_letter(letter, password), in_range(lo, hi, letter, password)]) == 2:
                total += 1
    return total

assert count_valid_passwords(example) == 2, count_valid_passwords(example)

print(count_valid_passwords(inputs))

# part 2

def count_valid_passwords2(pwds: List['str']) -> int:
    total = 0
    for line in pwds:
        lo, hi = line[0].split('-')
        letter = line[1][0]
        password = line[2]
        if sum([password[int(lo) - 1] == letter, password[int(hi) - 1] == letter]) == 1:
            total += 1
    return total

assert count_valid_passwords2(example) == 1

print(count_valid_passwords2(inputs))