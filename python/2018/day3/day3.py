import numpy as np


test = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""


def first(input):
    fabric = np.zeros((1000, 1000))

    alive = set()
    dead = set()
    for line in input:
        id, at, pos, size = line.split()
        id = int(id[1:])
        x, y = pos.split(',')
        y = y[0:-1]  # remove the :
        width, length = size.split('x')
        # print('%s:%s - %sx%s' % (x, y, width, length))
        i = int(x)
        while i < int(x) + int(width):
            if id not in dead:
                alive.add(id)
            j = int(y)
            while j < int(y) + int(length):
                if fabric[i, j] != 0:
                    if int(fabric[i, j]) in alive:
                        alive.remove(int(fabric[i, j]))
                        dead.add(int(fabric[i, j]))
                        if id in alive:
                            alive.remove(id)
                            dead.add(id)
                    fabric[i, j] = -1
                else:
                    fabric[i, j] = id
                j += 1
            i += 1
        print(alive)
        print(dead)
    print(alive)
    return (fabric == -1).sum()


def second(input):
    # Process
    return 2


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est " + str(first(content)))

    print("2. Le résultat est " + str(second(content)))
