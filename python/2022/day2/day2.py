from python.download_input import get_input_content

draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

my_score = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def first(data):
    score = 0
    for line in data:
        x, y = line.split()
        if draw[x] == y:
            score += 3
        elif win[x] == y:
            score += 6
        else:
            score += 0

        score += my_score[y]

    return score


def second(data):
    score = 0
    for line in data:
        x, y = line.split()

        if y == 'X':
            z = lose[x]
            score += 0
        elif y == 'Y':
            z = draw[x]
            score += 3
        else:
            z = win[x]
            score += 6

        score += my_score[z]

    return score


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
