from itertools import count


def first(input):
    start = int(input[0])
    bus_ids = sorted([int(bus) for bus in input[1].split(',') if bus != 'x'])
    earliest_bus = None
    i = start
    while earliest_bus is None:
        for bus_id in bus_ids:
            if i % bus_id == 0:
                earliest_bus = bus_id
                break
        if not earliest_bus:
            i += 1

    return (i - start) * earliest_bus


def second(input):
    bus_ids = [int(bus) if bus != 'x' else -1 for bus in input[1].split(',')]

    maximum = max(bus_ids)
    pos_max = bus_ids.index(maximum)
    i = maximum
    earliest_timestamp = None
    while earliest_timestamp is None:
        ok = True
        for index, bus_id in enumerate(bus_ids):
            if bus_id != -1:
                current_timestamp = i - (pos_max - index)
                if current_timestamp % bus_id != 0:
                    ok = False
                    break
        if ok:
            earliest_timestamp = i - pos_max
        i += maximum
        print(f'{i=}')

    return earliest_timestamp


def second_with_solution(input):
    n = int(input[0])
    buses = tuple((i, int(b)) for i, b in enumerate(input[1].split(',')) if b != 'x')
    step = 1
    for i, b in buses:
        n = next(c for c in count(n, step) if (c + i) % b == 0)
        step *= b
    return n


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second_with_solution(content))
