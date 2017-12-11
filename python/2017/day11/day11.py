test1 = 'ne,ne,ne'
test2 = 'ne,ne,sw,sw'
test3 = 'ne,ne,s,s'
test4 = 'se,sw,se,sw,sw'


def get_distance(x, y ,z):
    """ Documentation sur https://www.redblobgames.com/grids/hexagons """
    return int((abs(x) + abs(y) + abs(z)) / 2)


def first(input):
    x = 0
    y = 0
    z = 0
    max = 0
    for dir in input:
        if dir == 'n':
            y += 1
            z -= 1
        elif dir == 's':
            y -= 1
            z += 1
        elif dir == 'ne':
            x += 1
            z -= 1
        elif dir == 'nw':
            x -= 1
            y += 1
        elif dir == 'se':
            y -= 1
            x += 1
        elif dir == 'sw':
            x -= 1
            z += 1
        if get_distance(x, y , z) > max:
            max = get_distance(x, y, z)
    return get_distance(x, y, z), max


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readline()

    dist, max = first(content.split(','))

    print("1. La distance parcourue est " + str(dist))
    print("1. La distance maximale atteinte est " + str(max))