from math import prod


def count_trees(x_speed, y_speed, input):
    tree_encountered = 0
    x = y = 0

    row_nb = len(input)
    col_nb = len(input[0])

    while y < row_nb - y_speed:
        x += x_speed
        y += y_speed
        if input[y][x % col_nb] == '#':
            tree_encountered += 1

    return tree_encountered


def first(input):
    return count_trees(3, 1, input)


def second(input):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    slopes_tree_encountered = []

    for slope in slopes:
        x_speed = slope[0]
        y_speed = slope[1]
        slopes_tree_encountered.append(count_trees(x_speed, y_speed, input))

    return prod(slopes_tree_encountered)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [list(x.strip()) for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
