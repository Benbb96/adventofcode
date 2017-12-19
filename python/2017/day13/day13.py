test = """0: 3
1: 2
4: 4
6: 4"""


class Layer:

    def __init__(self, depth, rang):
        self.depth = depth
        self.rang = int(rang)
        self.scanner = 1
        self.down = True

    def __str__(self, playerHere):
        txt = self.depth + ' : '
        for i in range(self.rang):
            if playerHere and i == 0:
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

layers = {}


def first(level):
    severity = 0
    for i in range(level):
        #print('Tour n°' + str(i))
        # Ya-t-il un layer avec cette profondeur
        if str(i) in layers.keys():
            if layers[str(i)].scanner == 1:
                #print('Aie !')
                severity += i * layers[str(i)].rang
        for layer in layers.values():
            layer.update()
    return severity


def second(level):
    fail = True
    attempt = 0
    while fail:
        fail = False
        for layer in layers.values():
            layer.reset()  # On remet à 0 les layers
        for delay in range(attempt):
            # On bouge les layers autant de fois qu'il y a eu d'essai
            for layer in layers.values():
                layer.update()
        attempt += 1
        #print('Essai n°' + str(attempt))
        for i in range(level):
            #print('Tour n°' + str(i+1))
            # Ya-t-il un layer avec cette profondeur
            if str(i) in layers.keys():
                if layers[str(i)].scanner == 1:
                    #print('Aie !')
                    fail = True
                    break
            for layer in layers.values():
                print(layer.__str__(layer.depth == str(i)))
                layer.update()

    return attempt -1


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

    print("1. Le résultat est " + str(first(level)))
    for layer in layers.values():
        layer.reset()
    print("2. Le résultat est " + str(second(level)))
