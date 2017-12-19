test = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
                """


def first(lines):
    line = 0
    col = 0
    direction = 'S'
    path = ''
    end = False
    # Trouver le départ
    i = 0
    for c in lines[line]:
        if c == '|':
            col = i
        i += 1
    print(col)

    count = 1

    while not end:
        count += 1
        print('Position : [' + str(line) + '][' + str(col) + '] Direction : ' + direction)
        if direction == 'S':
            line += 1
        elif direction == 'N':
            line -= 1
        elif direction == 'E':
            col += 1
        elif direction == 'W':
            col -= 1

        char = lines[line][col]
        if char == '|' or char == '-':
            print('Keep going')
        elif char == '+':
            print('Change direction')
            if direction == 'N' or direction == 'S':
                testRight = lines[line][col+1]
                if testRight != ' ':
                    direction = 'E'
                else:
                    direction = 'W'
            else:
                testUp = lines[line-1][col]
                if testUp != ' ':
                    direction = 'N'
                else:
                    direction = 'S'
        else:
            print("C'est une lettre : " + char)
            path += char
            if direction == 'N' and lines[line-1][col] == ' ':
                end = True
            elif direction == 'S' and lines[line+1][col] == ' ':
                end = True
            elif direction == 'E' and lines[line][col+1] == ' ':
                end = True
            elif direction == 'W' and lines[line][col-1] == ' ':
                end = True

    return path, count


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()

    test = test.split('\n')

    path, count = first(content)

    print("1. Le chemin emprunté est " + path)
    print("2. Le résultat est " + str(count))
