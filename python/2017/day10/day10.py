test = ['3', '4', '1', '5']

test1 = ''
test2 = 'AoC 2017'
test3 = '1,2,3'
test4 = '1,2,4'

size = 256  # La taille de la liste


def first(input):
    l = list(range(size))  # Liste avec toutes les valeurs
    i = 0  # Current position
    skip_size = 0
    for length in input:
        length = int(length)
        if length > 1:
            # Si on ne sort pas de la taille de la liste
            if i + length < size:
                # On peut sélectionner directement l'intervalle souhaité
                current_list = l[i:(i + length)]
            else:
                # Sinon, on parcourt la liste et on revient au début une fois
                # la dernière valeur atteinte
                j = i
                count = 0
                current_list = []
                while count < length:
                    current_list.append(l[j % size])
                    j += 1
                    count += 1

            current_list = list(reversed(current_list))  # On inverse la liste sélectionnée
            j = i
            count = 0
            # Puis on remplace l'ancienne liste par la nouvelle
            while count < length:
                l[j % size] = current_list[count]
                j += 1
                count += 1

        i = (i + length + skip_size) % size  # On déplace le curseur
        skip_size += 1
    return l[0] * l[1]  # On retourne la multiplication des 2 premiers nombres de la liste finale


def second(input):
    l = list(range(size))
    i = 0  # Current position
    skip_size = 0
    # On va répéter l'opération 64 fois
    for _ in list(range(64)):
        for length in input:
            length = int(length)
            if length > 1:
                if i + length < size:
                    current_list = l[i:(i + length)]
                else:
                    j = i
                    count = 0
                    current_list = []
                    while count < length:
                        current_list.append(l[j % size])
                        j += 1
                        count += 1
                current_list = list(reversed(current_list))
                j = i
                count = 0
                while count < length:
                    l[j % size] = current_list[count]
                    j += 1
                    count += 1
            i = (i + length + skip_size) % size
            skip_size += 1


    # Hachage terminé, on récupère les 256 valeurs et on les regroupe en 16 valeurs hexadécimal
    result = ''
    i = 0
    for _ in list(range(16)):
        group = l[i:(i + 16)]
        regrouped = xor(group)
        result += '{:02x}'.format(regrouped)
        i += 16
    return result


def prepare(input):
    """
    Prépare l'input en passant tous les caractères en nombre ascii
    puis en ajoutant à la liste les valeurs 17, 31, 73, 47, 23
    """
    ascii_codes = []
    for c in input:
        ascii_codes.append(ord(c))
    for add in [17, 31, 73, 47, 23]:
        ascii_codes.append(add)
    return ascii_codes


def xor(n):
    """
    Regroupe les 16 valeurs en une grâce à l'opération binaire XOR ( ^ )
    """
    return n[0] ^ n[1] ^ n[2] ^ n[3] ^ n[4] ^ n[5] ^ n[6] ^ n[7] ^ n[8] ^ n[9] ^ n[10] ^ n[11] ^ n[12] ^ n[13] ^ n[14] ^ n[15]


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        content = f.readline()
    content = content.split(',')

    print("1. Le résultat est " + str(first(content)))

    with open('input.txt', 'r') as f:
        content2 = f.readline()
    content2 = prepare(content2)
    print("2. Le noeud de hachage est " + second(content2))
