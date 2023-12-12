import re

from python.download_input import get_input_content


def how_many_ways(duration: int, record: int) -> int:
    holding_time = 1
    start = 0
    while holding_time < duration:
        if (duration - holding_time) * holding_time > record:
            start = holding_time
            break
        holding_time += 1

    holding_time = duration - 1
    end = 0
    while holding_time > 0:
        if (duration - holding_time) * holding_time > record:
            end = holding_time
            break
        holding_time -= 1

    return end - start + 1


def first(data):
    times = list(map(int, re.findall(r'\d+', data[0])))
    distances = list(map(int, re.findall(r'\d+', data[1])))

    i = 0
    total = 1
    while i < len(times):
        total *= how_many_ways(times[i], distances[i])
        i += 1

    return total


def second(data):
    time = int(re.match(r'Time:(\d+)', data[0].replace(' ', '')).group(1))
    distance = int(re.match(r'Distance:(\d+)', data[1].replace(' ', '')).group(1))
    return how_many_ways(time, distance)


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
