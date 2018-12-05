test = 'dabAcCaCBAcCcaDA'
minuscule = 'abcdefghijklmnopqrstuvwxyz'
majuscule = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def first(input):
    s = list(input)
    crash = True
    while crash:
        crash = False
        i = 1
        while i < len(s):
            a = s[i-1]
            b = s[i]
            # print('a=' + a)
            # print('b=' + b)
            if a in minuscule and b in majuscule and a == b.lower() or a in majuscule and b in minuscule and a.lower() == b:
                del s[i]
                del s[i-1]
                crash = True
            i += 1
    return len(s)


def second(input):
    min = 100000
    letter = ''
    for c in minuscule:
        # print(c)
        s = input.replace(c, '')
        s = s.replace(c.upper(), '')
        size = first(s)
        if size < min:
            min = size
            letter = c
    return min, letter


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readline()

    print("1. La taille minimum est %s" % first(content))
    min, letter = second(content)
    print("2. Le taille minimum est %d en retirant la lettre %c" % (min, letter))
