from download_input import get_input_content


def first(grid):
    split_count = 0
    split_cols = set([grid[0].index('S')])
    row = 0

    while row < len(grid) - 2:
        row += 2
        new_split_cols = set()
        for col in split_cols:
            if grid[row][col] == '^':
                split_count += 1
                new_split_cols.add(col - 1)
                new_split_cols.add(col + 1)

        split_cols = new_split_cols

    return split_count


def second(grid):
    start_column = grid[0].index('S')
    timelines_per_columns = {start_column: 1}
    row = 0

    while row < len(grid) - 2:
        row += 2

        new_timelines_per_columns = {}
        for col, count in timelines_per_columns.items():
            if count:
                if grid[row][col] == '^':
                    left = col - 1
                    right = col + 1

                    new_timelines_per_columns[left] = new_timelines_per_columns.get(left, 0) + count
                    new_timelines_per_columns[right] = new_timelines_per_columns.get(right, 0) + count
                else:
                    new_timelines_per_columns[col] = new_timelines_per_columns.get(col, 0) + count

        timelines_per_columns = new_timelines_per_columns

    return sum(timelines_per_columns.values())


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''
    # if test_input:
    #     content = test_input.split('\n')

    grid = [list(line) for line in content]

    print(f'Le résultat de la première partie est :\n{first(grid)}')

    print(f'Le résultat de la deuxième partie est :\n{second(grid)}')