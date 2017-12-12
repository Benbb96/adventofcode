
class Spiral:

    def __init__(self, x, y, value, parent=None):
        self.x = x
        self.y = y
        self.value = value
        self.prev = parent

    def __str__(self):
        return 'x = ' + str(self.x) + '\t y = ' + str(self.y) + '\t value = ' + str(self.value)


def day3(n):
    x = y = 0
    initial = Spiral(x, y, 1)  # Première case exemple
    last = initial
    direction = 'E'
    moveX = 0
    moveY = 0
    widthLimit = 1
    heightLimit = 1
    for i in range(2, n + 1):  #On va créer toute sles cases jusqu'à celle ciblée

        if direction == 'E':
            y += 1
            moveY += 1
        elif direction == 'N':
            x -= 1
            moveX += 1
        elif direction == 'W':
            y -= 1
            moveY += 1
        elif direction == 'S':
            x += 1
            moveX += 1

        if moveY == widthLimit:
            widthLimit += 1
            moveY = 0
            if direction == 'E':
                direction = 'N'
            elif direction == 'W':
                direction = 'S'

        if moveX == heightLimit:
            heightLimit += 1
            moveX = 0
            if direction == 'N':
                direction = 'W'
            elif direction == 'S':
                direction = 'E'
        
        new = Spiral(x, y, i, last)
        last.next = new
        last = new

    # Enfin, on retourne la distance de la case par rapport à l'origine
    return abs(last.x) + abs(last.y)


if __name__ == "__main__":
    n = 289326
    print('La distance à laquelle se trouve la case ' + str(n) + ' est de ' + str(day3(n)))
    # La partie 2 s'est faite facilement grâce à OEIS : https://oeis.org/A141481
