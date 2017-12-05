def first(input):
    position = 0
    step = 0
    while position < len(input):
        currentPosition = int(input[position])
        oldPosition = position
        position += currentPosition
        currentPosition += 1
        input[oldPosition] = str(currentPosition)
        step += 1
    return step


# TODO Optimiser !
def second(input):
    position = 0
    step = 0
    while position < len(input):
        currentPosition = int(input[position])
        oldPosition = position
        position += currentPosition
        if currentPosition >= 3:
            currentPosition -= 1
        else:
            currentPosition += 1
        input[oldPosition] = str(currentPosition)
        step += 1
    return step


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    print("1. Le nombre d'étape pour terminer le labyrinthe de trampoline est de " + str(first(content)))

    with open('input.txt', 'r') as f:
        content2 = f.readlines()
    content2 = [x.strip() for x in content2]
    print("2. Le nombre d'étape pour terminer le labyrinthe de trampoline est de " + str(second(content2)))