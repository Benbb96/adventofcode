from python.download_input import get_input_content


def first(data):
    m = 0
    t = 0
    for line in data:
        if line == '':
            m = max(t, m)
            t = 0
        else:
            t += int(line)

    return m


def second(data):
    m = []
    t = 0
    for line in data:
        if line == '':
            m.append(t)
            t = 0
        else:
            t += int(line)

    return sum(sorted(m, reverse=True)[:3])


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = ''''''
    if test_input:
        content = test_input.split('\n')

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
