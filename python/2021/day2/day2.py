import re

from python.download_input import get_input_content


def first(data):
    horizontal = depth = 0
    for line in data:
        value = int(re.findall(r'\d', line)[0])
        if line.startswith('forward'):
            horizontal += value
        elif line.startswith('down'):
            depth += value
        elif line.startswith('up'):
            depth -= value
    return horizontal * depth


def second(data):
    horizontal = depth = aim = 0
    for line in data:
        value = int(re.findall(r'\d', line)[0])
        if line.startswith('forward'):
            horizontal += value
            depth += value * aim
        elif line.startswith('down'):
            aim += value
        elif line.startswith('up'):
            aim -= value
    return horizontal * depth


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
