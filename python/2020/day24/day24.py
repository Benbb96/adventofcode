from functools import lru_cache

black_tiles = []


def first(input):
    for line in input:
        i = 0
        x = y = 0
        while i < len(line):
            increment = 2
            if line[i] == 'e':
                x += 2
                increment = 1
            elif line[i] == 'w':
                x -= 2
                increment = 1
            elif line[i:i+2] == 'se':
                x += 1
                y -= 1
            elif line[i:i+2] == 'sw':
                x -= 1
                y -= 1
            elif line[i:i+2] == 'nw':
                x -= 1
                y += 1
            elif line[i:i+2] == 'ne':
                x += 1
                y += 1
            i += increment
        position = (x, y)
        if position in black_tiles:
            black_tiles.remove(position)
        else:
            black_tiles.append(position)

    return len(black_tiles)


@lru_cache
def get_neighbors(position):
    neighbors = []
    for x in [-1, 1]:
        for y in [-1, 1]:
            neighbors.append((position[0] + x, position[1] + y))
    for x in [-2, 2]:
        neighbors.append((position[0] + x, position[1]))
    return neighbors


def second():
    global black_tiles
    for day in range(100):
        to_remove = []
        to_add = []
        white_tiles = set()
        for black_tile in black_tiles:
            neighbors = get_neighbors(black_tile)
            black_neighbors = 0
            for neighbor in neighbors:
                if neighbor in black_tiles:
                    black_neighbors += 1
                else:
                    white_tiles.add(neighbor)
            if black_neighbors == 0 or black_neighbors > 2:
                to_remove.append(black_tile)
        for white_tile in white_tiles:
            neighbors = get_neighbors(white_tile)
            black_neighbors = 0
            for neighbor in neighbors:
                if neighbor in black_tiles:
                    black_neighbors += 1
            if black_neighbors == 2:
                to_add.append(white_tile)
        black_tiles = [item for item in black_tiles if item not in to_remove]
        black_tiles += to_add
        print(day+1, len(black_tiles))
    return len(black_tiles)


if __name__ == "__main__":
    with open('test.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second())
