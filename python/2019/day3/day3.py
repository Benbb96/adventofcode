

def first(input):
    paths = []
    intersections = []
    for line in input:
        print(line)
        x = 0
        y = 0
        path = {(x, y)}
        instructions = line.split(',')
        for instruction in instructions:
            print(instruction)
            direction = instruction[0]
            number = int(instruction[1:])

            for _ in range(number):
                if direction == 'R':
                    x += 1
                elif direction == 'L':
                    x -= 1
                elif direction == 'U':
                    y -= 1
                elif direction == 'D':
                    y += 1

                path.add((x, y))

                for line_path in path:
                    if (x, y) in line_path:
                        intersections.append((x, y))
        paths.append(path)
    print(intersections)

    return 1


def second(input):
    # Process
    return 2


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
