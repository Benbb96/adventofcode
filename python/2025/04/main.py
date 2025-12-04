from download_input import get_input_content


ADJACENCY = {(1, 1), (0, 1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, -1), (-1, -1)}  # Adjacency matrix


def first(data):
    count = 0
    grid = [list(line) for line in data]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                adjacent = 0
                for dx, dy in ADJACENCY:
                    if 0 <= i + dy < len(grid) and 0 <= j + dx < len(grid[0]) and grid[i + dy][j + dx] == '@':
                        adjacent += 1
                if adjacent < 4:
                    count += 1

    return count


def second(data):
    count = 0
    prev_count = -1
    grid = [list(line) for line in data]
    to_remove = []
    while count > prev_count:
        prev_count = count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    adjacent = 0
                    for dx, dy in ADJACENCY:
                        if 0 <= i + dy < len(grid) and 0 <= j + dx < len(grid[0]) and grid[i + dy][j + dx] == '@':
                            adjacent += 1
                    if adjacent < 4:
                        count += 1
                        to_remove.append((i, j))

        for i, j in to_remove:
            grid[i][j] = '.'

    return count


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''
    # if test_input:
    #     content = test_input.split('\n')

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
