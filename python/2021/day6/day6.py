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
        print(fish)
        fishs.append(fish)

    for day in range(18):
        print(day+1)
        new_fishs = []
        for fish in fishs:
            if fish.next_day():
                new_fishs.append(Fish())
        # Add new fishs
        fishs += new_fishs
    return len(fishs)


def second(data):
    line = data[0]
    for day in range(256):
        print(day+1)
        count_new = 0
        new_line = ''
        for timer in map(int, line.split(',')):
            if timer == 0:
                new_line += '6,'
                count_new += 1
            else:
                new_line += f'{timer-1},'
        line = new_line[:-1]
        for _ in range(count_new):
            line += ',8'
    return len(line.split(','))


if __name__ == "__main__":
    content = get_input_content(__file__)
    test_input = '''3,4,3,1,2'''
    if test_input:
        content = test_input.split('\n')

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
