# advent of code 2020, day 13
# part 1

import numpy as np
from typing import List, Tuple

input = """1014511
17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,643,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,433,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19"""

earliest_timestamp = 1014511

buses = '17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,643,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,433,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'.split(',')
buses_arr = np.array([int(elem) for elem in buses if elem.isdigit()])

waits = {}
for bus in buses_arr:
    trips = earliest_timestamp // bus + 1
    wait = trips * bus % earliest_timestamp
    waits[wait] = bus

print(min(waits) * waits[min(waits)]) # answer part 1

# part 2
# find mods for buses as they are delayed by a minute for where they are
# in the raw sequence input

# thanks to Joel Grus and Paul Fornia for this approach

def make_factors(raw_buses: List[str]):
    indexed = [(i, int(bus)) for i, bus in enumerate(raw_buses) if bus != 'x']
    factors = [(bus, (bus - i) % bus) for i, bus in indexed]
    return factors

def chinese_remainder(factors: List[Tuple[int, int]]) -> int:
    solution = factors[0][1]
    increment = factors[0][0]

    for d, r in factors[1:]:
        while solution % d != r:
            solution += increment
        print(solution, increment)
        increment *= d

    return solution % increment


bus_factors = make_factors(buses)
print(bus_factors)
print(chinese_remainder(bus_factors))

