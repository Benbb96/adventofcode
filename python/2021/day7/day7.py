from statistics import median, mean
from sys import maxsize

from python.download_input import get_input_content


def first(data):
    positions = list(map(int, data[0].split(',')))

    m = int(median(positions))

    fuel = 0
    for pos in positions:
        fuel += abs(pos - m)

    return fuel


def second(data):
    positions = list(map(int, data[0].split(',')))

    m = int(mean(positions))
    best_fuel = maxsize
    range_to_try = 4
    for i in range(-range_to_try, range_to_try):
        middle = m + i
        fuel = 0
        for pos in positions:
            # Triangular Number
            delta = abs(pos - middle)
            fuel += int((delta * (delta + 1))/2)
        if fuel < best_fuel:
            best_fuel = fuel

    return best_fuel


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
