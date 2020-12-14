import re


def first(input):
    mem = {}
    mask = None

    for line in input:
        command, value = line.split(' = ')
        if '[' in command:
            memory_index = int(re.search('\[(\d+)\]', command).group(1))
            value = list("{0:036b}".format(int(value)))
            for i, b in enumerate(mask):
                if b != 'X':
                    value[i] = b
            mem[memory_index] = int(''.join(value), 2)
        else:
            mask = value
    return sum(mem.values())


def second(input):
    mem = {}
    mask = None

    for line in input:
        command, value = line.split(' = ')
        if '[' in command:
            memory_index = int(re.search('\[(\d+)\]', command).group(1))
            memory_value = list("{0:036b}".format(int(memory_index)))
            for i, b in enumerate(mask):
                if b != '0':
                    memory_value[i] = b
            memory_to_add = ['']
            for b in memory_value:
                if b != 'X':
                    memory_to_add = [address + b for address in memory_to_add]
                else:
                    new_memory_to_add = []
                    for address in memory_to_add:
                        new_memory_to_add.append(address + '0')
                        new_memory_to_add.append(address + '1')
                    memory_to_add = new_memory_to_add
            for memory_address in memory_to_add:
                mem[int(''.join(memory_address), 2)] = int(value)
        else:
            mask = value
    return sum(mem.values())


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
