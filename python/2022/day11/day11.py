from collections import deque
from math import prod

from python.download_input import get_input_content


monkeys = []
prod_of_all_div = None


class Monkey:
    def __init__(self, raw):
        self.inspection_count = 0
        lines = raw.split('\n')
        self.id = lines[0][-2]
        self.items = deque(int(x) for x in lines[1][18:].split(', '))
        self.operation = lines[2][19:]
        self.div = int(''.join(filter(str.isdigit, lines[3])))
        self.throw_to_monkey_if_true = int(lines[4][-1])
        self.throw_to_monkey_if_false = int(lines[5][-1])

    def __str__(self):
        return self.id

    def inspect_items(self, part_1: bool = True):
        while self.items:
            self.inspection_count += 1
            old = self.items.popleft() % prod_of_all_div
            new = eval(self.operation)

            if part_1:
                item = new // 3
            else:
                item = new

            dest = self.throw_to_monkey_if_false if item % self.div else self.throw_to_monkey_if_true
            monkeys[dest].items.append(item)


def first():

    for i in range(20):
        for monkey in monkeys:
            monkey.inspect_items()

    inspection_counts = sorted(m.inspection_count for m in monkeys)
    return prod(inspection_counts[-2:])


def second():
    for i in range(10000):
        for monkey in monkeys:
            monkey.inspect_items(part_1=False)

    inspection_counts = sorted(m.inspection_count for m in monkeys)
    return prod(inspection_counts[-2:])


if __name__ == "__main__":
    content = get_input_content(__file__, split_by_lines=False)

    for raw_data in content.split('\n\n'):
        monkeys.append(Monkey(raw_data))

    # Calc of modulo by multiplying all the divisable monley's value in order to keep worry level acceptable
    prod_of_all_div = prod(m.div for m in monkeys)

    print(f'Le résultat de la première partie est :\n{first()}')

    # Reset monkeys list for part 2
    monkeys = []
    for raw_data in content.split('\n\n'):
        monkeys.append(Monkey(raw_data))

    print(f'Le résultat de la deuxième partie est :\n{second()}')
