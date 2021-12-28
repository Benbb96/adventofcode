import re
from python.download_input import get_input_content


def first(data):
    points = set()
    fold_instructions = []
    for line in data:
        if ',' in line:
            x, y = map(int, line.split(','))
            points.add((x, y))
        elif line:
            number = int(re.findall(r'\d+', line)[0])
            if 'x' in line:
                fold_instructions.append(('x', number))
            else:
                fold_instructions.append(('y', number))
    print(points)
    for instruction in fold_instructions[:1]:
        print(instruction)
        final_points = set()
        for x, y in points:
            if instruction[0] == 'y' and y > instruction[1]:
                final_points.add((x, instruction[1] - (y - instruction[1])))
            if instruction[0] == 'x' and x > instruction[1]:
                final_points.add((instruction[1] - (x - instruction[1]), y))
            else:
                final_points.add((x, y))
    print(final_points)
    return len(final_points)


def second(data):
    points = set()
    fold_instructions = []
    for line in data:
        if ',' in line:
            x, y = map(int, line.split(','))
            points.add((x, y))
        elif line:
            number = int(re.findall(r'\d+', line)[0])
            if 'x' in line:
                fold_instructions.append(('x', number))
            else:
                fold_instructions.append(('y', number))

    for instruction in fold_instructions:
        next_points = set()
        for x, y in points:
            if instruction[0] == 'y' and y > instruction[1]:
                next_points.add((x, instruction[1] - (y - instruction[1])))
            if instruction[0] == 'x' and x > instruction[1]:
                next_points.add((instruction[1] - (x - instruction[1]), y))
            else:
                next_points.add((x, y))
        points = next_points

    print(points)
    for y in range(max(i[0] for i in points)):
        for x in range(max(i[1] for i in points)):
            if (x, y) in points:
                print('#', end = '')
            else:
                print('.', end = '')
        print()

    return


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''
    #if test_input:
        #content = test_input.split('\n')

    #print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
