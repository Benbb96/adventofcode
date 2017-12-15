import random

test = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

groups = {}
count = set()
all = set()


def add_neighboors(neighboors):
    for neighboor in neighboors:
        if neighboor not in count:
            count.add(neighboor)
            all.remove(neighboor)
            add_neighboors(groups[neighboor])

def count_group(neighboors):
    for neighboor in neighboors:
        if neighboor in all:
            all.remove(neighboor)
            count_group(groups[neighboor])


def first(input):
    for line in input:
        n, neighboors = line.split(' <-> ')
        groups[n] = neighboors.split(', ')
        all.add(n)

    count.add('0')
    all.remove('0')
    add_neighboors(groups['0'])
    return len(count)


def second(input):
    i = 1
    while len(all) > 0:
        e = all.pop()
        count_group(groups[e])
        i +=1
    return i


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    test = test.split('\n')
    print("1. Le résultat est " + str(first(content)))

    print("2. Le résultat est " + str(second(content)))
