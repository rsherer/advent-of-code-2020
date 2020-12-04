# advent of code, day 4

# part, determine the number of valid passports.

from typing import Dict, List, NamedTuple, Set
import string

''' Expected fields:
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''

with open('../inputs/day04.txt') as f:
    readout = f.read()

FIELDS = {'byr', 'iyr','eyr', 'hgt', 'hcl', 'ecl', 'pid','cid'}

def make_passports(readout: str) -> List[Dict[str, str]]:
    elf_ids = readout.split('\n\n')

    passports = []

    for line in elf_ids:
        passport = {}
        for ids in line.split():
            k, v = ids.split(':')
            passport[k] = v
        passports.append(passport)

    return passports

def is_valid(fields: Set[str], passport: Dict[str, str], unnecessary_field: str) -> bool:
    valid = fields
    if unnecessary_field:
        valid -= {unnecessary_field}
    return valid == {key for key in passport.keys() if key != unnecessary_field}


example = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

assert sum(is_valid(FIELDS, passport, 'cid') for passport in make_passports(example)) == 2

print(sum(is_valid(FIELDS, passport, 'cid') for passport in make_passports(readout)))

# part 2

def is_valid2(passport: Dict[str, str]) -> bool:
    rules =[
        1920 <= int(passport.get('byr', 0)) <= 2002,
        2010 <= int(passport.get('iyr', 0)) <= 2020,
        2020 <= int(passport.get('eyr', 0)) <= 2030,
        is_valid_height(passport.get('hgt', '')),
        len(passport.get('hcl', '')) == 7 and passport.get('hcl', '')[0] == '#',
        passport.get('ecl', '') in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        len(passport.get('pid', '')) == 9 and all([True for char in passport.get('pid', '') if char in string.digits]),
        passport.get('cid', '1')
    ]

    return all(rules)
    

def is_valid_height(height: str) -> bool:
    if height[-2:] not in ['cm', 'in']:
        return False
    elif height[-2:] == 'cm':
        return 150 <= int(height[:-2]) <= 193
    else:
        return 59 <= int(height[:-2]) <= 76

assert is_valid_height('60in') == True
assert is_valid_height('190cm') == True
assert is_valid_height('190in') == False
assert is_valid_height('190') == False


INVALID = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

VALID = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''

assert sum(is_valid2(passport) for passport in make_passports(VALID)) == 4
assert sum(is_valid2(passport) for passport in make_passports(INVALID)) == 0

print(sum(is_valid2(passport) for passport in make_passports(readout)))
