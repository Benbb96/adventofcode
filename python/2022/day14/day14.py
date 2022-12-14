from copy import deepcopy

from python.download_input import get_input_content


LENGTH = 700
HEIGTH = 200


def move_sand(data, sand_y, sand_x):
    while True:
        if data[sand_y + 1][sand_x] == '.':
            sand_y += 1
        elif data[sand_y + 1][sand_x - 1] == '.':
            sand_y += 1
            sand_x -= 1
        elif data[sand_y + 1][sand_x + 1] == '.':
            sand_y += 1
            sand_x += 1
        else:
            break
    return sand_y, sand_x


def first(data):
    tick = 0
    while True:
        sand_x = 500
        sand_y = 0

        try:
            sand_y, sand_x = move_sand(data, sand_y, sand_x)
        except IndexError:
            # We touch the Abyss !
            return tick

        data[sand_y][sand_x] = 'o'
        tick += 1


def second(data):
    max_y = max(n for n, r in enumerate(data) if '#' in r) + 2
    for n in range(LENGTH):
        data[max_y][n] = '#'

    tick = 0
    while True:
        sand_x = 500
        sand_y = 0

        if data[sand_y][sand_x] == 'o':
            # Source of Sand has been reached
            return tick

        sand_y, sand_x = move_sand(data, sand_y, sand_x)

        data[sand_y][sand_x] = 'o'
        tick += 1


if __name__ == "__main__":
    content = get_input_content(__file__)

    # Parse the grid
    grid = [(['.'] * LENGTH) for _ in range(HEIGTH)]
    grid[0][500] = '+'  # Set source of sand
    for line in content:
        points = line.split(' -> ')
        i = 1
        while i < len(points):
            x1, y1 = map(int, points[i - 1].split(','))
            x2, y2 = map(int, points[i].split(','))
            x_range = range(x1, x2 + 1) if x1 <= x2 else range(x2, x1 + 1)
            y_range = range(y1, y2 + 1) if y1 <= y2 else range(y2, y1 + 1)
            for x in x_range:
                for y in y_range:
                    grid[y][x] = '#'
            i += 1

    print(f'Le résultat de la première partie est :\n{first(deepcopy(grid))}')

    print(f'Le résultat de la deuxième partie est :\n{second(deepcopy(grid))}')
