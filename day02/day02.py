# advent of code 2020 day 2
# part 1
from collections import Counter
from typing import List

def has_letter(policy: str, pwd: str) -> bool:
    letter = policy[-1]
    return letter in pwd

assert has_letter('1-3 a', ': abcde') == True
assert has_letter('1-3 b', ': cdefg') == False

def in_range(policy: str, pwd: str) -> bool:
    lo, hi = policy.split('-')
    lo, hi, letter = int(lo), int(hi[:-2]), hi[-1]
    counts = Counter(pwd)
    return counts[letter] in set(num for num in range(lo, hi + 1))

assert in_range('1-3 a', ': abcde') == True
assert in_range('1-3 b', ': cdefg') == False

def count_valid_passwords(pwds: List[str]) -> int:
    total = 0
    for line in pwds:
        policy, pwd = line.split(': ')
        if (has_letter(policy, pwd) and in_range(policy, pwd)):
            total += 1
    return total

example = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
]

assert count_valid_passwords(example) == 2

with open('day02.txt') as f:
    inputs = [line.strip() for line in f]

print(count_valid_passwords(inputs))

# part 2
# 
#     

def count_valid_passwords2(pwds: List['str']) -> int:
    total = 0
    for line in pwds:
        policy, pwd = line.split(': ')
        letter = policy[-1]
        idx1, idx2 = policy[:-2].split('-')
        idx1, idx2 = int(idx1), int(idx2)
        if sum([pwd[idx1 - 1] == letter, pwd[idx2 - 1] == letter]) == 1:
            total += 1
    return total

assert count_valid_passwords2(example) == 1, count_valid_passwords2(example)

print(count_valid_passwords2(inputs))