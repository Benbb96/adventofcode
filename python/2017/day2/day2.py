import sys


def first(input_content, sep):
    checksum = 0
    for line in input_content:
        line = line.split(sep)
        minimum = int(sys.maxsize)
        maximum = 0
        for digit in line:
            digit = int(digit)
            if digit > maximum:
                maximum = digit
            if digit < minimum:
                minimum = digit
        checksum += maximum - minimum
    return checksum


def second(input_content, sep):
    checksum = 0
    for line in input_content:
        line = line.split(sep)
        for i, digit in enumerate(line):
            count = i+1
            digit = int(digit)
            while count < len(line):
                next = int(line[count])
                if digit > next:
                    if digit % next == 0:
                        checksum += digit / next
                        break
                else:
                    if next % digit == 0:
                        checksum += next / digit
                        break
                count += 1
    return int(checksum)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    print('Le premier checksum est : ' + str(first(content, '\t')))
    print('Le second checksum est : ' + str(second(content, '\t')))
