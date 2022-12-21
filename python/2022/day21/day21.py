from copy import deepcopy

from python.download_input import get_input_content


def parse_monkeys(data):
    monkeys = {}
    for line in data:
        name, value = line.split(': ')
        try:
            value = int(value)
        except ValueError:
            pass
        monkeys[name] = value
    return monkeys


def get_result_for_monkey(name, monkeys):
    if type(monkeys[name]) is int:
        return monkeys[name]

    one, op, two = monkeys[name].split()

    one = get_result_for_monkey(one, monkeys)
    two = get_result_for_monkey(two, monkeys)

    match op:
        case '+': value = one + two
        case '-': value = one - two
        case '*': value = one * two
        case '/': value = one / two
        case _: raise ValueError(f'{op} not recognized')

    monkeys[name] = int(value)
    return monkeys[name]


def first(data):
    monkeys = parse_monkeys(data)

    return get_result_for_monkey('root', monkeys)


def solve(name, monkeys):
    if type(monkeys[name]) is int or type(monkeys[name]) is complex:
        return monkeys[name]

    print(name)
    print(monkeys[name])
    one, op, two = monkeys[name].split()

    return f'({solve(one, monkeys)} {op} {solve(two, monkeys)})'


def second(data):
    """ Inspired by https://www.reddit.com/r/adventofcode/comments/zrav4h/comment/j14w20m/ """
    monkeys = parse_monkeys(data)
    monkeys['humn'] = -1j
    monkeys['root'] = f'{monkeys["root"].split()[0]} - {monkeys["root"].split()[-1]}'
    equation = solve('root', monkeys)
    result = eval(equation)
    return int(result.real / result.imag)


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
