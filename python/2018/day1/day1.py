def first(input):
    frequency = 0
    for line in input:
        val = int(line[1:])
        if line[0] == '+':
            frequency += val
        else:
            frequency -= val
    return str(frequency)


def second(input):
    frequency = 0
    memory = [0]
    twice = None
    while twice is None:
        for line in input:
            val = int(line[1:])
            if line[0] == '+':
                frequency += val
            else:
                frequency -= val
            if frequency in memory:
                twice = frequency
                break
            else:
                memory.append(frequency)
    return str(twice)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print('1. Le total est : ' + first(content))
    print('2. Le nombre atteint deux fois est : ' + second(content))
