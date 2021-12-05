from python.download_input import get_input_content


def set_on_grid(grid, pos):
    if pos in grid:
        grid[pos] += 1
    else:
        grid[pos] = 1


def first(data):
    grid = {}
    for line in data:
        a, b = line.split(' -> ')
        x1, y1 = map(int, a.split(','))
        x2, y2 = map(int, b.split(','))
        if x1 == x2:
            # Horizontal lines
            increment = 1 if y1 < y2 else -1
            i = y1
            while i != y2:
                set_on_grid(grid, (x1, i))
                i += increment
            set_on_grid(grid, (x1, i))
        elif y1 == y2:
            # Vertical lines
            increment = 1 if x1 < x2 else -1
            i = x1
            while i != x2:
                set_on_grid(grid, (i, y1))
                i += increment
            set_on_grid(grid, (i, y1))
    count = 0
    for value in grid.values():
        if value > 1:
            count += 1
    return count


def second(data):
    grid = {}
    for line in data:
        a, b = line.split(' -> ')
        x1, y1 = map(int, a.split(','))
        x2, y2 = map(int, b.split(','))
        if x1 == x2:
            increment = 1 if y1 < y2 else -1
            i = y1
            while i != y2:
                set_on_grid(grid, (x1, i))
                i += increment
            set_on_grid(grid, (x1, i))
        elif y1 == y2:
            increment = 1 if x1 < x2 else -1
            i = x1
            while i != x2:
                set_on_grid(grid, (i, y1))
                i += increment
            set_on_grid(grid, (i, y1))
        else:
            # Diagonal lines
            increment_x = 1 if x1 < x2 else -1
            increment_y = 1 if y1 < y2 else -1
            i = x1
            j = y1
            while i != x2 and j != y2:
                set_on_grid(grid, (i, j))
                i += increment_x
                j += increment_y
            set_on_grid(grid, (i, j))
    count = 0
    for value in grid.values():
        if value > 1:
            count += 1
    return count


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
