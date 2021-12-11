from math import prod

from python.download_input import get_input_content


ADJACENCY = {(0, 1), (-1, 0), (1, 0), (0, -1)}  # Adjacency matrix


# https://newbedev.com/pythonic-and-efficient-way-of-finding-adjacent-cells-in-grid
def get_adjacent_cells(grid, x, y):
    max_x = len(grid)
    max_y = len(grid[0])
    for dx, dy in ADJACENCY:
        if 0 <= (x + dx) < max_x and 0 <= y + dy < max_y:  # Boundaries check
            # yielding is usually faster than constructing a list and returning it if you're just using it once
            yield x + dx, y + dy, grid[y + dy][x + dx]


def first(grid):
    count = 0
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            is_min = True
            for n_x, n_y, neighbour in get_adjacent_cells(grid, x, y):
                if val >= neighbour:
                    is_min = False
                    break
            if is_min:
                count += val + 1

    return count


def get_basin_size(grid, x, y, already_visited):
    already_visited.add((x, y))
    size = 1
    for n_x, n_y, neighbour in get_adjacent_cells(grid, x, y):
        if (n_x, n_y) in already_visited or neighbour == 9:
            continue
        size += get_basin_size(grid, n_x, n_y, already_visited)
    return size


def second(grid):
    already_visited = set()
    basins_size = []
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if (x, y) in already_visited or val == 9:
                continue

            basins_size.append(get_basin_size(grid, x, y, already_visited))
    basins_size.sort()
    return prod(basins_size[-3:])


if __name__ == "__main__":
    content = get_input_content(__file__)

    grid_input = [list(map(int, line)) for line in content]

    print(f'Le résultat de la première partie est :\n{first(grid_input)}')

    print(f'Le résultat de la deuxième partie est :\n{second(grid_input)}')
