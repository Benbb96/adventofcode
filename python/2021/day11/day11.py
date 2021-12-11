from python.download_input import get_input_content


ADJACENCY = {(1, 1), (0, 1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, -1), (-1, -1)}  # Adjacency matrix


# https://newbedev.com/pythonic-and-efficient-way-of-finding-adjacent-cells-in-grid
def get_adjacent_cells(grid, x, y):
    max_x = len(grid)
    max_y = len(grid[0])
    for dx, dy in ADJACENCY:
        if 0 <= (x + dx) < max_x and 0 <= y + dy < max_y:  # Boundaries check
            # yielding is usually faster than constructing a list and returning it if you're just using it once
            yield x + dx, y + dy, grid[y + dy][x + dx]


def first(grid):
    max_x = len(grid)
    max_y = len(grid[0])
    count = 0
    for step in range(1, 100+1):
        next_grid = grid.copy()
        flashes = []
        already_flashed = set()
        for x in range(max_x):
            for y in range(max_y):
                grid[x][y] += 1
                if grid[x][y] > 9:
                    flashes.append((x, y))

        while flashes:
            x, y = flashes.pop()
            if (x, y) not in already_flashed:
                already_flashed.add((x, y))
                next_grid[x][y] = 0
                count += 1
                # Increase neighbors
                for n_x, n_y, neighbour in get_adjacent_cells(grid, x, y):
                    if grid[n_x][n_y] > 0:
                        grid[n_x][n_y] += 1
                        if grid[n_x][n_y] > 9:
                            flashes.append((n_x, n_y))

        grid = next_grid
    return count


def second(grid):
    max_x = len(grid)
    max_y = len(grid[0])
    count = step = 0
    already_flashed = set()
    while len(already_flashed) < max_x * max_y:
        next_grid = grid.copy()
        flashes = []
        already_flashed = set()
        for x in range(max_x):
            for y in range(max_y):
                grid[x][y] += 1
                if grid[x][y] > 9:
                    flashes.append((x, y))

        while flashes:
            x, y = flashes.pop()
            if (x, y) not in already_flashed:
                already_flashed.add((x, y))
                next_grid[x][y] = 0
                count += 1
                # Increase neighbors
                for n_x, n_y, neighbour in get_adjacent_cells(grid, x, y):
                    if grid[n_x][n_y] > 0:
                        grid[n_x][n_y] += 1
                        if grid[n_x][n_y] > 9:
                            flashes.append((n_x, n_y))

        grid = next_grid
        step += 1

    return step


if __name__ == "__main__":
    content = get_input_content(__file__)

    grid_input = [list(map(int, line)) for line in content]

    print(f'Le résultat de la première partie est :\n{first(grid_input)}')

    print(f'Le résultat de la deuxième partie est :\n{second(grid_input)}')
