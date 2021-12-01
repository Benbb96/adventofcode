from python.download_input import get_input_content


def first(data):
    increased = 0
    prev = None
    for line in data:
        if prev is not None and line > prev:
            increased += 1
        prev = line

    return increased


def second(data):
    increased = 0
    prev_prev = data[0]
    prev = data[1]
    prev_sum = None
    for line in data[2:]:
        current_sum = sum([prev_prev, prev, line])
        if prev_sum is not None and current_sum > prev_sum:
            increased += 1
        prev_sum = current_sum
        prev_prev = prev
        prev = line

    return increased


if __name__ == "__main__":
    content = list(map(int, get_input_content(__file__)))

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
