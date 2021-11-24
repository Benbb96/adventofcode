from python.download_input import get_input_content


def first(data):

    for line in data:
        print(line)

    return 1


def second(data):
    return 2


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
