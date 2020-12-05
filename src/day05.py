# Advent of Code day 5

# part 1, find the seat id
# rows are 0 to 127
# for rows: F means lower half, B means upper half
# seats are rows 0 to 7
# for seats: L means the lower half, R means the upper half

# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
# Every seat also has a unique seat ID: multiply the row by 8, then add the column. 
# In this example, the seat has ID 44 * 8 + 5 = 357.

def find_row(boarding_pass: str):
    seat = 0
    for i, char in enumerate(reversed(boarding_pass)):
        if char == 'B':
            seat += 2**i
    return seat

def find_column(boarding_pass: str):
    seat = 0
    for i, char in enumerate(reversed(boarding_pass)):
        if char == 'R':
            seat += 2**i
    return seat

# Here are some other boarding passes:
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.

assert find_row('BFFFBBF') == 70
assert find_row('FFFBBBF') == 14
assert find_row('BBFFBBF') == 102

assert find_column('RRR') == 7
assert find_column('RRR') == 7
assert find_column('RLL') == 4


with open('../inputs/day05.txt') as f:
    passes = [line.strip() for line in f.readlines()]

print(max([find_row(bp[:7]) * 8 + find_column(bp[7:]) for bp in passes]))

# part 2
# my boarding pass is missing, but the seat IDs +1 and -1 are in the list
# need to find the id that is missing.

seat_ids = sorted([find_row(bp[:7]) * 8 + find_column(bp[7:]) for bp in passes])

for s1, s2 in zip(seat_ids, seat_ids[1:]):
    if s2 - s1 == 2:
        print(s2 - 1)