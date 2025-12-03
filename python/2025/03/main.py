from download_input import get_input_content


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
        sorted_numbers = sorted(numbers, reverse=True)
        max_12 = sorted_numbers[:12]
        print(max_12)
        indexes = set()
        corresponding_indexes = []
        for c in max_12:
            index = numbers.index(c)
            while index in indexes:
                index = numbers.index(c, index + 1)
            indexes.add(index)
            corresponding_indexes.append(index)
        print(corresponding_indexes)
        sorted_corresponding_indexes = sorted(corresponding_indexes)
        print(sorted_corresponding_indexes)
        found = int(''.join([str(numbers[i]) for i in sorted_corresponding_indexes]))
        print(found)
        sum += found
        print('----')

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
