import re

from python.download_input import get_input_content


def get_diff(numbers: list[int]) -> list[int]:
    i = 1
    diff = []
    while i < len(numbers):
        diff.append(numbers[i] - numbers[i - 1])
        i += 1
    return diff


def first(data):
    total = 0
    for line in data:
        numbers = list(map(int, re.findall(r'-?\d+', line)))
        diff_array = [numbers]
        while not all(n == 0 for n in diff_array[-1]):
            diff_array.append(get_diff(diff_array[-1]))

        diff_array[-1].append(0)

        i = len(diff_array) - 2
        while i >= 0:
            diff_array[i].append(diff_array[i][-1] + diff_array[i+1][-1])
            i -= 1

        total += diff_array[0][-1]

    return total


def second(data):
    total = 0
    for line in data:
        numbers = list(map(int, re.findall(r'-?\d+', line)))
        diff_array = [numbers]
        while not all(n == 0 for n in diff_array[-1]):
            diff_array.append(get_diff(diff_array[-1]))

        diff_array[-1].insert(0, 0)

        i = len(diff_array) - 2
        while i >= 0:
            diff_array[i].insert(0, diff_array[i][0] - diff_array[i+1][0])
            i -= 1

        total += diff_array[0][0]

    return total


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
