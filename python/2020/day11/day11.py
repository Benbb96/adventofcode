def count_occupied_around(current_map, i, j):
    count = 0
    # Loop through each seat around seat given by i and j position
    for x in range(-1, 2):
        for y in range(-1, 2):
            # Check if target is at the edge
            if i + x < 0 or i + x >= len(current_map) or j + y < 0 or j + y >= len(current_map[0]):
                continue
            # Ignore itself
            if x == 0 and y == 0:
                continue
            # Increment count if target is an occupied seat
            if current_map[i+x][j+y] == '#':
                count += 1
    return count


def first(input):
    current_map = input.copy()
    prev_map = None
    while current_map != prev_map:
        prev_map = current_map.copy()
        next_map = []
        for i in range(len(input)):
            next_line = ''
            for j in range(len(current_map[i])):
                char = current_map[i][j]
                if char == '.':
                    next_line += '.'
                    continue

                count_occupied = count_occupied_around(current_map, i, j)
                if char == 'L' and count_occupied == 0:
                    next_line += '#'
                elif char == '#' and count_occupied >= 4:
                    next_line += 'L'
                else:
                    next_line += char
            next_map.append(next_line)
        current_map = next_map
    return sum(line.count('#') for line in current_map)


def count_occupied_in_visibility(current_map, i, j):
    count = 0
    directions = {
        (-1, -1): False,
        (-1, 0): False,
        (-1, 1): False,
        (0, -1): False,
        (0, 1): False,
        (1, -1): False,
        (1, 0): False,
        (1, 1): False,
    }
    level = 1
    while not all(directions.values()):
        for direction, done in directions.items():
            if done:
                continue
            x, y = direction
            target_x = i + x * level
            target_y = j + y * level
            if target_x < 0 or target_x >= len(current_map) or target_y < 0 or target_y >= len(current_map[0]):
                directions[direction] = True
                continue
            target = current_map[target_x][target_y]
            if target == '.':
                continue
            if target == '#':
                count += 1
            directions[direction] = True
        level += 1
    return count


def second(input):
    current_map = input.copy()
    prev_map = None
    while current_map != prev_map:
        prev_map = current_map.copy()
        next_map = []
        for i in range(len(input)):
            next_line = ''
            for j in range(len(current_map[i])):
                char = current_map[i][j]
                if char == '.':
                    next_line += '.'
                    continue
                count_occupied = count_occupied_in_visibility(current_map, i, j)
                if char == 'L' and count_occupied == 0:
                    next_line += '#'
                elif char == '#' and count_occupied >= 5:
                    next_line += 'L'
                else:
                    next_line += char
            next_map.append(next_line)
        current_map = next_map
    return sum(line.count('#') for line in current_map)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
