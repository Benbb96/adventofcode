
def fuel(x):
    x = int(x)
    x = int(x / 3)
    x -= 2
    return x


def first(input):
    return sum(fuel(line) for line in input)


def second(input):
    sum = 0
    for line in input:
        x = fuel(line)
        while x > 0:
            sum += x
            x = fuel(x)
    return sum


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
