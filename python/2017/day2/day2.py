#! /usr/bin/env python3
# coding: utf-8
import sys


def first(input_content):
    checksum = 0
    for line in input_content:
        line = line.split('\t')
        minimum = int(sys.maxsize)
        maximum = 0
        for digit in line:
            digit = int(digit)
            if digit > maximum:
                maximum = digit
            if digit < minimum:
                minimum = digit
        checksum += maximum - minimum
    print('Le premier checksum est : ' + str(checksum))


def second(input_content):
    checksum = 0
    for line in input_content:
        line = line.split('\t')
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
    print('Le second checksum est : ' + str(int(checksum)))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    first(content)
    second(content)
