import re
import math

from download_input import get_input_content


def first(data):
    numbers = []
    operations = []
    for line in data:
        found_numbers = [int(x) for x in re.findall(r'\d+', line)]
        if found_numbers:
            numbers.append(found_numbers)
        else:
            operations = [x for x in line if x in ('*', '+')]

    total = 0
    col = 0
    while col < len(numbers[0]):
        is_add = True if operations[col] == '+' else False
        row_total = 0 if is_add else 1
        for row in range(len(numbers)):
            if is_add:
                row_total += numbers[row][col]
            else:
                row_total *= numbers[row][col]
        total += row_total
        col += 1

    return total

def second(lines):
    col = len(lines[0]) - 2 # -2 to skip newline and avoid index error
    row = 0
    numbers = []
    column_numbers = []
    # Read columns from right to left
    while col >= 0:
        number = ''
        while row < len(lines) - 1:
            if lines[row][col] != ' ':
                number += lines[row][col]
            row += 1
        if (number):
            column_numbers.append(int(number))
        else:
            numbers.append(column_numbers)
            column_numbers = []
        col -= 1
        row = 0
    numbers.append(column_numbers) # Append last column

    operations = [x for x in reversed(lines[-1]) if x in ('*', '+')]

    total = 0
    for i, numbers in enumerate(numbers):
        col_total = sum(numbers) if operations[i] == '+' else math.prod(numbers)
        total += col_total
    return total


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''
    # if test_input:
    #     content = test_input.split('\n')

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
