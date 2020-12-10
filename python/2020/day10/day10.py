

def first(input):
    differences = {1: 0, 2: 0, 3: 0}
    score = 0
    for number in input:
        diff = number - score
        differences[diff] += 1
        score = number
    differences[3] += 1
    return differences[1] * differences[3]


def second(input):
    # Had to look on reddit for this one... #DynamicProgramming
    ways = [0] * (input[-1] + 1)
    ways[0] = 1
    for n in input:
        ways[n] = ways[n-3] + ways[n-2] + ways[n-1]
    return ways[-1]


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = sorted([int(x.strip()) for x in content])

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
