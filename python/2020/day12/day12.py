

def first(input):
    direction = 'E'
    x = y = 0
    right_cycle = ['N', 'E', 'S', 'W']
    left_cycle = ['N', 'W', 'S', 'E']

    for line in input:
        action = line[0]
        value = int(line[1:])

        if action == 'F':
            action = direction

        if action == 'N':
            y -= value
        elif action == 'S':
            y += value
        elif action == 'W':
            x -= value
        elif action == 'E':
            x += value
        else:
            # Rotation
            quarter = value // 90
            if action == 'R':
                current_index = right_cycle.index(direction)
                new_index = (current_index + quarter) % 4
                direction = right_cycle[new_index]
            elif action == 'L':
                current_index = left_cycle.index(direction)
                new_index = (current_index + quarter) % 4
                direction = left_cycle[new_index]

    return abs(x) + abs(y)


def second(input):
    boat = (0, 0)
    waypoint = (10, -1)

    for line in input:
        action = line[0]
        value = int(line[1:])

        if action == 'F':
            boat = (boat[0] + waypoint[0] * value, boat[1] + waypoint[1] * value)
        elif action == 'N':
            waypoint = (waypoint[0], waypoint[1] - value)
        elif action == 'S':
            waypoint = (waypoint[0], waypoint[1] + value)
        elif action == 'W':
            waypoint = (waypoint[0] - value, waypoint[1])
        elif action == 'E':
            waypoint = (waypoint[0] + value, waypoint[1])
        else:
            # Rotation
            quarter = value // 90
            for _ in range(quarter):
                if action == 'R':
                    waypoint = (-waypoint[1], waypoint[0])
                elif action == 'L':
                    waypoint = (waypoint[1], -waypoint[0])

    return abs(boat[0]) + abs(boat[1])


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
