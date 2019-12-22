memory = ORIGINAL_MEM = []


def handle_intcode():
    i = 0
    while i < len(memory):
        if memory[i] == 99:
            break
        intcode(memory[i], memory[i + 1], memory[i + 2], memory[i + 3])
        i += 4


def intcode(opcode, *args):
    if opcode == 1:
        # Add
        memory[args[2]] = memory[args[0]] + memory[args[1]]
    elif opcode == 2:
        # Multiply
        memory[args[2]] = memory[args[0]] * memory[args[1]]


def first():
    global memory
    memory = ORIGINAL_MEM.copy()
    memory[1] = 12
    memory[2] = 2
    handle_intcode()
    return memory[0]


def second():
    global memory
    for noun in range(100):
        for verb in range(100):
            memory = ORIGINAL_MEM.copy()
            memory[1] = noun
            memory[2] = verb
            handle_intcode()
            if memory[0] == 19690720:
                return 100 * noun + verb
    return '19690720 est introuvable.'


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readline().strip()
    ORIGINAL_MEM = [int(x) for x in content.split(',')]

    print("1. Le résultat est %s" % first())

    print("2. Le résultat est %s" % second())
