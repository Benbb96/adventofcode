from download_input import get_input_content


def first(data):
    position = 50
    count = 0
    for line in data:
        position += int(line[1:]) if line[0] == 'R' else -int(line[1:])
        position = position % 100
        if position == 0:
            count += 1

    return count


def second(data):
    position = 50
    count = 0
    for line in data:
        clicks = int(line[1:])
        while clicks > 0:
            position += 1 if line[0] == 'R' else -1
            position = position % 100
            if position == 0:
                count += 1
            clicks -= 1
        
    return count


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''
    if test_input:
        content = test_input.split('\n')

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
