from python.download_input import get_input_content


def first(data):
    i = 4
    while i < len(data):
        if len(set(data[i-4:i])) == 4:
            print(data[i-4:i])
            return i
        i+=1


def second(data):
    i = 14
    while i < len(data):
        if len(set(data[i - 14:i])) == 14:
            print(data[i - 14:i])
            return i
        i += 1


if __name__ == "__main__":
    content = get_input_content(__file__, split_by_lines=False)
    test_input = '''nppdvjthqldpwncqszvftbrmjlhg'''
    # if test_input:
    #     content = test_input

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
