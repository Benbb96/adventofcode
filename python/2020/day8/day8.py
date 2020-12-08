

def first(input):
    acc = 0
    i = 0
    executed_lines = []
    while i not in executed_lines:
        current_line = input[i]
        executed_lines.append(i)
        value = int(current_line[4:])
        if current_line[:3] == 'jmp':
            i += value
        else:
            if current_line[:3] == 'acc':
                acc += value
            i += 1
    return acc


def second(input):
    for index, line in reversed(list(enumerate(input))):
        # Create a copy of the input list in order to change only one operation, starting by the end
        input_copy = input.copy()
        if line[:3] == 'jmp':
            input_copy[index] = input[index].replace('jmp', 'nop')
        elif line[:3] == 'nop':
            input_copy[index] = input[index].replace('nop', 'jmp')
        # Run the progam to find if it eventually got to the end (with an IndexError)
        acc = 0
        i = 0
        executed_lines = []
        while i not in executed_lines:
            try:
                current_line = input_copy[i]
            except IndexError:
                return acc
            executed_lines.append(i)
            value = int(current_line[4:])
            if current_line[:3] == 'jmp':
                i += value
            else:
                if current_line[:3] == 'acc':
                    acc += value
                i += 1


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
