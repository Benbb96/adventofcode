def is_valid(number):
    prev = None
    adjacent = False
    for digit in str(number):
        digit = int(digit)
        if prev is not None and digit < prev:
            return False
        if digit == prev:
            adjacent = True
        prev = digit
    return adjacent


def first(data):
    count = 0
    start, stop = map(int, data.split('-'))
    for number in range(start, stop + 1):
        if is_valid(number):
            count += 1
    return count


def is_valid_2(number):
    prev = None
    for digit in str(number):
        digit = int(digit)
        if prev is not None and digit < prev:
            return False
        prev = digit

    # Check if one digit appears only twice
    for digit in range(number // 100000, 10):
        if str(number).count(str(digit)) == 2:
            return True
    return False


def second(data):
    count = 0
    start, stop = map(int, data.split('-'))
    for number in range(start, stop + 1):
        if is_valid_2(number):
            count += 1
    return count


if __name__ == "__main__":
    content = '206938-679128'

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
