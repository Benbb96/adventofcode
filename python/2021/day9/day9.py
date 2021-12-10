from python.download_input import get_input_content


ADJACENCY = {(0, 1), (-1, 0), (1, 0), (0, -1)}  # Adjacency matrix


# https://newbedev.com/pythonic-and-efficient-way-of-finding-adjacent-cells-in-grid
def get_adjacent_cells(grid, x, y, max_x, max_y):
    for dx, dy in ADJACENCY:
        if 0 <= (x + dx) < max_x and 0 <= y + dy < max_y:  # Boundaries check
            # yielding is usually faster than constructing a list and returning it if you're just using it once
            yield grid[y + dy][x + dx]


def first(data):
    grid = []
    for line in data:
        grid.append(list(map(int, line)))

    count = 0
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            is_min = True
            for neighbour in get_adjacent_cells(grid, x, y, len(row), len(grid)):
                print(val, neighbour)
                if val >= neighbour:
                    is_min = False
                    break
            if is_min:
                count += val + 1

    return count


def second(data):
    return 2


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''2199943210
3987894921
9856789892
8767896789
9899965678'''
    # if test_input:
    #     content = test_input.split('\n')

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
