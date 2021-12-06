from collections import Counter, defaultdict

from python.download_input import get_input_content


class Fish:
    def __init__(self, timer=8):
        self.timer = timer

    def __str__(self):
        return f'Timer {self.timer}'

    def next_day(self):
        new = False
        if self.timer == 0:
            self.timer = 7
            new = True
        self.timer -= 1
        return new


def first(data):
    fishs = []
    for timer in data[0].split(','):
        fish = Fish(int(timer))
        fishs.append(fish)

    for day in range(80):
        new_fishs = []
        for fish in fishs:
            if fish.next_day():
                new_fishs.append(Fish())
        # Add new fishs
        fishs += new_fishs

    return len(fishs)


def second(data):
    # Use a dict to count how many fish there are at each timer
    counter = Counter(map(int, data[0].split(',')))

    for day in range(256):
        next_counter = defaultdict(int)
        for val, count in counter.items():
            if val == 0:
                next_counter[6] += count
                next_counter[8] += count
            else:
                next_counter[val-1] += count
        counter = next_counter

    return sum(counter.values())


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
