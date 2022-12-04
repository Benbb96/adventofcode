from python.download_input import get_input_content


def first(data):
    s = 0
    for line in data:
        print(line)
        r1, r2 = line.split(',')
        mi1, ma1 = map(int, r1.split('-'))
        mi2, ma2 = map(int, r2.split('-'))
        if mi1 >= mi2 and ma1 <= ma2 or mi1 <= mi2 and ma1 >= ma2:
            print('contained')
            s += 1

    return s


def second(data):
    s = 0
    for line in data:
        print(line)
        r1, r2 = line.split(',')
        mi1, ma1 = map(int, r1.split('-'))
        mi2, ma2 = map(int, r2.split('-'))
        if mi1 >= mi2 and ma1 <= ma2 or mi1 <= mi2 and ma1 >= ma2:
            print('contained')
            s += 1
        elif mi2 <= mi1 <= ma2:
            s += 1
        elif mi2 <= ma1 <= ma2:
            s += 1
        elif mi1 <= mi2 <= ma1:
            s += 1
        elif mi1 <= ma2 <= ma1:
            s += 1

    return s


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
    # if test_input:
    #     content = test_input.split('\n')

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
