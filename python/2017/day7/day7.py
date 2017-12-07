class Program:

    def __init__(self, name, weight, support):
        self.name = name
        weight = weight.replace('(', '').replace(')', '')  # On retire les parenthèses
        self.weight = int(weight)
        self.weightPlusChildren = self.weight
        self.support = support
        self.parent = None
        self.children = None

    def __str__(self):
        return self.name

    def display(self, level=0):
        txt = ' - ' * level + self.name + ' (' + str(self.weight) + ' - ' + str(self.weightPlusChildren) + ')'
        if not self.isBalanced():
            txt = txt + ' !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        print(txt)
        if self.isSupporting():
            for child in self.children:
                child.display(level + 1)

    def isSupporting(self):
        if not self.support:
            return False
        return True

    def calculateWeight(self):
        if self.children is None:
            return self.weight
        sum = self.weight
        for child in self.children:
            sum += child.calculateWeight()
        self.weightPlusChildren = sum
        return sum

    def isBalanced(self):
        if not self.isSupporting():
            return True
        weight = self.children[0].weightPlusChildren
        for child in self.children:
            if child.weightPlusChildren != weight:
                last = self
                return False
        return True

    def findNotBalanced(self, notBalanced):
        if self.isBalanced():
            return []
        else:
            notBalanced.append(self)
            for child in self.children:
                child.findNotBalanced(notBalanced)


def parseLine(line):
    if '-> ' in line:
        line = line.split('-> ')
        name = line[0].split()[0]
        weight = line[0].split()[1]
        support = line[1].split(', ')
    else:
        name = line.split()[0]
        weight = line.split()[1]
        support = []
    program = Program(name, weight, support)
    return program


programs = {}


def first(input):
    for line in input:
        program = parseLine(line)
        programs[program.name] = program

    for program in programs.values():
        if program.isSupporting():
            children = []
            for childName in program.support:
                child = programs[childName]
                child.parent = program
                children.append(child)
            program.children = children
    for program in programs.values():
        if program.parent is None:
            return program


def second(father):
    father.calculateWeight()
    print(father.display())
    notBalanced = []
    print(father.findNotBalanced(notBalanced))
    value = []
    for child in notBalanced[-1].children:
        print(child.name + ' : ' + str(child.weightPlusChildren))

if __name__ == "__main__":
    with open('test1.txt', 'r') as f:
        test = f.readlines()
    test = [x.strip() for x in test]

    #first(test)

    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    bottom_program = first(content)
    print("1. Le nom du programme tout en bas de la tour est " + bottom_program.name +'.')

    second(bottom_program)

    #print("2. Le résultat est " + str(second(content)))