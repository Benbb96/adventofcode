def generate(value, factor):
    return (value * factor) % 2147483647


def first():
    match = 0
    factorA = 16807
    factorB = 48271
    a = 679
    b = 771
    for i in range(40000000):
        # print(i)
        # print(a)
        # print(b)
        a = generate(a, factorA)
        b = generate(b, factorB)
        # print(format(a, '032b'))
        # print(format(b, '032b'))
        binA = format(a, '032b')
        binB = format(b, '032b')
        binA = binA[16:32]
        binB = binB[16:32]
        # print(binA)
        # print(binB)
        if binA == binB:
            match += 1

    return match

if __name__ == "__main__":

    print("1. Le nombre de match est " + str(first()))
