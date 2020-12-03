# Advent of Code 2020
# day 3, part 1

# travel through a forest with a toboggan and count the trees encountered
import numpy as np
from typing import NamedTuple, List, Tuple
from dataclasses import dataclass

with open('../inputs/day03.txt') as f:
    forest = [line.strip() for line in f]

@dataclass
class Location:
    x: int
    y: int

class Forest(NamedTuple):
    run: int
    rise: int
    trees: List[str]

    def parse_forest(self) -> np.array:
        grove = [
            [1 if char != '.' else 0
            for char in line]
            for line in self.trees 
            ]
        width = len(self.trees[0])
        length = len(self.trees)
        grove_length = length / self.rise
        grove_width = grove_length * self.run // width + 1

        forest = np.concatenate([grove for _ in range(int(grove_width))], axis = 1)

        return forest

    def count_tree_encounters(self) -> int:
        start = Location(0, 0)
        encounters = 0
        forest = self.parse_forest()
        length, width = self.parse_forest().shape
        while start.y < length - 1:
            start.y += self.rise
            start.x += self.run
            if forest[start.y][start.x] == 1:
                encounters += 1
        return encounters

example = [
    '..##.......',
'#...#...#..',
'.#....#..#.',
'..#.#...#.#',
'.#...##..#.',
'..#.##.....',
'.#.#.#....#',
'.#........#',
'#.##...#...',
'#...##....#',
'.#..#...#.#',
]

test_park =  Forest(3, 1, example)
#breakpoint()
#print(test_park.parse_forest())
assert test_park.count_tree_encounters() == 7, test_park.count_tree_encounters()

park = Forest(3, 1, forest)
print(park.count_tree_encounters())

# part 2

'''Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.

'''
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

def get_trees_product(slopes: List[Tuple[int, int]], forest: List[str]) -> int:
    return np.prod([
        Forest(run, rise, forest).count_tree_encounters() 
        for run, rise in slopes])
    
assert get_trees_product(slopes, example) == 336

print(get_trees_product(slopes, forest))

