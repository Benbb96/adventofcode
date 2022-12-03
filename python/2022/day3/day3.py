from python.download_input import get_input_content


def first(data):
    score = 0
    for line in data:
        middle = int(len(line)/2)
        a = line[:middle]
        b = line[middle:]
        for c in a:
            if c in b:
                score += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(c) + 1
                break

    return score


def second(data):
    score = 0
    i = 2
    while i < len(data):
        common = set.intersection(*map(set, [data[i-2], data[i-1], data[i]]))
        for c in common:
            score += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(c) + 1
        i += 3

    return score


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
    # if test_input:
    #     content = test_input.split('\n')

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
