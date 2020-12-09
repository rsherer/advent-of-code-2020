# advent of code, day 7

# part 1
from typing import Dict, List

with open('../inputs/day07.txt') as f:
    bags = [line.strip('.\n') for line in f.readlines()]

def parse_rules(rule: str) -> Dict[str, Dict[str, int]]:
    outer, inner = rule.replace(' bags', '').replace(' bag', '').split(' contain ')

    if inner in 'no other.':
        parsed_rules = {outer: {'no bag': 0}}
    else:
        parsed_rules = {outer:
        {bags[2:]: int(bags[:2]) for bags in inner.split(', ')}
        }

    return parsed_rules

def is_bag_inside(rule: str, bag: str) -> int:
    return bag in [list(bags.keys()) for bags in parse_rules(rule).values() if not 0][0]

def get_outer_bag(rule: str, inner_bag: str) -> str:
    if is_bag_inside(rule, inner_bag):
        return list(parse_rules(rule).keys())[0]

def get_bag_colors(rules: List[str], origin_bag: str) -> int:
    outer_bags = [get_outer_bag(rule, origin_bag) for rule in rules if get_outer_bag(rule, origin_bag)]
    final = []
    while outer_bags:
        final += outer_bags
        next_outer = [get_outer_bag(rule, bag) for bag in outer_bags for rule in rules if get_outer_bag(rule, bag)]
        outer_bags = next_outer
    return len(set(final))

example = ['light red bags contain 1 bright white bag, 2 muted yellow bags',
'dark orange bags contain 3 bright white bags, 4 muted yellow bags',
'bright white bags contain 1 shiny gold bag',
'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags',
'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags',
'dark olive bags contain 3 faded blue bags, 4 dotted black bags',
'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags',
'faded blue bags contain no other bags',
'dotted black bags contain no other bags']

assert get_bag_colors(example, 'shiny gold') == 4

#print(get_bag_colors(bags, 'shiny gold'))

# part 2

def count_number_bags(rules: List[str], outside: str) -> int:
    bags = [parse_rules(rule) for rule in rules]
    root = [bag for bag in bags if bag.get(outside)][0]

    # total = 0
    # for bag, total in root[outside].items():
    #     inner_bag = count_number_bags(rules, bag)
    #     total += total * sum(total for bag, total in root[outside].items())
    return [bag for bag, total in root[outside].items()]
 #   return root[outside]


#print(count_number_bags(bags, 'shiny gold'))
print(count_number_bags(bags, 'striped gold'))