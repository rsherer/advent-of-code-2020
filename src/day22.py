# advent of code 2020, day 22
# part 1

from typing import List, Tuple

input = '''Player 1:
27
29
30
44
50
5
33
47
34
38
36
4
2
18
24
16
32
21
17
9
3
22
41
31
23

Player 2:
25
1
15
46
6
13
20
12
10
14
19
37
40
26
43
11
48
45
49
28
35
7
42
39
8'''

def parse(input: str) -> Tuple[List[int], List[int]]:
    p1, p2 = input.split('\n\n')
    p1 = [int(num) for num in p1.split('\n')[1:]]
    p2 = [int(num) for num in p2.split('\n')[1:]]
    return p1, p2

p1, p2 = parse(input)

def play_hand(p1: List[int], p2: List[int]) -> Tuple[List[int], List[int]]:
    c1, c2 = p1.pop(0), p2.pop(0)
    if c1 > c2:
        p1.extend(sorted([c1, c2], reverse=True))
    else:
        p2.extend(sorted([c1, c2], reverse=True))
    return p1, p2

player1 = [9, 2, 6, 3, 1]
player2 = [5, 8, 4, 7, 10]

#print(play_hand(player1, player2))
assert play_hand(player1, player2) == ([2, 6, 3, 1, 9, 5], [8, 4, 7, 10])

def play_game(p1: List[int], p2: List[int]) -> Tuple[List[int], List[int]]:
    hands = 1
    while min(len(p1), len(p2)) > 0:
        p1, p2 = play_hand(p1, p2)
        hands += 1
    return p1, p2

print(play_game(player1, player2))

def game_score(final_hand: List[int]) -> int:
    total = 0
    hand_scores = [score for score in range(1, len(final_hand) + 1)]
    for score, card in zip(hand_scores, reversed(final_hand)):
        total += score * card
    return total

print(game_score([3, 2, 10, 6, 8, 5, 9, 4, 7, 1]))
#print(play_game(p1, p2))
h1, h2 = play_game(p1, p2)

if h1:
    print(f"player 1 won with a score of {game_score(h1)}")
else:
    print(f"player 2 won with a score of {game_score(h2)}")


#part 2, Recursive Combat

