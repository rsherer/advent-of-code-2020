# advent of code, day 15
# part 1

import numpy as np
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Number:
    previous: int
    latest: int

class ElfGame:
    def __init__(self):
        self.seen: Dict[int, Number] = {}
        self.last = 0
        self.turns = 0

    def process_number(self, num: int) -> int:
        self.last = num
        self.turns += 1
        if self.last not in self.seen:
            self.seen[self.last] = Number(None, self.turns)
        else:
            self.seen[self.last].previous = self.seen[self.last].latest
            self.seen[self.last].latest = self.turns
        return num

    def get_next_number(self) -> None:
        if not self.seen[self.last].previous:
            self.process_number(0)
        else:
            age = self.seen[self.last].latest - self.seen[self.last].previous
            self.process_number(age)

    def process_starters(self, starters: List[int]) -> None:
        for num in starters:
            self.process_number(num)

    def play_game(self, rounds: int) -> None:
        while self.turns < rounds:
            if self.turns % 10_000 == 0:
                print(self.turns / rounds)
            self.get_next_number()

game1 = ([0, 3, 6], 436)
game2 = ([1, 3, 2], 1)
game3 = ([2, 1, 3], 10)

for game, final in [game1, game2, game3]:
    eg = ElfGame()
    eg.process_starters(game)
    eg.play_game(2020)
    assert eg.last == final

inputs = [0,13,1,8,6,15]


# part 1
# rounds1 = 2020
# eg = ElfGame()
# eg.process_starters(inputs)
# eg.play_game(rounds1)
# print(eg.last) #1618

# part 2
rounds2 = 30000000

eg = ElfGame()
eg.process_starters(inputs)
eg.play_game(rounds2)
print(eg.last)
