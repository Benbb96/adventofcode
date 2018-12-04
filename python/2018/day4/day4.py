import datetime
import re

matcher = "[{year:d}-{month:d}-{day:d} {hour:d}:{minute:d}]"
guards = {}


def first(input):
    actions = {}
    guard = 0
    asleep = 0
    for line in input:
        dt, action = line.split('] ')
        dt = datetime.datetime.strptime(dt[1:], '%Y-%m-%d %H:%M')
        if dt.date() in actions:
            actions[dt.date()][dt.time()] = action
        else:
            actions[dt.date()] = {dt.time(): action}

    for date, times in sorted(actions.items()):
        for time, action in sorted(times.items()):
            if action[0] == 'G':
                guard = re.search(r'\d+', action).group()
            elif action[0] == 'f':
                asleep = time.minute
            elif action[0] == 'w':
                if guard in guards:
                    if date in guards[guard]:
                        minutes = guards[guard][date]
                    else:
                        minutes = [0] * 60
                    minutes[asleep:time.minute] = [1] * (time.minute - asleep)
                    guards[guard][date] = minutes
                else:
                    minutes = [0] * 60
                    minutes[asleep:time.minute] = [1] * (time.minute - asleep)
                    guards[guard] = {date: minutes}

    max = 0
    best_guard = 0
    for guard, dates in guards.items():
        x = 0
        for minutes in dates.values():
            x += sum(minutes)
        if x > max:
            max = x
            best_guard = guard

    max = 0
    minute = 0
    for i in range(60):
        # print('Minute : ' + str(i))
        cpt = 0
        for minutes in guards[best_guard].values():
            if minutes[i] == 1:
                cpt += 1
        if cpt > max:
            max = cpt
            minute = i
        # print('Best :')
        # print(max)
        # print(minute)
        # print('-----')

    return int(best_guard) * int(minute)


def second():
    max = 0
    minute = 0
    best = 0
    for i in range(60):
        for guard, dates in guards.items():
            cpt = 0
            for minutes in dates.values():
                if minutes[i] == 1:
                    cpt += 1
            if cpt > max:
                max = cpt
                minute = i
                best = guard

    return int(best) * int(minute)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second())
