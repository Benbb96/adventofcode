def first(input):
    length = len(input)
    i = 0
    while i < length:
        j = 1
        while j < length:
            if input[i] + input[j] == 2020:
                return input[i] * input[j]
            j += 1
        i += 1


def second(input):
    length = len(input)
    i = 0
    while i < length:
        j = 0
        while j < length:
            k = 0
            while k < length:
                if input[i] + input[j] + input[k] == 2020:
                    return input[i] * input[j] * input[k]
                k += 1
            j += 1
        i += 1


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [int(x) for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
