import collections

test = """0: 3
1: 2
4: 4
6: 4"""

layers = collections.OrderedDict()
picoseconds = 0

class Layer:

    def __init__(self, depth, rang):
        self.depth = depth
        self.rang = int(rang)
        self.scanner = 1
        self.down = True

    def __str__(self):
        txt = self.depth + ' : '
        for i in range(self.rang):
            if i == 0 and int(self.depth) == picoseconds:
                if self.scanner == i + 1:
                    txt += ' (S) '
                else:
                    txt += ' ( ) '
            else:
                if self.scanner == i + 1:
                    txt += ' [S] '
                else:
                    txt += ' [ ] '
        return txt

    def reset(self):
        self.scanner = 1
        self.down = True

    def update(self):
        if self.down:
            # Si le scanner descend
            if self.scanner < self.rang:
                self.scanner += 1
            else:
                self.scanner -= 1
                self.down = False
        else:
            # Si le scanner descend
            if self.scanner > 1:
                self.scanner -= 1
            else:
                self.scanner += 1
                self.down = True


def first(level):
    global picoseconds
    severity = 0
    while picoseconds < level:
        print('Tour n°' + str(picoseconds))
        # Ya-t-il un layer avec cette profondeur
        if str(picoseconds) in layers.keys():
            if layers[str(picoseconds)].scanner == 1:
                print('Aie !')
                severity += picoseconds * layers[str(picoseconds)].rang
        for layer in layers.values():
            layer.update()
            print(layer)
        picoseconds += 1
    return severity


def second(level):
    global picoseconds
    fail = True
    attempt = 0
    while fail:
        attempt += 1
        print('Essai n°' + str(attempt))
        fail = False
        for layer in layers.values():
            layer.reset()  # On remet à 0 les layers
        for delay in range(attempt):
            # On bouge les layers autant de fois qu'il y a eu d'essai
            for layer in layers.values():
                layer.update()
        picoseconds = 0
        while picoseconds < level:
            print('Tour n°' + str(picoseconds))
            # Ya-t-il un layer avec cette profondeur
            if str(picoseconds) in layers.keys():
                if layers[str(picoseconds)].scanner == 1:
                    print('Aie !')
                    fail = True
                    break
            for layer in layers.values():
                print(layer)
                layer.update()
            picoseconds += 1

    return attempt


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    test = test.split('\n')

    # Création des layers
    for line in content:
        depth, rang = line.split(': ')
        layers[depth] = (Layer(depth, rang))

    level = int(max(layers, key=int)) + 1

    #print("1. Le résultat est " + str(first(level)))
    for layer in layers.values():
        layer.reset()
    print("2. Le résultat est " + str(second(level)))
