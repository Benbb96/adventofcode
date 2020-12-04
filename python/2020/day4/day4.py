import re


def first(input):
    valid = 0
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    fields = set()
    for line in input:
        if line == '':
            print(fields)
            if fields == required_fields:
                valid += 1
            fields = set()

        data = line.split()
        for d in data:
            if d[:3] in required_fields:
                fields.add(d[:3])

    return valid


def second(input):
    valid = 0
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    fields = set()
    for line in input:
        if line == '':
            print(fields)
            if fields == required_fields:
                valid += 1
            fields = set()

        data = line.split()
        for d in data:
            field, value = d.split(':')
            if field in required_fields:
                if field == 'byr' and (1920 <= int(value) <= 2002):
                    fields.add(field)
                if field == 'iyr' and (2010 <= int(value) <= 2020):
                    fields.add(field)
                if field == 'eyr' and (2020 <= int(value) <= 2030):
                    fields.add(field)
                if field == 'hgt':
                    if value[-2:] == 'cm' and (150 <= int(value[:-2]) <= 193):
                        fields.add(field)
                    elif value[-2:] == 'in' and (59 <= int(value[:-2]) <= 76):
                        fields.add(field)
                if field == 'hcl' and re.match('^#[0-9a-f]{6}$', value):
                    fields.add(field)
                if field == 'ecl' and value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    fields.add(field)
                if field == 'pid' and re.match('^[0-9]{9}$', value):
                    fields.add(field)

    return valid


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
