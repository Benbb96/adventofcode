def get_sum_of_numbers(numbers):
    i = 0
    sum_numbers = []
    length = len(numbers)
    while i < length:
        j = i + 1
        while j < length:
            sum_numbers.append(int(numbers[i]) + int(numbers[j]))
            j += 1
        i += 1
    return sum_numbers


def first(input):
    preamble = 25
    previous_numbers = []
    for index, line in enumerate(input):
        number = int(line)
        if index < preamble:
            previous_numbers.append(number)
        else:
            if number not in get_sum_of_numbers(previous_numbers):
                return number
            # Remove first and add current number
            previous_numbers.pop(0)
            previous_numbers.append(number)


def second(input, result_1):
    used_numbers = []
    for line in input:
        number = int(line)
        used_numbers.append(number)
        sum_used_numbers = sum(used_numbers)
        if sum_used_numbers == result_1:
            return min(used_numbers) + max(used_numbers)
        if sum_used_numbers > result_1:
            while sum_used_numbers > result_1:
                used_numbers.pop(0)
                sum_used_numbers = sum(used_numbers)
                if sum_used_numbers == result_1:
                    return min(used_numbers) + max(used_numbers)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    result_1 = first(content)
    print("1. Le résultat est %s" % result_1)

    print("2. Le résultat est %s" % second(content, result_1))
