from download_input import get_input_content
from collections import deque


def first(data):
    sum = 0
    for line in data:
        print(line)
        numbers = [int(c) for c in line]

        max_char = max(numbers)
        if line.count(str(max_char)) > 1:
            sum += int(f'{max_char}{max_char}')
        else:
            index_of_max = numbers.index(max_char)
            if index_of_max == len(line) - 1:
                found = int(f'{max(numbers[:index_of_max])}{max_char}')
            else:
                found = int(f'{max_char}{max(numbers[index_of_max + 1:])}')
            sum += found

    return sum


def second(data):
     sum = 0
     for line in data:
        print(line)
        numbers = [int(c) for c in line]
        copy_numbers = numbers.copy()

        # init
        found_indexes = []
        last_max_char = None
        last_index = None
        while len(found_indexes) < 12:
            print(f'{copy_numbers=}')
            max_char = max(copy_numbers)
            print(f'{max_char=}')
            if last_max_char == max_char:
                start = last_index + 1
            else:
                start = 0
            print(f'{start=}')
            last_max_char = max_char
            last_index = numbers.index(max_char, start)
            found_indexes.append(last_index)
            del copy_numbers[copy_numbers.index(max_char)]

        # sort
        found_indexes.sort()
        found = ''.join(str(numbers[i]) for i in found_indexes)
        print(found)
        print()
        sum += int(found)

     return sum


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''987654321111111
811111111111119
234234234234278
818181911112111'''
    if test_input:
        content = test_input.split('\n')

    # print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
