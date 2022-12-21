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


def second(data):
    monkeys = parse_monkeys(data)
    my_input = 3700000000000  # huh
    while True:
        monkeys_copy = deepcopy(monkeys)
        one, op, two = monkeys_copy['root'].split()
        monkeys_copy['humn'] = my_input
        # print(my_input)
        # print(get_result_for_monkey(one, monkeys_copy))
        # print(get_result_for_monkey(two, monkeys_copy))
        if get_result_for_monkey(one, monkeys_copy) == get_result_for_monkey(two, monkeys_copy):
            return my_input
        my_input += 1


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''
    # if test_input:
    #     content = test_input.split('\n')

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
