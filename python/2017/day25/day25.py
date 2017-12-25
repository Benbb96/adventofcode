states = {}
state = '.'
checksum = 0
tape = {}


def parseFile(content):
    global states, state, checksum
    content = content.split('\n\n')
    state = content[0][15]
    checksum = int(content[0].split()[9])

    for s in content[1:]:
        part = s.split(':')
        instructionsZero = part[2].split('-')
        ifZero = {}
        ifZero['nextValue'] = instructionsZero[1][17]
        ifZero['move'] = 'right' if instructionsZero[2][22] == 'r' else 'left'
        ifZero['nextState'] = instructionsZero[3][21]

        instructionsOne = part[3].split('-')
        ifOne = {}
        ifOne['nextValue'] = instructionsOne[1][17]
        ifOne['move'] = 'right' if instructionsOne[2][22] == 'r' else 'left'
        ifOne['nextState'] = instructionsOne[3][21]

        states[s[9]] = {'0': ifZero, '1': ifOne}

def day25(checksum, state, states, tape):
    cursor = 0
    print(states)
    for step in range(checksum):
        # On initialise à 0 s'il n'existe pas actuellement dans la bande
        if str(cursor) not in tape.keys():
            tape[str(cursor)] = '0'
        print('Step ' + str(step))
        # print("State : " + state)
        # print('Cursor = ' + str(cursor))
        # print('Value = ' + tape[str(cursor)])
        # print(tape)
        last = cursor
        cursor = cursor - 1 if states[state][tape[str(cursor)]]['move'] == 'left' else cursor + 1
        lastState = state
        state = states[state][tape[str(last)]]['nextState']
        tape[str(last)] = states[lastState][tape[str(last)]]['nextValue']

    total = 0
    for val in tape.values():
        if val == '1':
            total += 1

    return total


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.read()

    parseFile(content)

    print("Le résultat est " + str(day25(checksum, state, states, tape)))
