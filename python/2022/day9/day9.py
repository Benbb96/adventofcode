from python.download_input import get_input_content


DIRECTIONS = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0),
}


def move_tail(hx: int, hy: int, tx: int, ty: int) -> tuple[int, int]:
    if hy == ty:
        if hx - tx > 1:
            tx += 1
        elif hx - tx < -1:
            tx -= 1
    elif hx == tx:
        if hy - ty > 1:
            ty += 1
        elif hy - ty < -1:
            ty -= 1
    else:
        if hx - tx > 1:
            tx += 1
            if hy > ty:
                ty += 1
            else:
                ty -= 1
        elif hx - tx < -1:
            tx -= 1
            if hy > ty:
                ty += 1
            else:
                ty -= 1
        elif hy - ty > 1:
            ty += 1
            if hx > tx:
                tx += 1
            else:
                tx -= 1
        elif hy - ty < -1:
            ty -= 1
            if hx > tx:
                tx += 1
            else:
                tx -= 1

    return tx, ty


def first(data):
    hx, hy, tx, ty = 0, 0, 0, 0
    tail_positions = set()
    for line in data:
        d, v = line.split()
        v = int(v)
        for _ in range(v):
            hx, hy = (hx + DIRECTIONS[d][0], hy + DIRECTIONS[d][1])
            tx, ty = move_tail(hx, hy, tx, ty)
            tail_positions.add((tx, ty))

    return len(tail_positions)


def second(data):
    knot_positions = [(0, 0) for _ in range(10)]
    tail_positions = set()
    for line in data:
        d, v = line.split()
        v = int(v)
        for _ in range(v):
            knot_positions[0] = (knot_positions[0][0] + DIRECTIONS[d][0], knot_positions[0][1] + DIRECTIONS[d][1])
            for i in range(9):
                hx, hy = knot_positions[i]
                tx, ty = knot_positions[i+1]
                knot_positions[i + 1] = move_tail(hx, hy, tx, ty)
            tail_positions.add(knot_positions[-1])

    return len(tail_positions)


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
