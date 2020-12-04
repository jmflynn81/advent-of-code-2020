import json
import re

REQUIRED = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]
YEAR_MAP = {
    "byr": [1920, 2002],
    "iyr": [2010, 2020],
    "eyr": [2020, 2030]
}
HEIGHT_MAP = {
    "cm": ["c", 150, 193],
    "in": ["i", 59, 76]
}
EYE_COLORS = [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth"
]
RE_STRING_MAP = {
    "pid": r'^[0-9]{9}$',
    "hcl": r'^#[0-9a-f]{6}$'
}

def get_passports():
    with open('passports') as f:
        passports = f.read().splitlines()
    return passports


def get_formatted_passports(passports):
    formatted_passports = [{}]
    counter = 0
    for line in passports:
        if not line == "":
            cats = line.split()
            for cat in cats:
                category, value = cat.split(':')
                if category != 'cid':
                    formatted_passports[counter][category] = value
        else:
            counter += 1
            formatted_passports.append({})
    return formatted_passports


passports = get_passports()
formatted_passports = get_formatted_passports(passports)
valid_passports = 0

for check in formatted_passports:
    valid = True
    for requirement in REQUIRED:
        value = check.get(requirement)
        if value == None:
            print(f"* Requirement {requirement} not in {check}")
            valid = False
            break
        elif requirement in ['byr', 'iyr', 'eyr']:
            if not (int(value) >= YEAR_MAP[requirement][0] 
                    and int(value) <= YEAR_MAP[requirement][1]):
                print(f"  {requirement} check failed {value}")
                valid = False
                break
        elif requirement == 'hgt':
            units = value[-2:]
            if units == 'cm' or units == 'in':
                height = int(value.split(HEIGHT_MAP[units][0])[0])
                if not (height >= HEIGHT_MAP[units][1] 
                        and height <= HEIGHT_MAP[units][2]):
                    print(f"  hgt ({units}) check failed {value}")
                    valid = False
                    break
            else:
                print(f"  hgt (no units) check failed {value}")
                valid = False
                break
        elif requirement in ['hcl', 'pid']:
            if not re.match(RE_STRING_MAP[requirement], value):
                print(f"  {requirement} check failed {value}")
                valid = False
                break
        elif requirement == 'ecl':
            if value not in EYE_COLORS:
                print(f"  ecl check failed {value}")
                valid = False
                break
    if valid:
        print(f"+ VALID {check}")
        valid_passports += 1

print()
print(f"Total pasports {len(formatted_passports)}")
print(f"Valid Passports {valid_passports}")


