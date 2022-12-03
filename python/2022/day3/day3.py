from python.download_input import get_input_content


def prioritize(c: str):
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(c) + 1


def first(data):
    score = 0
    for line in data:
        a = line[:len(line)//2]
        b = line[len(line)//2:]
        for c in a:
            if c in b:
                score += prioritize(c)
                break

    return score


def second(data):
    score = 0
    i = 2
    while i < len(data):
        common = set(data[i-2]) & set(data[i-1]) & set(data[i])
        score += prioritize(list(common)[0])
        i += 3

    return score


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
