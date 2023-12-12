from python.download_input import get_input_content

mapping = {
    ('7', 'E'): 'S',
    ('7', 'N'): 'W',
    ('J', 'S'): 'W',
    ('J', 'E'): 'N',
    ('L', 'W'): 'N',
    ('L', 'S'): 'E',
    ('F', 'N'): 'E',
    ('F', 'W'): 'S',
}


def first(grid: list[list[str]], sx: int, sy: int) -> int:
    x = sx
    y = sy + 1  # Start one step down
    d = 'S'
    step = 1

    while x != sx or y != sy:
        pipe = grid[y][x]
        d = mapping.get((pipe, d), d)
        match d:
            case 'E':
                x += 1
            case 'S':
                y += 1
            case 'W':
                x -= 1
            case 'N':
                y -= 1
        step += 1

    return int(step / 2)


def second(data):
    return 2


if __name__ == "__main__":
    content = get_input_content(__file__)

    grid = []
    sx = None
    sy = None
    for i, line in enumerate(content):
        grid.append(list(line))
        if 'S' in line:
            sy = i
            sx = line.index('S')

    print(f'Le résultat de la première partie est :\n{first(grid, sx, sy)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
