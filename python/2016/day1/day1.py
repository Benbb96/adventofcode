class Me:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'N'

    def move(self, instruction):
        # print(self.direction + ' - ' + instruction)
        turn = instruction[0]
        step = int(instruction[1])

        if turn == 'R':
            self.turnRight()
        else:
            self.turnLeft()

        if self.direction == 'N':
            self.y += step
        elif self.direction == 'S':
            self.y -= step
        elif self.direction == 'E':
            self.x += step
        else:
            self.x -= step

        # print('x=' + str(self.x) + ' ; y=' + str(self.y))

    def turnRight(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        else:
            self.direction = 'N'

    def turnLeft(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        else:
            self.direction = 'N'



def day1(inputContent):
    me = Me()
    instructions = inputContent.split(', ')
    for instruction in instructions:
        me.move(instruction)
    distance = abs(me.x) + abs(me.y)
    return distance


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        content = f.read()
    print('La distance parcouru est de ' + str(day1(content)))
