instructions = 's1,x3/4,pe/b'

def rotate(strg,n):
    return strg[n:] + strg[:n]


def first(input, test):

    for instruction in input:
        if instruction[0] == 's':
            loop = int(instruction[1:])
            #print('Spin ' + str(loop))
            test = rotate(test, loop * -1)

        elif instruction[0] == 'x':
            instruction = instruction[1:].split('/')
            a = instruction[0]
            b = instruction[1]
            #print('Exchange ' + a + ' and ' + b)
            a = int(a)
            b = int(b)
            test[a], test[b] = test[b], test[a]

        elif instruction[0] == 'p':
            instruction = instruction[1:].split('/')
            a = instruction[0]
            b = instruction[1]
            #print('Partner ' + a + ' and ' + b)
            a = test.index(a)
            b = test.index(b)
            test[a], test[b] = test[b], test[a]

    return test


def second(instructions, string):
    seen = []
    for i in range(1000000000):
        s = ''.join(string)
        if s in seen:
            return seen[1000000000 % i - 1]
        seen.append(s)
        # print('Dance n°' + str(i))
        string = first(instructions, string)
    return string


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readline()

    test = False
    if test:
        instructions = instructions.split(',')
        string = ['a', 'b', 'c', 'd', 'e']
    else:
        instructions = content.split(',')
        string = list('abcdefghijklmnop')

    result1 = first(instructions, string)

    print("1. Le résultat est " + ''.join(result1))
    result1000000000 = second(instructions, result1)
    print("2. Le résultat est " + ''.join(result1000000000))
