from collections import deque

class Program:
    def __init__(self):
        self.registers = {}
        self.pos = 0
        self.queue = deque([])
        self.wait = False
        self.count = 0

    def process(self, instruction):
        cmd = instruction.split()[0]
        reg = instruction.split()[1]
        x = self.get_register_or_value(reg)
        try:
            y = self.get_register_or_value(instruction.split()[2])
        except IndexError:
            # S'il n'y a pas de 2ème paramètre
            pass

        if cmd == 'jgz':
            self.jump(x, y)
        else:
            if cmd == 'snd':
                self.send(x)
            elif cmd == 'rcv':
                self.receive(reg)
            elif cmd == 'set':
                self.set_register(reg, y)
            elif cmd == 'add':
                self.calculate(reg, x, '+', y)
            elif cmd == 'mul':
                self.calculate(reg, x, '*', y)
            elif cmd == 'mod':
                self.calculate(reg, x, '%', y)
            # On passe à l'instruction suivante si on est pas en attente
            if not self.wait:
                self.pos += 1

    def get_register_or_value(self, x):
        try:
            n = int(x)
        except ValueError:
            # S'il s'agit d'un register
            try:
                n = int(self.registers[x])
            except KeyError:
                # Si le register n'a pas encore été appelé
                self.registers[x] = 0  # Il ne faut pas oublier d'assigner 0 au register... Au moins 30 min de debug :(
                n = 0
        return n

    def send(self, value):
        self.friend.queue.append(value)
        self.friend.wait = False
        self.count += 1

    def receive(self, reg):
        if len(self.queue) > 0:
            self.registers[reg] = self.queue.popleft()
        else:
            self.wait = True

    def set_register(self, reg, value):
        self.registers[reg] = value

    def calculate(self, reg, x, operation,  y):
        if operation == '+':
            result = x + y
        elif operation == '*':
            result = x * y
        else:
            result = x % y
        self.registers[reg] = str(result)

    def jump(self, reg, value):
        if reg > 0:
            self.pos += value
        else:
            self.pos += 1


def first(input):
    sound = None
    registers = {}
    pos = 0
    total_instructions = len(input)
    while pos < total_instructions:
        line = input[pos]
        instruction = line.split()[0]
        # print(str(pos) + ' : ' + line)
        reg = line.split()[1]

        # Calcul de X
        try:
            x = int(registers[reg])
        except KeyError:
            x = 0

        # Calcul de Y
        try:
            y = int(line.split()[2])
        except ValueError:
            # S'il s'agit d'un register
            y = int(registers[line.split()[2]])
        except IndexError:
            # Dans le cas d'une instruction sans valeur y
            y = None

        if instruction == 'snd':
            sound = x
        elif instruction == 'rcv':
            if x != 0:
                return sound
        elif instruction == 'set':
            registers[reg] = str(y)
        elif instruction == 'add':
            new = x + y
            registers[reg] = str(new)
        elif instruction == 'mul':
            new = x * y
            registers[reg] = str(new)
        elif instruction == 'mod':
            new = x % y
            registers[reg] = str(new)
        elif instruction == 'jgz':
            if x > 0:
                pos += y
                continue  # On incrémente pas le nombre ligne
        pos += 1  # On passe à l'instruction suivante


def second(input):
    test = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv b""".split('\n')
    programA = Program()
    programB = Program()
    programA.friend = programB
    programB.friend = programA
    programA.registers['p'] = 0
    programB.registers['p'] = 1

    deadlock = False
    while not deadlock:
        lineA = input[programA.pos]
        lineB = input[programB.pos]
        # print('A : ' + lineA + ' || ' + str(programA.pos))
        # print('B : ' + lineB + ' || ' + str(programB.pos))
        # print('-----------------')
        programA.process(lineA)
        programB.process(lineB)
        if programA.wait and programB.wait:
            deadlock = True
    return programB.count


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    print("1. La première fréquence émise est " + str(first(content)))

    print("2. Le nombre de fois qu'émet le programme B est " + str(second(content)))
