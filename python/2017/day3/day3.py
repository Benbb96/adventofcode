size = 5
matrix = [[0 for i in range(size)] for i in range(size)]


def fillMatrix():
    positionX = int(size/2)
    positionY = int(size / 2)
    count = 1
    width = 1
    height = 1

    while count <= 20:
        print('X=' + str(positionX) + ', Y= ' + str(positionY))
        for w in range(width):
            matrix[positionX][positionY] = count
            count += 1
            positionY += 1
        width += 1
        print('X=' + str(positionX) + ', Y= ' + str(positionY))
        for h in range(height):
            matrix[positionX][positionY] = count
            count += 1
            positionX -= 1
        height += 1
        print('X=' + str(positionX) + ', Y= ' + str(positionY))
        for w in range(width):
            matrix[positionX][positionY] = count
            count += 1
            positionY -= 1
        width += 1
        print('X=' + str(positionX) + ', Y= ' + str(positionY))
        for h in range(height):
            matrix[positionX][positionY] = count
            count += 1
            positionX += 1
        height += 1
        print('X=' + str(positionX) + ', Y= ' + str(positionY))


    # matrix[positionX][positionY] = count
    # count += 1
    # positionY += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionX -= 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY -= 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY -= 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionX += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionX += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionX -= 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionX -= 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionX -= 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY -= 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY -= 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY -= 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY -= 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionX += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionX += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionX += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionX += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY += 1
    #
    # matrix[positionX][positionY] = count
    # count += 1
    # positionY += 1
    #
    # matrix[positionX][positionY] = count


def displayMatrix():
    x = 0
    while x < size:
        y = 0
        while y < size:
            print(matrix[x][y], end='\t')
            y += 1
        print()
        x += 1


def day3(input):
    pass
    # print(input)


if __name__ == "__main__":
    fillMatrix()
    displayMatrix()
    day3(1)