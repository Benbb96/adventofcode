
def resolve1(parts):
    total = None
    last_op = None
    for x in parts:
        if type(x) == list:
            x = resolve1(x)

        if total is None:
            total = int(x)
        else:
            if x in '+*':
                last_op = x
            else:
                x = int(x)
                if last_op == '+':
                    total += x
                elif last_op == '*':
                    total *= x
                else:
                    raise ValueError('No last_op')
    return str(total)


def resolve2(parts):
    if '*' in parts:
        total = 1
        subtotals = []
        for x in parts:
            if x == '*':
                total *= int(resolve2(subtotals))
                subtotals = []
            else:
                subtotals.append(x)
        total *= int(resolve2(subtotals))
    else:
        total = None
        for x in parts:
            if type(x) == list:
                x = resolve2(x)

            if total is None:
                total = int(x)
            elif x != '+':
                total += int(x)
    return str(total)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    result_1 = 0
    result_2 = 0
    for line in content:
        level = 0
        levels = {
            level: []
        }
        for part in line.split():
            if '(' in part:
                count = part.count('(')
                for _ in range(count):
                    level += 1
                    levels[level] = []
                levels[level].append(part[count:])
            elif ')' in part:
                count = part.count(')')
                levels[level].append(part[:-count])
                for _ in range(count):
                    level -= 1
                    levels[level].append(levels[level + 1])
            else:
                levels[level].append(part)

        result_1 += int(resolve1(levels[0]))
        result_2 += int(resolve2(levels[0]))

    print("1. Le résultat est %s" % result_1)

    print("2. Le résultat est %s" % result_2)
