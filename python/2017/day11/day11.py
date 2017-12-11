test1 = 'ne,ne,ne'
test2 = 'ne,ne,sw,sw'
test3 = 'ne,ne,s,s'
test4 = 'se,sw,se,sw,sw'


def first(input):
    axe1 = 0
    axe2 = 0
    axe3 = 0
    for dir in input:
        if dir == 'n':
            axe1 += 1
        elif dir == 's':
            axe1 -= 1
        elif dir == 'ne':
            axe2 += 1
        elif dir == 'nw':
            axe3 += 1
        elif dir == 'se':
            axe3 -= 1
        elif dir == 'sw':
            axe2 -= 1
    print(axe1)
    print(axe2)
    print(axe3)
    print(abs(axe1) + abs(axe2) + abs(axe3))


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readline()

    first(test4.split(','))