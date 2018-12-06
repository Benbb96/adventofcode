import numpy as np


test = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".split('\n')


class Point:
    def __init__(self, x, y, name):
        self.col = x
        self.row = y
        self.name = name
        self.is_infinite = False

    def __str__(self):
        return '%d : %d-%d (%s)' % (self.name, self.col, self.row, 'Infini' if self.is_infinite else 'Fini')

    def distance(self, point):
        return abs(point.col - self.row) + abs(point.row - self.col)


def first(input):
    points = []
    name = 0
    max_col = max_row = 0
    min_col = min_row = 1e5
    for line in test:
        name += 1
        x, y = map(int, line.split(', '))
        max_col = max(max_col, x)
        max_row = max(max_row, y)
        min_col = min(min_col, x)
        min_row = min(min_row, y)
        points.append(Point(x, y, name))
    print(max_col)
    print(max_row)

    for point in points:
        if point.col == min_col or point.col == max_col or point.row == min_row or point.row == max_row:
            point.is_infinite = True
        print(point)

    cp_points = points.copy()
    area = np.zeros((max_row+1, max_col+1))
    col = 0
    while col <= max_col:
        row = 0
        while row <= max_row:
            for point in cp_points:
                if row == point.row and col == point.col:
                    area[row, col] = point.name
                    cp_points.remove(point)
            row += 1
        col += 1

    dist = 1
    while dist < 3:
        for point in points:
            if point.row - dist > min_row and area[point.row - dist, point.col] == 0:
                area[point.row - dist, point.col] = point.name
            if point.col - dist > min_col and area[point.row, point.col - dist] == 0:
                area[point.row, point.col - dist] = point.name
            if point.row + dist <= max_row and area[point.row + dist, point.col] == 0:
                area[point.row + dist, point.col] = point.name
            if point.col + dist <= max_col and area[point.row, point.col + dist] == 0:
                area[point.row, point.col + dist] = point.name
        print(area)
        dist += 1

    return 1


def second(input):
    # Process
    return 2


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
