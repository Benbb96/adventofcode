import numpy as np


test = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""


def first(input):
    fabric = np.zeros((1000, 1000))

    for line in input:
        id, at, pos, size = line.split()
        x, y = pos.split(',')
        y = y[0:-1]  # remove the :
        width, length = size.split('x')

        # print('%s:%s - %sx%s' % (x, y, width, length))
        i = int(x)
        while i < int(x) + int(width):
            j = int(y)
            while j < int(y) + int(length):
                if fabric[i,j] != 0:
                    fabric[i, j] = '-1'
                else:
                    fabric[i, j] = id[1:]
                j +=1
            i += 1

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
