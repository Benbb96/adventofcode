import sys
from collections import Counter


def first(input):
    # My solution which wasn't working..
    # b = {}
    # for line in input:
    #     a = {}
    #     for c in line:
    #         if c in a:
    #             a[c] += 1
    #         else:
    #             a[c] = 1
    #     print(a)
    #     for key, val in a.items():
    #         if val > 1:
    #             if val in b.keys():
    #                 b[val].add(key)
    #             else:
    #                 b[val] = {key}
    #     print(b)
    #
    # o = []
    # for h in b.values():
    #     o.append(len(h))

    # Solution from reddit
    c = [0, 0]
    for i in input:
        a = [j for i, j in Counter(i).most_common()]
        if 3 in a:
            c[0] += 1
        if 2 in a:
            c[1] += 1

    return str(c[0] * c[1])


def second(input):
    i = 0
    l = len(input)
    min = sys.maxsize
    r = ['', '']
    while i < l -1:
        j = i +1
        while j < l:
            x = sum(1 for a, b in zip(input[i], input[j]) if a != b)  # Number of differences between the two
            if x < min:
                min = x
                r = [input[i], input[j]]
            j += 1
        i += 1

    l = len(r[0])
    i = 0
    end = []
    while i < l:
        if r[0][i] == r[1][i]:
            end.append(r[0][i])
        i += 1
    return ''.join(end)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print('1. Le checksum est : ' + first(content))
    print('2. Les lettres en communs sont : ' + second(content))
