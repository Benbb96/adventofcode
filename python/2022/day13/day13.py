from functools import cmp_to_key

from python.download_input import get_input_content


def compare(left: str, rigth: str) -> int:
    left = eval(left)
    rigth = eval(rigth)

    # Fix type mismatch
    if type(left) != type(rigth):
        if type(left) == int:
            left = [left]
        elif type(rigth) == int:
            rigth = [rigth]

    if type(left) == int:
        return left - rigth

    # Compare two lists
    i = 0
    while i < max(len(left), len(rigth)):
        try:
            left_value = left[i]
        except IndexError:
            # If the left list runs out of items first, the inputs are in the right order
            return -1
        try:
            rigth_value = rigth[i]
        except IndexError:
            # If the right list runs out of items first, the inputs are not in the right order
            return 1
        result = compare(str(left_value), str(rigth_value))
        if result != 0:
            return result
        i += 1
    return 0


def first(data):
    data = data.split('\n\n')
    right_orders = []

    for i, line in enumerate(data):
        left, rigth = line.split('\n')
        result = compare(left, rigth)
        if result < 0:
            right_orders.append(i+1)

    return sum(right_orders)


def second(data):
    # Remove blank lines
    data = data.replace('\n\n', '\n')
    # Add two packets
    data = '[[2]]\n[[6]]\n' + data
    # Split by line
    data = data.split('\n')
    # Sort with custom comparison
    data.sort(key=cmp_to_key(compare))

    return (data.index('[[2]]') + 1) * (data.index('[[6]]') + 1)


if __name__ == "__main__":
    content = get_input_content(__file__, split_by_lines=False)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
