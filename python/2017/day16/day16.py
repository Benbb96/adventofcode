s = 'abcdefghijklmnop'
instructions = 's1,x3/4,pe/b'

def rotate(strg,n):
    return strg[n:] + strg[:n]


def first(input):
    test = 'abcde'
    for instruction in input:
        if instruction[0] == 's':
            loop = int(instruction[1])
            print('Spin ' + str(loop))
            test = rotate(test, loop * -1)

        elif instruction[0] == 'x':
            instruction = instruction[1:].split('/')
            a = instruction[0]
            b = instruction[1]
            print('Exchange ' + a + ' and ' + b)
            test[a], test[b] = test[b], test[a]

        elif instruction[0] == 'p':
            instruction = instruction[1:].split('/')
            a = instruction[0]
            b = instruction[1]
            print('Partner ' + a + ' and ' + b)
            a = test.find(a)
            b = test.find(b)
            test[a], test[b] = test[b], test[a]

    return test


def second(input):
    # Process
    return 2


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readline()
    content = content.split(',')

    instructions.split(',')
    print("1. Le résultat est " + str(first(instructions)))

    #print("2. Le résultat est " + str(second(content)))
