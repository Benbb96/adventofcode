from copy import deepcopy

from python.download_input import get_input_content


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def first(data):
    start_pos = target_pos = None
    for i, r in enumerate(data):
        for j, c in enumerate(r):
            if c == 'S':
                start_pos = (i, j)
                data[i][j] = 'a'
            elif c == 'E':
                target_pos = (i, j)
                data[i][j] = 'z'

    assert start_pos is not None
    assert target_pos is not None

    bfs = [[-1 for _ in r] for r in data]
    bfs[start_pos[0]][start_pos[1]] = 0
    to_visit = [start_pos]

    while len(to_visit):
        pos_y, pos_x = to_visit.pop()
        current_cell = data[pos_y][pos_x]
        for dy, dx in DIRECTIONS:
            tx = pos_x + dx
            ty = pos_y + dy
            if tx in range(len(data[0])) and ty in range(len(data)):
                target_cell = data[ty][tx]
                if ord(target_cell) <= ord(current_cell) + 1 and (bfs[ty][tx] < 0 or bfs[ty][tx] > bfs[pos_y][pos_x] + 1):
                    bfs[ty][tx] = bfs[pos_y][pos_x] + 1
                    to_visit.append((pos_y + dy, pos_x + dx))

    return bfs[target_pos[0]][target_pos[1]]


def second(data):
    # Same but go from z to a

    start_pos = None
    for i, r in enumerate(data):
        for j, c in enumerate(r):
            if c == 'S':
                data[i][j] = 'a'
            elif c == 'E':
                start_pos = (i, j)
                data[i][j] = 'z'

    bfs = [[-1 for _ in r] for r in data]
    bfs[start_pos[0]][start_pos[1]] = 0
    to_visit = [start_pos]

    while len(to_visit):
        pos_y, pos_x = to_visit.pop()
        current_cell = data[pos_y][pos_x]
        for dy, dx in DIRECTIONS:
            tx = pos_x + dx
            ty = pos_y + dy
            if tx in range(len(data[0])) and ty in range(len(data)):
                target_cell = data[ty][tx]
                if ord(target_cell) >= ord(current_cell) - 1 and (bfs[ty][tx] < 0 or bfs[ty][tx] > bfs[pos_y][pos_x] + 1):
                    bfs[ty][tx] = bfs[pos_y][pos_x] + 1
                    to_visit.append((pos_y + dy, pos_x + dx))

    distances = []
    for i, r in enumerate(bfs):
        for j, c in enumerate(r):
            if data[i][j] == 'a' and c != -1:
                distances.append(c)

    return min(distances)


if __name__ == "__main__":
    content = get_input_content(__file__)

    grid = [list(row) for row in content]

    print(f'Le résultat de la première partie est :\n{first(deepcopy(grid))}')

    print(f'Le résultat de la deuxième partie est :\n{second(deepcopy(grid))}')
