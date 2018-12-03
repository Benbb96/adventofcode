from math import sqrt

rules2 = {}
rules3 = {}


def get_size(pattern):
    return int(sqrt(len(pattern)))


def count_pixel_on(pattern):
    count = 0
    for pixel in pattern:
        if pixel == '#':
            count += 1
    return count


def follow_rule(pattern, size):
    """Return which the output pattern following the corresponding rule"""
    if size % 2 == 0:
        if pattern in rules2.keys():
            return rules2[pattern]
    else:  # Size 3
        if pattern in rules3.keys():
            return rules3[pattern]


def first(iteration):
    art = '.#./..#/###'
    for i in range(iteration):
        print('Iteration ' + str(i+1))
        print(art)
        size = get_size(art)
        if size % 2 == 0:
            # divide by 2*2 squares
            print('2')
        elif size % 3 == 0 :
            #divide by 3*3 squares
            print('3')
            art = follow_rule(art, size)
    print(art)

    return count_pixel_on(art)


def second(input):
    # Process
    return 2


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        # content = f.readlines()
        content = f.readline()
    content = [x.strip() for x in content]

    # Tests
    rule2 = '../.# => ##./#../...'
    rule3 = '.#./..#/### => #..#/..../..../#..#'
    rules2[rule2.split(' => ')[0]] = rule2.split(' => ')[1]
    rules3[rule3.split(' => ')[0]] = rule3.split(' => ')[1]

    print("1. Le résultat est " + str(first(2)))

    #print("2. Le résultat est " + str(second(content)))
