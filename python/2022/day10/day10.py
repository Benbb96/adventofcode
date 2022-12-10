from python.download_input import get_input_content


def check_cycle(tick, x, signal_strengths):
    if (tick % 40) + 20 == 40:
        signal_strengths.append(tick * x)
    return signal_strengths


def first(data):
    tick = 1
    x = 1
    signal_strengths = []
    for line in data:
        signal_strengths = check_cycle(tick, x, signal_strengths)
        tick += 1

        if line.startswith('addx'):
            value = int(line.split()[1])
            signal_strengths = check_cycle(tick, x, signal_strengths)
            tick += 1
            x += value

    return sum(signal_strengths)


def get_sprite_position(x):
    sprite = ''
    for i in range(40):
        sprite += '#' if i in (x-1, x, x + 1) else '.'
    return sprite


def increment_tick(tick, row):
    tick += 1
    if tick % 40 == 0:
        tick = 0
        row += 1
    return tick, row


def second(data):
    tick = 0
    x = 1
    screen = [''] * 6
    row = 0
    for line in data:
        screen[row] += get_sprite_position(x)[tick]

        tick, row = increment_tick(tick, row)

        if line.startswith('addx'):
            value = int(line.split()[1])
            screen[row] += get_sprite_position(x)[tick]
            x += value

            tick, row = increment_tick(tick, row)

    return '\n'.join(screen)


if __name__ == "__main__":
    content = get_input_content(__file__)

    print(f'Le résultat de la première partie est :\n{first(content)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
