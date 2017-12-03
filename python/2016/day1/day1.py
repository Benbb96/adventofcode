class Me:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'N'
        self.historic = [(0, 0)]
        self.firstTwiceVisitedPosition = (0, 0)

    def move(self, instruction):
        # print(self.direction + ' - ' + instruction)
        turn = instruction[0]  # Le premier caractère est le sens dans lequel on se tourne
        steps = int(instruction[1:])  # Les caractères suivants sont le nombre de pas à faire

        if turn == 'R':
            self.turn_right()
        else:
            self.turn_left()
        for step in range(steps):
            if self.direction == 'N':
                self.y += 1
            elif self.direction == 'S':
                self.y -= 1
            elif self.direction == 'E':
                self.x += 1
            else:
                self.x -= 1
            position = (self.x, self.y)
            if self.historic.__contains__(position) and self.firstTwiceVisitedPosition == (0, 0):
                self.firstTwiceVisitedPosition = position
            self.historic.append(position)

        # print('x=' + str(self.x) + ' ; y=' + str(self.y) + '\n')

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        else:
            self.direction = 'N'

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        else:
            self.direction = 'N'


def day1(input_content):
    me = Me()
    instructions = input_content.split(', ')
    for instruction in instructions:
        me.move(instruction)
    distance = get_distance((me.x, me.y))
    return distance, me.firstTwiceVisitedPosition


def get_distance(pos):
    return abs(pos[0]) + abs(pos[1])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        content = f.read()
    # distance, position = day1('R8, R4, R4, R8')
    distance, position = day1(content)
    distanceFirstPosition = get_distance(position)
    print('La distance parcouru est de ' + str(distance))
    print('La première position visitée deux fois est ' + str(position) + ', soit à ' + str(distanceFirstPosition))
