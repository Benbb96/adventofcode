def dichotomy(line):
    total_range = 2**len(line)
    minimum = 0
    maximum = total_range - 1
    for letter in line:
        total_range = total_range / 2
        if letter == 'F' or letter == 'L':
            maximum -= total_range
        elif letter == 'B' or letter == 'R':
            minimum += total_range
    assert minimum == maximum
    return int(minimum)


def get_seat_ids(input):
    seat_ids = []
    for line in input:
        first = line[:7]
        second = line[-3:]
        row = dichotomy(first)
        column = dichotomy(second)
        seat_ids.append(row * 8 + column)
    return seat_ids


def first(input):
    return max(get_seat_ids(input))


def second(input):
    seat_ids = get_seat_ids(input)
    all_seats = [n for n in range(1024)]
    missing = list(set(all_seats) - set(seat_ids))
    for miss in missing:
        if miss - 1 in seat_ids and miss + 1 in seat_ids:
            return miss


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
