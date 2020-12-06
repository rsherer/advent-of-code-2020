# advent of code 2020, day 6
# part 1

from typing import List

with open('../inputs/day06.txt') as f:
    qs = f.read()

#print(qs.split('\n\n'))

def parse_questionnaires(qs: str) -> List[str]:
    qs = qs.split('\n\n')
    return [questions.split() for questions in qs]

def count_answered(answers: List[str]) -> int:
    return len(set(''.join(answers)))

print(sum([count_answered(answers) for answers in parse_questionnaires(qs)]))

# part 2
# find the number of questions everyone answers the same

def count_all_answered(answers: List[str]) -> int:
    same = set(answers[0])

    for a in answers[1:]:
        try:
            same = same.intersection(a)
        except IndexError:
            return len(same)
    return len(same)

assert count_all_answered(['abc']) == 3
assert count_all_answered(['a', 'b', 'c']) == 0
assert count_all_answered(['ab', 'ac']) == 1

print(sum([count_all_answered(answers) for answers in parse_questionnaires(qs)]))


