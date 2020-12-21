

def first(input):
    # Init 3D map
    x = y = z = 0
    cubes = {}
    for line in input:
        y = 0
        for c in line:
            cubes[(x, y, z)] = True if c == '#' else False
            y += 1
        x += 1
    print(f'{cubes=}')

    target_cycle = 6
    for cycle in range(target_cycle):
        print(f'{cycle + 1=}')
        old_state = cubes.copy()
        futur_state = cubes.copy()
        for cube, state in cubes.items():
            count_active_neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        if i == 0 and j == 0 and i == 0:
                            pass
                        target_cube = (cube[0] + i, cube[1] + j, cube[2] + k)
                        if not target_cube in old_state.keys():
                            futur_state[target_cube] = False
                            old_state[target_cube] = False
                        elif old_state[target_cube]:
                            count_active_neighbors += 1
            if state:
                if count_active_neighbors < 2 or count_active_neighbors > 3:
                    futur_state[cube] = False
            elif count_active_neighbors == 3:
                    futur_state[cube] = True
        cubes = futur_state
        print(cubes)
        print(sum(1 if state else 0 for state in cubes.values()))

    return sum(1 if state else 0 for state in cubes.values())


def second(input):
    # Process
    return 2


if __name__ == "__main__":
    with open('test.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. Le résultat est %s" % first(content))

    print("2. Le résultat est %s" % second(content))
