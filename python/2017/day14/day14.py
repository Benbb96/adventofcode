import sys

size = 256  # La taille de la liste


def knot_hash(input):
    input = prepare(input)
    l = list(range(size))
    i = 0  # Current position
    skip_size = 0
    # On va répéter l'opération 64 fois
    for _ in list(range(64)):
        for length in input:
            length = int(length)
            if length > 1:
                if i + length < size:
                    sublist = l[i:(i + length)]
                else:
                    j = i
                    count = 0
                    sublist = []
                    while count < length:
                        sublist.append(l[j % size])
                        j += 1
                        count += 1
                sublist = list(reversed(sublist))
                j = i
                count = 0
                while count < length:
                    l[j % size] = sublist[count]
                    j += 1
                    count += 1
            i = (i + length + skip_size) % size
            skip_size += 1


    # Hachage terminé, on récupère les 256 valeurs et on les regroupe en 16 valeurs hexadécimal
    result = ''
    i = 0
    for _ in range(16):
        group = l[i:(i + 16)]
        regrouped = xor(group)
        result += '{:02x}'.format(regrouped)
        i += 16
    return result


def prepare(input):
    """
    Prépare l'input en passant tous les caractères en nombre ascii
    puis en ajoutant à la liste les valeurs 17, 31, 73, 47, 23
    """
    ascii_codes = []
    for c in input:
        ascii_codes.append(ord(c))
    for add in [17, 31, 73, 47, 23]:
        ascii_codes.append(add)
    return ascii_codes


def xor(n):
    """
    Regroupe les 16 valeurs en une grâce à l'opération binaire XOR ( ^ )
    """
    return n[0] ^ n[1] ^ n[2] ^ n[3] ^ n[4] ^ n[5] ^ n[6] ^ n[7] ^ n[8] ^ n[9] ^ n[10] ^ n[11] ^ n[12] ^ n[13] ^ n[14] ^ n[15]


def hex_to_bin(hex):
    return format(int(hex, 16), '0128b')


def display_grid(grid):
    for i in range(128):
        for j in range(128):
            if grid[i][j] == '1':
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')


def search_neighboors(i, j, grid, processed):
    # Check the neighboors in the four direction
    # Ignore the one we already saw
    if i > 0 and (i-1) * 128 + j not in processed and grid[i-1][j] == '1':
        processed.append((i-1) * 128 + j)
        search_neighboors(i-1, j, grid, processed)
    if j > 0 and (i) * 128 + j - 1 not in processed and grid[i][j-1] == '1':
        processed.append((i) * 128 + j-1)
        search_neighboors(i, j-1, grid, processed)
    if i < 128-1 and (i+1) * 128 + j not in processed and grid[i+1][j] == '1':
        processed.append((i+1) * 128 + j)
        search_neighboors(i+1, j, grid, processed)
    if j < 128-1 and (i) * 128 + j + 1 not in processed and grid[i][j+1] == '1':
        processed.append((i) * 128 + j+1)
        search_neighboors(i, j+1, grid, processed)


def day14(input):
    # Part 1
    grid = []
    total = 0
    for process in range(128):
        row = hex_to_bin(knot_hash(input + '-' + str(process)))
        total += row.count('1')
        grid.append(list(row))

    display_grid(grid)

    # Part 2
    processed = []
    i = 0
    region = 0
    while i < 128:
        j = 0
        while j < 128:
            if i * 128 + j not in processed and grid[i][j] == '1':
                processed.append(i * 128 + j)
                region += 1
                search_neighboors(i, j, grid, processed)
            j += 1
        i += 1

    return total, region


if __name__ == "__main__":
    input = 'amgozmfv'
    test = 'flqrgnkx'
    total, region = day14(input)

    print("1. Le nombre de carrés utilisés est " + str(total))

    print("2. Le nombre de régions  est " + str(region))
