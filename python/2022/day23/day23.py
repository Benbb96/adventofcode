from python.download_input import get_input_content


UP = (0, -1)
DOWN = (0, 1)
WEST = (-1, 0)
EAST = (1, 0)

MAPPING = {
    UP: [(i, -1) for i in range(-1, 2)],
    DOWN: [(i, 1) for i in range(-1, 2)],
    WEST: [(-1, i) for i in range(-1, 2)],
    EAST: [(1, i) for i in range(-1, 2)]
}

NEIGHBOURS = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
NEIGHBOURS.remove((0, 0))


def first(data):
    elves = set()

    for y, line in enumerate(data):
        for x, item in enumerate(line):
            if item == "#":
                elves.add((x, y))

    moves = [UP, DOWN, WEST, EAST]

    for _ in range(10):
        once = set()
        twice = set()

        for x, y in elves:
            if all((x + dx, y + dy) not in elves for dx, dy in NEIGHBOURS):
                continue
            for move in moves:
                if all((x + dx, y + dy) not in elves for dx, dy in MAPPING[move]):
                    prop = (x + move[0], y + move[1])
                    if prop in twice:
                        pass
                    elif prop in once:
                        twice.add(prop)
                    else:
                        once.add(prop)
                    break

        elves_copy = set(elves)
        for x, y in elves_copy:
            if all((x + dx, y + dy) not in elves_copy for dx, dy in NEIGHBOURS):
                continue
            for move in moves:
                if all((x + dx, y + dy) not in elves_copy for dx, dy in MAPPING[move]):
                    prop = (x + move[0], y + move[1])
                    if prop not in twice:
                        elves.remove((x, y))
                        elves.add(prop)
                    break

        moves.append(moves.pop(0))

    min_x = min(x for x, y in elves)
    max_x = max(x for x, y in elves)
    min_y = min(y for x, y in elves)
    max_y = max(y for x, y in elves)

    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)


def second(data):
    elves = set()

    for y, line in enumerate(data):
        for x, item in enumerate(line):
            if item == "#":
                elves.add((x, y))

    moves = [UP, DOWN, WEST, EAST]

    last = set(elves)
    round = 1

    while True:
        once = set()
        twice = set()

        for x, y in elves:
            if all((x + dx, y + dy) not in elves for dx, dy in NEIGHBOURS):
                continue
            for move in moves:
                if all((x + dx, y + dy) not in elves for dx, dy in MAPPING[move]):
                    prop = (x + move[0], y + move[1])
                    if prop in twice:
                        pass
                    elif prop in once:
                        twice.add(prop)
                    else:
                        once.add(prop)
                    break

        elves_copy = set(elves)
        for x, y in elves_copy:
            if all((x + dx, y + dy) not in elves_copy for dx, dy in NEIGHBOURS):
                continue
            for move in moves:
                if all((x + dx, y + dy) not in elves_copy for dx, dy in MAPPING[move]):
                    prop = (x + move[0], y + move[1])
                    if prop not in twice:
                        elves.remove((x, y))
                        elves.add(prop)
                    break

        moves.append(moves.pop(0))

        if last == elves:
            break

        last = set(elves)
        round += 1

    return round


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
