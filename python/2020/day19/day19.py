import re
import sys
from functools import lru_cache

sys.setrecursionlimit(5000)

rules = {}


@lru_cache()
def get_rule(number, second=False):
    if second:
        if number == '8':
            return get_rule('42', second) + '+'
        elif number == '11':
            a = get_rule('42', second)
            b = get_rule('31', second)
            return '(?:' + '|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 100)) + ')'

    rule = rules[number]
    letter = re.search('^"(.)"$', rule)
    if letter:
        return letter.group(1)
    else:
        parts = rule.split(' | ')
        res = []
        for part in parts:
            nums = part.split(' ')
            res.append(''.join(get_rule(num, second) for num in nums))
        return '(?:' + '|'.join(res) + ')'


def first(input):
    messages = []
    rules_done = False
    for line in input:
        if rules_done:
            messages.append(line)
        else:
            if line == '':
                rules_done = True
                continue
            number, rule = line.split(': ')
            rules[number] = rule

    valid_count = 0
    rule_0 = get_rule('0')
    for message in messages:
        valid_count += bool(re.fullmatch(rule_0, message))

    return valid_count


def second(input):
    messages = []
    rules_done = False
    for line in input:
        if rules_done:
            messages.append(line)
        else:
            if line == '':
                rules_done = True
                continue
            number, rule = line.split(': ')
            rules[number] = rule

    valid_count = 0
    rule_0 = get_rule('0', True)
    for message in messages:
        valid_count += bool(re.fullmatch(rule_0, message))

    return valid_count


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
