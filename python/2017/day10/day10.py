test = ['3', '4', '1', '5']

test1 = ''
test2 = 'AoC 2017'
test3 = '1,2,3'
test4 = '1,2,4'

size = 256


def first(input):
    l = list(range(size))
    i = 0  # Current position
    skip_size = 0
    for length in input:
        length = int(length)
        if length > 1:
            if i + length < size:
                current_list = l[i:(i + length)]
            else:
                j = i
                count = 0
                current_list = []
                while count < length:
                    current_list.append(l[j % size])
                    j += 1
                    count += 1
            current_list = list(reversed(current_list))
            j = i
            count = 0
            while count < length:
                l[j % size] = current_list[count]
                j += 1
                count += 1
        i = (i + length + skip_size) % size
        skip_size += 1
    return l[0] * l[1]


def second(input):
    l = list(range(size))
    i = 0  # Current position
    skip_size = 0
    for _ in list(range(64)):
        for length in input:
            length = int(length)
            if length > 1:
                if i + length < size:
                    current_list = l[i:(i + length)]
                else:
                    j = i
                    count = 0
                    current_list = []
                    while count < length:
                        current_list.append(l[j % size])
                        j += 1
                        count += 1
                current_list = list(reversed(current_list))
                j = i
                count = 0
                while count < length:
                    l[j % size] = current_list[count]
                    j += 1
                    count += 1
            i = (i + length + skip_size) % size
            skip_size += 1

    result = []
    i = 0
    for _ in list(range(16)):
        result.append('{:02x}'.format(xor(l[i:(i + 16)])))
        i += 16
    return ''.join(result)


def prepare(input):
    ascii_codes = []
    for c in input:
        ascii_codes.append(ord(c))
    for add in [17, 31, 73, 47, 23]:
        ascii_codes.append(add)
    return ascii_codes


def xor(n):
    return n[0] ^ n[1] ^ n[2] ^ n[3] ^ n[4] ^ n[5] ^ n[6] ^ n[7] ^ n[8] ^ n[9] ^ n[10] ^ n[11] ^ n[12] ^ n[13] ^ n[14] ^ n[15]


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readline()
    content = content.split(',')

    print("1. Le résultat est " + str(first(content)))

    with open('input.txt', 'r') as f:
        content2 = f.readline()
    content2 = prepare(content2)
    print("2. Le noeud de hachage est " + second(content2))
