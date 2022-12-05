import re
from copy import deepcopy

from python.download_input import get_input_content


def first(my_stacks, instructions):
    for line in instructions.split('\n'):
        n, from_pos, to_pos = map(int, re.findall(r' \d* ?', line))
        for _ in range(n):
            x = my_stacks[from_pos-1].pop()
            my_stacks[to_pos-1].append(x)

    return ''.join(s[-1] for s in my_stacks)


def second(my_stacks, instructions):
    for line in instructions.split('\n'):
        n, from_pos, to_pos = map(int, re.findall(r' \d* ?', line))
        to_move = list()
        for _ in range(n):
            to_move.append(my_stacks[from_pos - 1].pop())
        for x in reversed(to_move):
            my_stacks[to_pos - 1].append(x)

    return ''.join(s[-1] for s in my_stacks)


if __name__ == "__main__":
    stack_lines, instructions = get_input_content(__file__, split_by_lines=False).split('\n\n')
    test_input = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

    # if test_input:
    #     stack_lines, instructions = test_input.split('\n\n')

    stacks_number = int(stack_lines.split('\n')[-1][-2])

    stacks = None
    for line in reversed(stack_lines.split('\n')):
        if not stacks:
            stacks = [list() for _ in range(stacks_number)]
        else:
            for i in range(stacks_number):
                if line[i*4+1] != ' ':
                    stacks[i].append(line[i*4+1])

    print(f'Le résultat de la première partie est :\n{first(deepcopy(stacks), instructions)}')

    print(f'Le résultat de la deuxième partie est :\n{second(deepcopy(stacks), instructions)}')
