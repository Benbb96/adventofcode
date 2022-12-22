import re

from python.download_input import get_input_content


turn_right = {
    'R': 'D',
    'D': 'L',
    'L': 'U',
    'U': 'R'
}

turn_left = {
    'R': 'U',
    'U': 'L',
    'L': 'D',
    'D': 'R'
}


def first(board, path):
    pos_x = pos_y = None
    direction = 'R'
    tiles = []
    walls = []

    for y, line in enumerate(board):
        for x, cell in enumerate(line):
            if cell == ' ':
                continue
            tiles.append((x, y))
            if cell == '.':
                # Set starting position at first tiles seen
                if pos_x is None and pos_y is None:
                    pos_x = x
                    pos_y = y
            if cell == '#':
                walls.append((x, y))

    # Read path
    for instruction in re.findall(r'(\d+|[RL])', path):
        try:
            steps = int(instruction)
        except ValueError:
            match instruction:
                case 'R': direction = turn_right[direction]
                case 'L': direction = turn_left[direction]
                case _: raise ValueError(f'{instruction} not recognized')
        else:
            for i in range(steps):
                # Find next_position
                next_x = pos_x
                next_y = pos_y
                match direction:
                    case 'R':
                        next_x += 1
                        if (next_x, next_y) not in tiles:
                            next_x = 0
                            while (next_x, next_y) not in tiles:
                                next_x += 1
                    case 'D':
                        next_y += 1
                        if (next_x, next_y) not in tiles:
                            next_y = 0
                            while (next_x, next_y) not in tiles:
                                next_y += 1
                    case 'L':
                        next_x -= 1
                        if (next_x, next_y) not in tiles:
                            next_x = len(board[0])
                            while (next_x, next_y) not in tiles:
                                next_x -= 1
                    case 'U':
                        next_y -= 1
                        if (next_x, next_y) not in tiles:
                            next_y = len(board)
                            while (next_x, next_y) not in tiles:
                                next_y -= 1

                # Check if it is a wall
                if (next_x, next_y) in walls:
                    # Stop here
                    break

                # Check if it is a tile
                if (next_x, next_y) in tiles:
                    # Go forward
                    pos_x = next_x
                    pos_y = next_y

    return 1000 * (pos_y + 1) + 4 * (pos_x + 1) + 'RDLU'.index(direction)


def second(board, path):
    return 2


if __name__ == "__main__":
    content = get_input_content(__file__, split_by_lines=False)
    test_input = '''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5'''
    # if test_input:
    #     content = test_input\

    board, path = content.split('\n\n')
    board = board.split('\n')

    print(f'Le résultat de la première partie est :\n{first(board, path)}')

    print(f'Le résultat de la deuxième partie est :\n{second(board, path)}')
